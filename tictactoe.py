import tkinter as tk
from tkinter import messagebox

size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 100
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
custom_green_color = '#7BC043'


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24, "bold"), width=8, height=4, command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                button.config(bg=custom_green_color)
                self.buttons[i][j] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            color = symbol_X_color if self.current_player == "X" else symbol_O_color
            self.buttons[row][col].config(text=self.current_player, bg=color)

            if self.check_winner(row, col):
                self.show_winner()
            elif self.check_draw():
                self.show_draw()
            else:
                self.toggle_player()

    def check_winner(self, row, col):
        player = self.current_player
        # Check row and column
        if all(self.board[row][c] == player for c in range(3)) or all(self.board[r][col] == player for r in range(3)):
            return True

        # Check diagonals
        if row == col and all(self.board[i][i] == player for i in range(3)):
            return True

        if row + col == 2 and all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(all(cell != "" for cell in row) for row in self.board)

    def toggle_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def show_winner(self):
        winner = self.current_player
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()

    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", bg=custom_green_color)
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
