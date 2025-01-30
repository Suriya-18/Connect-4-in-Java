import tkinter as tk
from tkinter import messagebox

class Connect4:
    def __init__(self):
        self.ROWS = 6
        self.COLS = 7
        self.EMPTY = 'E'
        self.board = [[self.EMPTY for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.currentPlayerPiece = 'X'
        
        self.root = tk.Tk()
        self.root.title("Connect 4")
        
        self.buttons = [[None for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.init_gui()
        
        self.switch_player()
        self.root.mainloop()
    
    def init_gui(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.grid(row=0, column=0)
        
        for row in range(self.ROWS):
            for col in range(self.COLS):
                self.buttons[row][col] = tk.Button(
                    self.board_frame, text="", width=6, height=3,
                    command=lambda c=col: self.button_click(c)
                )
                self.buttons[row][col].grid(row=row, column=col)
    
    def button_click(self, col):
        row = self.drop_piece(col)
        if row != -1:
            button = self.buttons[row][col]
            button.config(text=self.currentPlayerPiece, state=tk.DISABLED,
                          bg='black' if self.currentPlayerPiece == 'X' else 'red')
            
            if self.check_win(row, col, self.currentPlayerPiece):
                messagebox.showinfo("Game Over", f"Player {self.currentPlayerPiece} has won!")
                self.disable_all_buttons()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "The game is a draw.")
                self.disable_all_buttons()
            else:
                self.switch_player()
    
    def drop_piece(self, col):
        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][col] == self.EMPTY:
                self.board[row][col] = self.currentPlayerPiece
                return row
        return -1
    
    def check_win(self, row, col, player_piece):
        return (self.check_direction(row, col, player_piece, 0, 1) or  # Horizontal
                self.check_direction(row, col, player_piece, 1, 0) or  # Vertical
                self.check_direction(row, col, player_piece, 1, 1) or  # Diagonal /
                self.check_direction(row, col, player_piece, 1, -1))   # Diagonal \
    
    def check_direction(self, row, col, player_piece, row_dir, col_dir):
        count = 0
        for d in range(-3, 4):
            r, c = row + d * row_dir, col + d * col_dir
            if 0 <= r < self.ROWS and 0 <= c < self.COLS and self.board[r][c] == player_piece:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
        return False
    
    def check_draw(self):
        return all(self.board[0][col] != self.EMPTY for col in range(self.COLS))
    
    def switch_player(self):
        self.currentPlayerPiece = 'O' if self.currentPlayerPiece == 'X' else 'X'
        self.root.title(f"Player {self.currentPlayerPiece}'s Turn")
    
    def disable_all_buttons(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                self.buttons[row][col].config(state=tk.DISABLED)

if __name__ == "__main__":
    Connect4()
