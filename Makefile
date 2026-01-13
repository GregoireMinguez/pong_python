NAME = 101pong
SRC = $(NAME).py

all: $(NAME)

$(NAME): $(SRC)
	@cp $(SRC) $(NAME)
	@chmod +x $(NAME)

clean:
	@true

fclean: clean
	@$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
