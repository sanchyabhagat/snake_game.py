#!python2
import curses
import random

# initialize the screen
screen = curses.initscr();
print (3)
# remove the cursor from screen
curses.curs_set(0)

# get the screen height and width
screen_height, screen_width = screen.getmaxyx();

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