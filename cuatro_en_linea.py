import tkinter as tk
from tkinter import messagebox

class ConnectFour:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Conecta Cuatro")

        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'Red'
        self.red_wins = 0
        self.yellow_wins = 0

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        self.restart_button = tk.Button(self.buttons_frame, text="Reiniciar Partida", command=self.restart_game)
        self.restart_button.grid(row=0, column=0, padx=10)

        self.reset_scores_button = tk.Button(self.buttons_frame, text="Resetear Contador", command=self.reset_scores)
        self.reset_scores_button.grid(row=0, column=1, padx=10)

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.buttons = []
        for row in range(6):
            row_buttons = []
            for col in range(7):
                button = tk.Button(self.board_frame, text='', width=4, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_button(row, col)
            
            if self.check_win(row, col):
                self.show_winner()
                self.restart_game()
            elif self.check_draw():
                messagebox.showinfo("Empate", "La partida ha terminado en empate.")
                self.restart_game()
            else:
                self.switch_player()

    def update_button(self, row, col):
        color = 'red' if self.current_player == 'Red' else 'yellow'
        self.buttons[row][col].configure(text='', bg=color, state=tk.DISABLED)

    def switch_player(self):
        self.current_player = 'Red' if self.current_player == 'Yellow' else 'Yellow'

    def check_win(self, row, col):
        return (self.check_line(row, col, 0, 1) or   # Horizontal
                self.check_line(row, col, 1, 0) or   # Vertical
                self.check_line(row, col, 1, 1) or   # Diagonal \
                self.check_line(row, col, -1, 1))    # Diagonal /

    def check_line(self, row, col, row_direction, col_direction):
        player = self.current_player
        count = 0

        for i in range(-3, 4):
            new_row = row + i * row_direction
            new_col = col + i * col_direction

            if 0 <= new_row < 6 and 0 <= new_col < 7:
                if self.board[new_row][new_col] == player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def show_winner(self):
        winner = 'Roja' if self.current_player == 'Red' else 'Amarilla'
        messagebox.showinfo("¡Ganador!", f"{winner} gana la partida.")
        
        if self.current_player == 'Red':
            self.red_wins += 1
        else:
            self.yellow_wins += 1

        self.update_scores_display()

    def update_scores_display(self):
        messagebox.showinfo("Puntuación", f"Fichas Rojas: {self.red_wins}\nFichas Amarillas: {self.yellow_wins}")

    def restart_game(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        for row in self.buttons:
            for button in row:
                button.configure(text='', bg='white', state=tk.NORMAL)

        self.current_player = 'Red'

    def reset_scores(self):
        self.red_wins = 0
        self.yellow_wins = 0
        self.update_scores_display()

if __name__ == "__main__":
    game = ConnectFour()