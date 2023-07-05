# Importing the modules
from tkinter import * 
import random

# Constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#F38BFD"
FOOD_COLOR = "#FD8B8D"
BACKGROUND_COLOR = "#EA8BFD"


class Snake:
    pass

class Food:
    pass

def next_turn(new_direction):
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text = "Score: {}".format(score), font = ("consolas", 40))
label.pack()


window.mainloop

