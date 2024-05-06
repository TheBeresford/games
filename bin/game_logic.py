# This will be the main logic of the game
from player import *
import pandas as pd

class game_board:
    def __init__(self, ) -> None:
        self.ingredients = pd.read_csv('../data/ingredients.csv', delimiter=';', header=0)
        self.board_positions = pd.read_csv('../data/board_positions.csv', delimiter=';', header=0)

if __name__ == "__main__":

    print(ingredients)
