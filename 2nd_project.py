import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def _init_(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#f4f4f4")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        tk.Label(root, text="Guess a number (1-100)", font=("Arial", 14, "bold"), bg="#f4f4f4").pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Submit", command=self.check_guess, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f4f4f4", fg="blue")
        self.result_label.pack(pady=5)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game, font=("Arial", 12), bg="#2196F3", fg="white")
        self.restart_button.pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1

            if user_guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.", fg="red")
            elif user_guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.", fg="red")
            else:
                messagebox.showinfo("You Win!", f"Correct! You guessed it in {self.attempts} attempts.")
                self.restart_game()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def restart_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="", fg="blue")
        self.entry.delete(0, tk.END)

# Run the game
if _name_ == "_main_":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
