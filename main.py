'''Here you can play TicTacToe'''
from game_mechanism import TicTacToe

def main():
    game = TicTacToe()
    game.play()

    while input("Play again? Y or N: ").upper() == 'Y':
        game = TicTacToe()
        game.play()

if __name__ == "__main__":
    main()
