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

window.keypad(1)
window.timeout(100)

