# from tkinter import *
# from tkinter import messagebox
# root = Tk()
# root.title("Login Form")
# root.geometry("350x250")
# root.resizable(False, False)
# def login():
#     username = entry_username.get()
#     password = entry_password.get()
#     if username == "" or password == "": messagebox.showwarning("Warning","Please fill the username and password.")
#     else:
#         if username == "MILAN" and password == "123456789": messagebox.showinfo("Login Success", "Welcome, Admin!")
#         else:
#             messagebox.showerror("Login Failed", "Invalid Username or Password")

# def cancel():
#     entry_username.delete(0, END)
#     entry_password.delete(0, END)
# photo = PhotoImage(file="/Users/milan/Desktop/web project a m/preview.png")
# lable3 = Label(image=photo)
# lable3.place(x=0, y=0)
# label_username = Label( text="Username:")
# label_username.pack(pady=(30, 5))
# entry_username = Entry( width=30)
# entry_username.pack()
# label_password = Label(text="Password:")
# label_password.pack(pady=5)
# entry_password = Entry(width=30, show="*")
# entry_password.pack()
# button_login = Button( text="Login", command=login)
# button_login.pack(pady=10)
# button_cancel = Button(text="Reset", command=cancel)
# button_cancel.pack()
# root.mainloop()


# # import tkinter as tk
# # def start_process(): print("Process Started!")
# # def stop_process(): print("Process Stopped!")
# # window = tk.Tk()
# # window.title("Process Control")
# # window.geometry("300x200")
# # start_button = tk.Button(window, text="Start", command=start_process, width=10, height=2, bg="green", fg="white")
# # start_button.pack(pady=20)
# # stop_button = tk.Button(window, text="Stop", command=stop_process, width=10, height=2, bg="red", fg="white")
# # stop_button.pack(pady=10)
# # window.mainloop()




# import tkinter as tk
# from tkinter import ttk

# #window
# window = tk.Tk()
# window.title('combined layout')
# window.geometry('600x600')
# window.minsize(600,600)

# #main layout widgets
# menu_frame = ttk.Frame(window)
# main_frame = ttk.Frame(window)

# #main place layout
# menu_frame.place(x=0.9, y=0, relwidth = 0.3, relheight= 1)
# main_frame.place(relx = 0.3 ,y=0.9, relwidth = 0.7, relheight= 1)
# #menu widgets
# menu_button1 = ttk.Button(menu_frame,text = 'button 1')
# menu_button2 = ttk.Button(menu_frame,text = 'button 2')
# menu_button3 = ttk.Button(menu_frame,text = 'button 3')

# menu_slider1 = ttk.Scale(menu_frame,orient= 'vertical')
# menu_slider2 = ttk.Scale(menu_frame,orient= 'vertical')

# toggle_frame = ttk.Frame(menu_frame)
# menu_toggle1 = ttk.Checkbutton(toggle_frame,text= 'check1')
# menu_toggle2 = ttk.Checkbutton(toggle_frame,text= 'check2')

# entry = ttk.Entry(menu_frame)

# #menu layout
# menu_frame.columnconfigure((0,1,2), weight= 1, uniform= 'a')
# menu_frame.rowconfigure((0,1,2,3,4), weight= 1, uniform= 'a')

# menu_button1.grid(row= 0, column= 1, sticky= 'nswe', columnspan= 2)
# menu_button2.grid(row= 0, column= 0, sticky= 'nswe')
# menu_button3.grid(row = 1, column = 0, columnspan= 3 ,sticky= 'nswe')

# menu_slider1.grid(row=2 ,column=0, rowspan=2,sticky='nswe' ,pady= 20)
# menu_slider2.grid(row=2 ,column=1, rowspan=2,sticky='nswe' ,pady= 20)

# #toggle layout
# toggle_frame.grid(row =4,column = 0, columnspan =3 ,sticky = 'nsew')
# menu_toggle1.pack(side ='left', expand = True)
# menu_toggle2.pack(side = 'left',expand = True)

# #entry layout
# entry.place(relx= 0.2, rely = 0.95,relwidth= 0.3,anchor= 'center')

# #main widgets
# entry_frame1 = ttk.Frame(main_frame)
# main_label1 = ttk.Label(entry_frame1, text= 'label 1', background= 'red')
# main_button1 = ttk.Button(entry_frame1, text= 'Button 1')

# entry_frame2 = ttk.Frame(main_frame)
# main_label2 = ttk.Label(entry_frame2, text= 'label 2', background= 'blue')
# main_button2 = ttk.Button(entry_frame2, text= 'button 2')


# #main layout
# entry_frame1.pack(side= 'left',expand= True,fill= 'both', padx= 20,pady =20)
# entry_frame2.pack(side= 'left',expand= True,fill= 'both', padx=20 ,pady = 20)

# # ttk.Label(entry_frame1, background= 'red').pack(expand = True,fill = 'both')
# # ttk.Label(entry_frame2, background= 'yellow').pack(expand = True,fill = 'both')

# main_label1.pack(expand= True, fill= 'both')
# main_button1.pack(expand= True, fill = 'both' ,pady= 10)

# main_label1.pack(expand= True, fill= 'both')
# main_button1.pack(expand= True, fill = 'both' ,pady= 10)

# #run
# window.mainloop()


# import tkinter as tk
# from tkinter import ttk, messagebox

# # Window setup
# window = tk.Tk()
# window.title('Dashboard Application')
# window.geometry('700x600')
# window.minsize(700, 600)
# window.configure(bg='#e6f2ff')  # Light blue background for the main window

# # Styling
# style = ttk.Style()
# style.configure('TButton', font=('Arial', 10, 'bold'), padding=5, background='#4CAF50', foreground='white')
# style.configure('TLabel', font=('Arial', 11))
# style.configure('TCheckbutton', font=('Arial', 10), background='#d9d9d9')
# style.configure('TScale', background='#d9d9d9')
# style.configure('TFrame', background='#d9d9d9')  # Background for all frames

# # Menu and main frames with colors
# menu_frame = ttk.Frame(window, style='TFrame')
# main_frame = ttk.Frame(window, style='TFrame')
# menu_frame.place(x=0, y=0, relwidth=0.3, relheight=1)
# main_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

# # Title Label
# title_label = ttk.Label(window, text="User Dashboard", font=('Arial', 16, 'bold'), background='#e6f2ff', foreground='#333')
# title_label.pack(side='top', pady=10)

# # User Info Section
# user_info_label = ttk.Label(menu_frame, text="User Info", font=('Arial', 14, 'bold'), background='#d9d9d9')
# user_info_label.grid(row=0, column=0, columnspan=3, pady=(10, 5))

# name_label = ttk.Label(menu_frame, text="Name:", style='TLabel')
# name_label.grid(row=1, column=0, sticky='w', padx=10)
# name_entry = ttk.Entry(menu_frame, font=('Arial', 10))
# name_entry.grid(row=1, column=1, columnspan=2, sticky='ew', padx=10)

# age_label = ttk.Label(menu_frame, text="Age:", style='TLabel')
# age_label.grid(row=2, column=0, sticky='w', padx=10)
# age_entry = ttk.Entry(menu_frame, font=('Arial', 10))
# age_entry.grid(row=2, column=1, columnspan=2, sticky='ew', padx=10)

# # Separator
# separator = ttk.Separator(menu_frame, orient='horizontal')
# separator.grid(row=3, column=0, columnspan=3, sticky='ew', pady=10)

# # Settings Section
# settings_label = ttk.Label(menu_frame, text="Settings", font=('Arial', 14, 'bold'), background='#d9d9d9')
# settings_label.grid(row=4, column=0, columnspan=3, pady=(10, 5))

# brightness_label = ttk.Label(menu_frame, text="Brightness:", style='TLabel')
# brightness_label.grid(row=5, column=0, sticky='w', padx=10)
# brightness_slider = ttk.Scale(menu_frame, from_=0, to=100, orient='horizontal')
# brightness_slider.grid(row=5, column=1, columnspan=2, sticky='ew', padx=10)

# volume_label = ttk.Label(menu_frame, text="Volume:", style='TLabel')
# volume_label.grid(row=6, column=0, sticky='w', padx=10)
# volume_slider = ttk.Scale(menu_frame, from_=0, to=100, orient='horizontal')
# volume_slider.grid(row=6, column=1, columnspan=2, sticky='ew', padx=10)

# # Toggle Options
# sound_toggle = ttk.Checkbutton(menu_frame, text="Sound Enabled")
# sound_toggle.grid(row=7, column=0, columnspan=3, sticky='w', padx=10, pady=(5, 10))

# dark_mode_toggle = ttk.Checkbutton(menu_frame, text="Dark Mode")
# dark_mode_toggle.grid(row=8, column=0, columnspan=3, sticky='w', padx=10, pady=(0, 10))

# # Apply Settings Button
# apply_button = ttk.Button(menu_frame, text="Apply Settings", style='TButton')

# # Apply Button Functionality
# def apply_settings():
#     name = name_entry.get()
#     age = age_entry.get()
#     brightness = brightness_slider.get()
#     volume = volume_slider.get()
#     sound = sound_toggle.instate(['selected'])
#     dark_mode = dark_mode_toggle.instate(['selected'])
    
#     if not name or not age:
#         messagebox.showwarning("Input Error", "Please enter both your name and age.")
#         return
    
#     # Display settings summary in main frame
#     settings_summary = (
#         f"Hello, {name}! Here is a summary of your settings:\n"
#         f"- Age: {age}\n"
#         f"- Brightness: {int(brightness)}%\n"
#         f"- Volume: {int(volume)}%\n"
#         f"- Sound Enabled: {'Yes' if sound else 'No'}\n"
#         f"- Dark Mode: {'Enabled' if dark_mode else 'Disabled'}"
#     )
#     display_message.set(settings_summary)

# apply_button.config(command=apply_settings)
# apply_button.grid(row=9, column=0, columnspan=3, pady=10, sticky='ew', padx=10)

# # Display Message in Main Frame
# display_message = tk.StringVar()
# message_label = ttk.Label(main_frame, textvariable=display_message, font=('Arial', 12), background='#b3e0ff', padding=10)
# message_label.pack(expand=True, fill='both', padx=20, pady=20)

# # Run the application
# window.mainloop()



# import tkinter as tk
# import random

# # Set up game constants
# WINDOW_SIZE = 400
# GRID_SIZE = 20
# SNAKE_COLOR = "green"
# FOOD_COLOR = "red"
# BG_COLOR = "black"

# # Initialize global variables
# snake_direction = "Right"
# snake_positions = [(100, 100), (80, 100), (60, 100)]
# food_position = (random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
#                  random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
# score = 0

# # Set up the main window
# window = tk.Tk()
# window.title("Snake Game")
# window.resizable(False, False)

# # Set up the canvas
# canvas = tk.Canvas(window, bg=BG_COLOR, width=WINDOW_SIZE, height=WINDOW_SIZE)
# canvas.pack()

# # Update score label
# score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 14))
# score_label.pack()

# # Draw the food
# def create_food():
#     global food_position
#     food_position = (random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
#                      random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
#     canvas.create_rectangle(*food_position, food_position[0] + GRID_SIZE, food_position[1] + GRID_SIZE, fill=FOOD_COLOR)

# # Draw the snake
# def draw_snake():
#     canvas.delete("snake")
#     for pos in snake_positions:
#         canvas.create_rectangle(*pos, pos[0] + GRID_SIZE, pos[1] + GRID_SIZE, fill=SNAKE_COLOR, tags="snake")

# # Move the snake in the current direction
# def move_snake():
#     global snake_positions, score
#     head_x, head_y = snake_positions[0]

#     if snake_direction == "Up":
#         new_head = (head_x, head_y - GRID_SIZE)
#     elif snake_direction == "Down":
#         new_head = (head_x, head_y + GRID_SIZE)
#     elif snake_direction == "Left":
#         new_head = (head_x - GRID_SIZE, head_y)
#     elif snake_direction == "Right":
#         new_head = (head_x + GRID_SIZE, head_y)

#     # Check for collisions
#     if (
#         new_head in snake_positions or  # Collision with itself
#         new_head[0] < 0 or new_head[0] >= WINDOW_SIZE or  # Collision with walls
#         new_head[1] < 0 or new_head[1] >= WINDOW_SIZE
#     ):
#         game_over()
#         return

#     # Move the snake
#     snake_positions = [new_head] + snake_positions[:-1]

#     # Check if the snake eats the food
#     if new_head == food_position:
#         snake_positions.append(snake_positions[-1])
#         score += 1
#         score_label.config(text=f"Score: {score}")
#         canvas.delete("food")
#         create_food()

#     draw_snake()
#     window.after(100, move_snake)

# # Change the snake's direction
# def change_direction(new_direction):
#     global snake_direction
#     opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
#     if new_direction != opposite_directions.get(snake_direction):  # Avoid reversing direction
#         snake_direction = new_direction

# # Handle game over
# def game_over():
#     canvas.delete("all")
#     canvas.create_text(WINDOW_SIZE / 2, WINDOW_SIZE / 2, text="Game Over", fill="white", font=("Arial", 24))
#     canvas.create_text(WINDOW_SIZE / 2, WINDOW_SIZE / 2 + 40, text=f"Score: {score}", fill="white", font=("Arial", 18))

# # Keyboard bindings
# window.bind("<Up>", lambda event: change_direction("Up"))
# window.bind("<Down>", lambda event: change_direction("Down"))
# window.bind("<Left>", lambda event: change_direction("Left"))
# window.bind("<Right>", lambda event: change_direction("Right"))

# # Start the game
# create_food()
# move_snake()
# window.mainloop()



import tkinter as tk
import random
import pickle
 

# Set up game constants
WINDOW_SIZE = 400
GRID_SIZE = 20
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"

# Initialize game variables
snake_direction = "Right"
snake_positions = [(100, 100), (80, 100), (60, 100)]
food_position = (random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                 random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
score = 0
speed = 100  # Speed of snake movement
paused = True  # Start the game in paused mode
high_score = 0

# Load high score from file
try:
    with open("high_score.pkl", "rb") as f:
        high_score = pickle.load(f)
except FileNotFoundError:
    high_score = 0

# Set up the main window
window = tk.Tk()
window.title("Advanced Snake Game")
window.resizable(False, False)

# Set up the canvas
canvas = tk.Canvas(window, bg=BG_COLOR, width=WINDOW_SIZE, height=WINDOW_SIZE)
canvas.pack()

# Update score label
score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 14))
score_label.pack()

# Draw the food
def create_food():
    global food_position
    food_position = (random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                     random.randint(0, (WINDOW_SIZE - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
    canvas.create_rectangle(*food_position, food_position[0] + GRID_SIZE, food_position[1] + GRID_SIZE, fill=FOOD_COLOR, tags="food")

# Draw the snake
def draw_snake():
    canvas.delete("snake")
    for pos in snake_positions:
        canvas.create_rectangle(*pos, pos[0] + GRID_SIZE, pos[1] + GRID_SIZE, fill=SNAKE_COLOR, tags="snake")

# Move the snake in the current direction
def move_snake():
    global snake_positions, score, speed, paused, high_score
    if paused:
        return  # Do nothing if the game is paused

    head_x, head_y = snake_positions[0]
    if snake_direction == "Up":
        new_head = (head_x, head_y - GRID_SIZE)
    elif snake_direction == "Down":
        new_head = (head_x, head_y + GRID_SIZE)
    elif snake_direction == "Left":
        new_head = (head_x - GRID_SIZE, head_y)
    elif snake_direction == "Right":
        new_head = (head_x + GRID_SIZE, head_y)

    # Check for collisions with self or wall
    if (new_head in snake_positions or
        new_head[0] < 0 or new_head[0] >= WINDOW_SIZE or
        new_head[1] < 0 or new_head[1] >= WINDOW_SIZE):
        game_over()
        return

    # Move the snake
    snake_positions = [new_head] + snake_positions[:-1]

    # Check if the snake eats the food
    if new_head == food_position:
        snake_positions.append(snake_positions[-1])
        score += 1
        speed = max(50, speed - 5)  # Increase speed as score goes up
        score_label.config(text=f"Score: {score}")
        canvas.delete("food")
        create_food()

    draw_snake()
    window.after(speed, move_snake)

# Change the snake's direction
def change_direction(new_direction):
    global snake_direction
    opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    if new_direction != opposite_directions.get(snake_direction):  # Avoid reversing direction
        snake_direction = new_direction

# Handle game over
def game_over():
    global high_score
    canvas.delete("all")
    canvas.create_text(WINDOW_SIZE / 2, WINDOW_SIZE / 2, text="Game Over", fill="white", font=("Arial", 24))
    canvas.create_text(WINDOW_SIZE / 2, WINDOW_SIZE / 2 + 40, text=f"Score: {score}", fill="white", font=("Arial", 18))

    # Update high score if needed
    if score > high_score:
        high_score = score
        with open("high_score.pkl", "wb") as f:
            pickle.dump(high_score, f)

    canvas.create_text(WINDOW_SIZE / 2, WINDOW_SIZE / 2 + 80, text=f"High Score: {high_score}", fill="white", font=("Arial", 18))
    pause_game()  # Pause the game after game over

# Toggle pause
def toggle_pause():
    global paused
    paused = not paused
    if not paused:
        move_snake()

# Start the game function
def start_game():
    global paused, score, speed, snake_positions
    paused = False
    score = 0
    speed = 100
    snake_positions = [(100, 100), (80, 100), (60, 100)]
    create_food()
    draw_snake()
    score_label.config(text=f"Score: {score}")
    move_snake()

# Pause the game function
def pause_game():
    global paused
    paused = True

# Save game state
def save_game():
    with open("snake_save.pkl", "wb") as f:
        pickle.dump((snake_positions, food_position, score, snake_direction), f)

# Load game state
def load_game():
    global snake_positions, food_position, score, snake_direction
    try:
        with open("snake_save.pkl", "rb") as f:
            snake_positions, food_position, score, snake_direction = pickle.load(f)
        draw_snake()
        create_food()
        score_label.config(text=f"Score: {score}")
    except FileNotFoundError:
        pass

# Keyboard bindings
window.bind("<Up>", lambda event: change_direction("Up"))
window.bind("<Down>", lambda event: change_direction("Down"))
window.bind("<Left>", lambda event: change_direction("Left"))
window.bind("<Right>", lambda event: change_direction("Right"))
window.bind("<space>", lambda event: toggle_pause())
window.bind("s", lambda event: save_game())
window.bind("l", lambda event: load_game())

# Start and Pause buttons
start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack(pady=5)

pause_button = tk.Button(window, text="Pause Game", command=pause_game)
pause_button.pack(pady=5)

# Start the game initially in paused mode
create_food()
draw_snake()
window.mainloop()
