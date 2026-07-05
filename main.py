import tkinter as tk
import random

# ---------------- WINDOW ----------------
WIDTH = 600
HEIGHT = 600

root = tk.Tk()
root.title("Catch the Falling Objects")
root.geometry("600x600")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="skyblue")
canvas.pack()

# Keyboard focus
root.focus_force()

# ---------------- VARIABLES ----------------
score = 0
miss = 0
speed = 3
running = False
ball = None

# ---------------- TOP BAR ----------------
score_text = canvas.create_text(
    70, 20,
    text="Score: 0",
    font=("Arial", 14, "bold"),
    fill="black"
)

mode_text = canvas.create_text(
    280, 20,
    text="Mode: -",
    font=("Arial", 14, "bold"),
    fill="blue"
)

miss_text = canvas.create_text(
    520, 20,
    text="Miss: 0",
    font=("Arial", 14, "bold"),
    fill="red"
)

# ---------------- BASKET ----------------
basket = canvas.create_rectangle(
    250, 560,
    350, 585,
    fill="brown"
)

# ---------------- BALL ----------------
BALL_SIZE = 30


def create_ball():
    x = random.randint(20, WIDTH - 20)
    color = random.choice(
        ["red", "blue", "green", "yellow", "orange", "purple"]
    )

    return canvas.create_oval(
        x - 15,
        0,
        x + 15,
        30,
        fill=color
    )


# ---------------- MOVEMENT ----------------
MOVE = 30


def move_left(event):
    x1, y1, x2, y2 = canvas.coords(basket)

    if x1 > 0:
        canvas.move(basket, -MOVE, 0)


def move_right(event):
    x1, y1, x2, y2 = canvas.coords(basket)

    if x2 < WIDTH:
        canvas.move(basket, MOVE, 0)


root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# ---------------- GAME ----------------

def back_to_menu():
    global running, ball

    # Stop the game
    running = False

    # Remove ball
    if ball is not None:
        canvas.delete(ball)
        ball = None

    # Reset texts
    canvas.itemconfig(score_text, text="Score: 0")
    canvas.itemconfig(mode_text, text="Mode: -")
    canvas.itemconfig(miss_text, text="Miss: 0")

    # Remove Game Over message
    canvas.delete("gameover")

    # Hide Back and Restart buttons
    back_btn.place_forget()
    restart_btn.place_forget()

    # Show first screen
    title.place(x=120, y=100)

    easy_btn.place(x=80, y=250)
    medium_btn.place(x=240, y=250)
    hard_btn.place(x=420, y=250)

def start_game(level):
    global speed, running, score, miss, ball

    score = 0
    miss = 0
    running = True

    canvas.itemconfig(score_text, text="Score: 0")
    canvas.itemconfig(miss_text, text="Miss: 0")
    canvas.itemconfig(mode_text, text="Mode: " + level.capitalize())

    if level == "easy":
        speed = 3

    elif level == "medium":
        speed = 6

    else:
        speed = 10

    # Hide buttons
    easy_btn.place_forget()
    medium_btn.place_forget()
    hard_btn.place_forget()
    back_btn.place(x=10, y=35)
    restart_btn.place_forget()
    title.place_forget()

    # Reset basket
    canvas.coords(basket, 250, 560, 350, 585)

    if ball is not None:
        canvas.delete(ball)

    canvas.delete("gameover")

    ball = create_ball()

    animate()


def animate():
    global ball, score, miss

    if not running:
        return

    canvas.move(ball, 0, speed)

    bx1, by1, bx2, by2 = canvas.coords(basket)
    ox1, oy1, ox2, oy2 = canvas.coords(ball)

    # Catch
    if ox2 >= bx1 and ox1 <= bx2 and oy2 >= by1 and oy1 <= by2:

        score += 1

        canvas.itemconfig(score_text,
                          text="Score: " + str(score))

        canvas.delete(ball)
        ball = create_ball()

    # Miss
    elif oy2 >= HEIGHT:

        miss += 1

        canvas.itemconfig(miss_text,
                          text="Miss: " + str(miss))

        canvas.delete(ball)
        ball = create_ball()

        if miss >= 5:
            game_over()
            return

    root.after(30, animate)


def game_over():
    global running

    running = False

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text="GAME OVER\n\nFinal Score: {}".format(score),
        font=("Arial", 24, "bold"),
        fill="red",
        tags="gameover"
    )

    restart_btn.place(x=250, y=380)


def restart():
    global running

    running = False

    canvas.delete("gameover")

    restart_btn.place_forget()

    back_to_menu()

# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="Catch the Falling Objects",
    font=("Arial", 22, "bold")
)

title.place(x=120, y=100)

# ---------------- BUTTONS ----------------

easy_btn = tk.Button(
    root,
    text="Easy",
    width=12,
    bg="lightgreen",
    font=("Arial", 12),
    command=lambda: start_game("easy")
)

medium_btn = tk.Button(
    root,
    text="Medium",
    width=12,
    bg="yellow",
    font=("Arial", 12),
    command=lambda: start_game("medium")
)

hard_btn = tk.Button(
    root,
    text="Hard",
    width=12,
    bg="tomato",
    font=("Arial", 12),
    command=lambda: start_game("hard")
)

restart_btn = tk.Button(
    root,
    text="Restart",
    width=12,
    font=("Arial", 12),
    command=restart
)

back_btn = tk.Button(
    root,
    text="⬅ Back",
    width=10,
    bg="lightblue",
    font=("Arial", 11, "bold"),
    command=back_to_menu
)

easy_btn.place(x=80, y=250)
medium_btn.place(x=240, y=250)
hard_btn.place(x=420, y=250)

root.mainloop()