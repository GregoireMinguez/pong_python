#!/usr/bin/python3

import math
import sys

HELP_TEXT = """USAGE
    ./101pong x0 y0 z0 x1 y1 z1 n
    

DESCRIPTION
    x0  ball abscissa at time t - 1
    y0  ball ordinate at time t - 1e
    z0  ball altitude at time t - 1
    x1  ball abscissa at time t
    y1  ball ordinate at time t
    z1  ball altitude at time t
    n   time shift (greater than or equal to zero, integer)"""


def fmt(value):
    return f"{value:.2f}"


def print_error(message):
    print(message, file=sys.stderr)
    sys.exit(84)


def parse_args(args):
    if len(args) == 1 and args[0] in ("-h", "--help"):
        print(HELP_TEXT)
        sys.exit(0)
    if len(args) != 7:
        print_error(HELP_TEXT)
    try:
        x0, y0, z0 = map(float, args[0:3])
        x1, y1, z1 = map(float, args[3:6])
        n = int(args[6])
        if n < 0:
            print_error(HELP_TEXT)
        return x0, y0, z0, x1, y1, z1, n
    except (TypeError, ValueError):
        print_error(HELP_TEXT)


def main(argv):
    x0, y0, z0, x1, y1, z1, n = parse_args(argv)
    vx = x1 - x0
    vy = y1 - y0
    vz = z1 - z0

    xn = x1 + n * vx
    yn = y1 + n * vy
    zn = z1 + n * vz

    print("The velocity vector of the ball is:")
    print(f"({fmt(vx)}, {fmt(vy)}, {fmt(vz)})")
    print(f"At time t + {n}, ball coordinates will be:")
    print(f"({fmt(xn)}, {fmt(yn)}, {fmt(zn)})")

    hit = False
    if vz != 0:
        t_hit = -z1 / vz
        hit = t_hit >= 0
    else:
        hit = z1 == 0

    if hit:
        speed = math.sqrt(vx * vx + vy * vy + vz * vz)
        if speed == 0:
            angle = 0.0
        else:
            ratio = abs(vz) / speed
            clamped = min(max(ratio, 0.0), 1.0)
            angle = math.degrees(math.asin(clamped))
        print("The incidence angle is:")
        print(f"{fmt(angle)} degrees")
    else:
        print("The ball won't reach the paddle.")


if __name__ == "__main__":
    main(sys.argv[1:])

