'''This is the TicTacToe game mechanism written in OOP'''
import random

class TicTacToe:
    COLUMNS = ['A', 'B', 'C']
    ROWS = ['1', '2', '3']

    def __init__(self):
        self.grid = self.create_grid()
        self.current_player = 'X'

    def create_grid(self):
        return {char + numb: "_" for char in self.COLUMNS for numb in self.ROWS}

    def print_grid(self):
        print('  A B C')
        for row in self.ROWS:
            print(f"{row} {'|'.join(self.grid[char + row] for char in self.COLUMNS)}")

    def check_win(self):
        for row in self.ROWS:
            if self.is_equal(self.grid['A' + row], self.grid['B' + row], self.grid['C' + row]):
                return True
        for col in self.COLUMNS:
            if self.is_equal(self.grid[col + '1'], self.grid[col + '2'], self.grid[col + '3']):
                return True
        if self.is_equal(self.grid['A1'], self.grid['B2'], self.grid['C3']):
            return True
        if self.is_equal(self.grid['C1'], self.grid['B2'], self.grid['A3']):
            return True
        return False

    def is_equal(self, *args):
        return args[0] != "_" and all(arg == args[0] for arg in args)

    def move(self, cell, figure):
        if self.grid[cell] == '_':
            self.grid[cell] = figure
            return True
        else:
            print(f"The cell {cell} is taken, choose another one")
            return False

    def auto_move(self, figure):
        all_cells = [col + row for col in self.COLUMNS for row in self.ROWS]
        while True:
            cell = random.choice(all_cells)
            if self.grid[cell] == '_':
                self.grid[cell] = figure
                return

    def get_player_move(self):
        return input("Please make your move (e.g., A1, B3): ")

    def play(self):
        while True:
            self.print_grid()

            if self.current_player == 'X':
                move_made = False
                while not move_made:
                    player_move = self.get_player_move()
                    move_made = self.move(player_move, self.current_player)
                if self.check_win():
                    self.print_grid()
                    print("Congratulations, the 'X' player has won!")
                    break

            else:
                self.auto_move('O')
                if self.check_win():
                    self.print_grid()
                    print("Sorry, the player 'O' has won!")
                    break

            self.current_player = 'O' if self.current_player == 'X' else 'X'