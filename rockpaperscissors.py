import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        self.player_score = 0
        self.computer_score = 0
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Choose your move:", font=("Arial", 14, "bold"), foreground="black")  # Change font color to black
        self.label.pack(pady=10)

        self.buttons_frame = ttk.Frame(self.root)
        self.buttons_frame.pack()

        self.buttons = []
        moves = ["Rock", "Paper", "Scissors"]
        colors = ["#FF5733", "#33FF48", "#334BFF"]  # Colors for Rock, Paper, Scissors buttons

        for i, move in enumerate(moves):
            style = ttk.Style()
            style.configure(f"Custom.TButton{i}.TButton",
                            font=("Arial", 14, "bold"),
                            background=colors[i],
                            foreground="black",  # Set font color to black
                            width=10,
                            height=3)

            button = ttk.Button(self.buttons_frame, text=move, command=lambda m=move: self.play_round(m), style=f"Custom.TButton{i}.TButton")
            button.pack(side=tk.LEFT, padx=10)

            self.buttons.append(button)

        self.result_label = ttk.Label(self.root, text="", font=("Arial", 20), foreground="black")  # Change font color to black
        self.result_label.pack(pady=20)

        self.score_label = ttk.Label(self.root, text="Score: 0 - 0", font=("Arial", 16, "bold"), foreground="black")  # Change font color to black and set font to bold
        self.score_label.pack()

    def play_round(self, player_move):
        computer_move = random.choice(["Rock", "Paper", "Scissors"])

        result = self.get_round_result(player_move, computer_move)

        self.result_label.config(text=f"You chose {player_move}. Computer chose {computer_move}. {result}", foreground="black")  # Change font color to black

        if result.startswith("You"):
            self.player_score += 1
        elif result.startswith("Computer"):
            self.computer_score += 1

        self.update_score_label()

    def get_round_result(self, player_move, computer_move):
        if player_move == computer_move:
            return "It's a tie!"
        elif (player_move == "Rock" and computer_move == "Scissors") or \
             (player_move == "Paper" and computer_move == "Rock") or \
             (player_move == "Scissors" and computer_move == "Paper"):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.player_score} - {self.computer_score}", foreground="black")  # Change font color to black

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
