#!python2
import curses
import random

# initialize the screen
screen = curses.initscr();
#print(3)
# remove the cursor from screen
curses.curs_set(0)

# get the screen height and width
screen_height, screen_width = screen.getmaxyx()

#initialize a new window with the height and width
window = curses.newwin(screen_height,screen_width,0,0)

# accept keypad input
window.keypad(1)
window.timeout(100)

# add snake body
snake_x = screen_width / 4
snake_y = screen_height / 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

print (str(snake_x) + ' ' + str(snake_y))

food = [screen_height/2, screen_width/2]
window.addch(food[0], food[1], curses.ACS_PI)
#print (window)

# initial direction of snake
key = curses.KEY_RIGHT

#Start game here
while True:
    #get key pressed
    key_pressed = window.getch()
    if key_pressed == -1:
        key = key
    else:
        key = key_pressed

    #game lost
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    # determine the new head position of the snake
    newHeadPosition = [snake[0][0], snake[0][1]]

    # update the new head according to key press

    if key == curses.KEY_DOWN:
        newHeadPosition[0] += 1
    elif key == curses.KEY_UP:
        newHeadPosition[0] -= 1
    elif key == curses.KEY_LEFT:
        newHeadPosition[1] -= 1
    elif key == curses.KEY_RIGHT:
        newHeadPosition[1] += 1

    #add the new head
    snake.insert(0, newHeadPosition)

    #check if snake ran into the food
    if snake[0] == food:
        food = None
        while food is None:
            newFoodPosition = [
                random.randint(1, screen_height-1),
                random.randint(1, screen_width-1)
            ]
            food = newFoodPosition if newFoodPosition not in snake else None

        # add the food again
        window.addch(food[0], food[1], curses.ACS_PI)
    