# Importing the modules
from tkinter import * 
import random

# Constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 95
SPACE_SIZE = 25
BODY_PARTS = 2
SNAKE_COLOR = "#6A005C"
FOOD_COLOR = "#FFFFFF"
BACKGROUND_COLOR = "#EA8BFD"


class Snake:


    def __init__(self):
        self.body_size = BODY_PARTS # snake body size
        self.coordinates = [] # coordinates of the snake
        self.squares = [] # squares that make up the snake

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0]) # snake appears in top left corner

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)
            canvas.itemconfig(square, fill=SNAKE_COLOR)
    pass

class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")

    pass

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":    
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y)) # add new coordinates to the front of the snake

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
    
    snake.squares.insert(0, square) # add new square to the front of the snake

    if x == food.coordinates[0] and y == food.coordinates[1]: # if the snake eats the food

        global score 

        score += 1

        label.config(text = "Score: {}".format(score))

        canvas.delete("food") # remove the old food

        food = Food() # create new food

    else:
        del snake.coordinates[-1] # remove the last coordinate

        canvas.delete(snake.squares[-1]) # remove the last square

        del snake.squares[-1] # remove the last square

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right': # this stops the snake from doing a 180 degree turn
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
        
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font = ('arial', 70), text = "GAME OVER", fill = "red", tag = "gameover")
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text = "Score: {}".format(score), font = ("arial", 40))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2 - window_width/2))
y = int((screen_width/2 - window_width/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Right>", lambda event: change_direction('right'))
window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down')) # bind the arrow keys to the change_direction function

food = Food()
snake = Snake()

next_turn(snake, food)

window.mainloop()

