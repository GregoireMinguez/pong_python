# pong_python

Simple Pong-inspired visualization used to display the results of the `101pong` math assignment.

## Requirements

- Python 3.x with the Tkinter module available (on Debian/Ubuntu install `python3 python3-tk`, on Fedora `python3 python3-tkinter`, on macOS use the Python that ships with Xcode or Homebrew which already includes Tk).


### Using Python directly

```bash
python3 101pong.py x0 y0 z0 x1 y1 z1 n
```

- `x0`, `y0`, `z0`: ball coordinates at time `t - 1`
- `x1`, `y1`, `z1`: ball coordinates at time `t`
- `n`: non-negative integer time shift

### Using the provided executable

```bash
make        # creates ./101pong
./101pong x0 y0 z0 x1 y1 z1 n
```

The program prints the velocity vector, future coordinates at `t + n`, and whether the ball will hit the paddle (plus the incidence angle). A Tk window also opens with a small Pong game that visualizes the current computation. Controls: left paddle uses `W/S`, right paddle uses the Up/Down arrows.
