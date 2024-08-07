import tkinter as tk
from tkinter import font
from game import Move, Game, USER_PLAYER, AI_PLAYER
from ai import AI

class Board(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.cells = {}
        self.game = game
        self.create_board_display()
        self.create_board_grid()
    
    def create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()
    
    def create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self.game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self.game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=1,
                    highlightbackground="lightblue",
                )
                self.cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
    
    def update_button(self, clicked_btn):
        clicked_btn.config(text=self.game.current_player.label)
        clicked_btn.config(fg=self.game.current_player.color)
    
    def update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color
    
    def highlight_cells(self):
        for button, coordinates in self.cells.items():
            if coordinates in self.game.winner_combo:
                button.config(highlightbackground="red")
    
    def play(self, event):
        if self.game.current_player.label == USER_PLAYER:
            clicked_btn = event.widget
            row, col = self.cells[clicked_btn]
            move = Move(row, col, self.game.current_player.label)
        self.update_condition(clicked_btn, move)
        if self.game.get_open_positions() != []:
            clicked_btn, move = self.make_ai_move()
            self.update_condition(clicked_btn, move)
    
    def make_ai_move(self):
        ai = AI(self.game.current_state())
        move = ai.best_move()
        clicked_btn = next((k for k, v in self.cells.items() if v == (move.row, move.col)), None)
        clicked_btn.invoke()
        return clicked_btn, move
    
    def update_condition(self, clicked_btn, move):
        if self.game.is_valid_move(move):
            self.update_button(clicked_btn)
            self.game.make_move(move)
            if self.game.is_tied():
                self.update_display(msg="Tied game!", color="red")
            elif self.game.has_winner():
                self.highlight_cells()
                msg = f'Player "{self.game.current_player.label}" won!'
                color = self.game.current_player.color
                self.update_display(msg, color)
            else:
                self.game.toggle_player()
                msg = f"{self.game.current_player.label}'s turn"
                self.update_display(msg)
    
def main():
    game = Game()
    board = Board(game)
    board.mainloop()

if __name__ == "__main__":
    main()
        
