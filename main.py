import tkinter as tk
from PIL import ImageTk, Image
from random import randint
from tkinter import messagebox

def resize_image(image_path, size=(500, 500)):
    original_image = Image.open(image_path)
    resized_image = original_image.resize(size)
    tk_image = ImageTk.PhotoImage(resized_image)
    return tk_image

def new_game():
    global randomNumber, attempts
    randomNumber = randint(1, 10)
    attempts = 3
    update_feedback("New game started. Guess a number between 1 and 10.")
    update_attempts()

def update_feedback(message):
    feedback_label.config(text=message)

def update_attempts():
    attempts_label.config(text=f"Attempts left: {attempts}")

def check_guess():
    global attempts
    try:
        guessNumber = int(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")
        return

    if attempts > 0:
        if randomNumber > guessNumber:
            update_feedback("You chose a small number. Try again.")
        elif randomNumber < guessNumber:
            update_feedback("You chose a big number. Try again.")
        else:
            messagebox.showinfo("Congratulations", f"Congratulations! You guessed the number {randomNumber} correctly.")
            new_game()
            return
        attempts -= 1
        update_attempts()
        if attempts == 0:
            messagebox.showwarning("Game Over", f"You ran out of attempts. The correct number was {randomNumber}.")
            new_game()

# Main Tkinter window
root = tk.Tk()
root.title("Guess Game")
root.resizable(False, False)

# Load background image
page = resize_image('bg_image1.jpeg')
label = tk.Label(root, image=page)
label.pack()

# Frame for widgets
frame = tk.Frame(root, width="200", height="200", bg="black", bd=0)
# frame.pack(padx=80, pady=100)
frame.place(x = 80, y = 100)
# Define a function to clear the placeholder text
def onEnter(entry_widget, placeholder):
    if entry_widget.get() == placeholder:
        entry_widget.delete(0, 'end')
        entry_widget['fg'] = 'green'  # Change text color to black when the user clicks to enter data

# Define a function to insert the placeholder text if the field is empty
def onLeave(entry_widget, placeholder):
    if not entry_widget.get():
        entry_widget.insert(0, placeholder)
        entry_widget['fg'] = 'green'  # Change text color back to gray for the placeholder text

# Entry widget
entry = tk.Entry(frame, width=25, border=0, fg="green", bg="black",
                  font=('Work Sans', 16, 'bold'), borderwidth=12)
entry.insert(0, "Guess the lucky Number :) ")
entry.bind('<FocusIn>', lambda e: onEnter(entry, "Guess the lucky Number :) "))
entry.bind('<FocusOut>', lambda e: onLeave(entry, "Guess the lucky Number :) "))
entry.pack()

# Button to check the guess
check_button = tk.Button(frame, text="Check!", font=("Work Sans", 16), bg='black', fg='green', command=check_guess)
check_button.pack(padx=60, pady=15)

# Button to start a new game
new_game_button = tk.Button(frame, text="New Game", font=("Work Sans", 16), bg='black', fg='green', command=new_game)
new_game_button.pack(pady=15)

# Label for feedback
feedback_label = tk.Label(frame, text="New game started. Guess a number between 1 and 10.", font=("Work Sans", 12), fg="green", bg="black", bd=0)
feedback_label.pack(pady=15)

# Label for attempts
attempts_label = tk.Label(frame, text="Attempts left: 3", font=("Work Sans", 12), fg="red", bg="black",  bd=0)
attempts_label.pack(pady=15)

# Bind events for hover effect
def on_enter(event):
    check_button.config(bg='green', fg='black')
    new_game_button.config(bg='green', fg='black')

def on_leave(event):
    check_button.config(bg='black', fg='green')
    new_game_button.config(bg='black', fg='green')

check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)
new_game_button.bind("<Enter>", on_enter)
new_game_button.bind("<Leave>", on_leave)

# Start a new game when the application starts
new_game()

# Main Tkinter loop
root.mainloop()



