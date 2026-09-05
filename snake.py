import curses
import random

def main(stdscr):
    # Setup terminal screen settings
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    sh, sw = stdscr.getmaxyx()

    # Define initial positions for the snake and game boundaries
    snake_x = sw // 4
    snake_y = sh // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    # Spawn the first piece of food
    food = [sh // 2, sw // 2]
    stdscr.addch(food[0], food[1], curses.ACS_PI)

    # Initial movement direction (moving right)
    key = curses.KEY_RIGHT

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        # Calculate the new head position based on current direction
        head = snake[0]
        if key == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        elif key == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif key == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif key == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]

        snake.insert(0, new_head)

        # Check collision with borders or itself
        if (new_head[0] in [0, sh-1] or 
            new_head[1] in [0, sw-1] or 
            new_head in snake[1:]):
            break

        # Check if snake eats the food
        if snake[0] == food:
            food = None
            while food is None:
                new_food = [random.randint(1, sh-2), random.randint(1, sw-2)]
                food = new_food if new_food not in snake else None
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

curses.wrapper(main)

