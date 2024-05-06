# This will be the main logic of the game
from player import *
import pandas as pd

class game_board:
    def __init__(self, ) -> None:

if __name__ == "__main__":

    ingredients = pd.read_csv('../data/ingredients.csv', delimiter = ";", header=0)
    board_positions = pd.read_csv('../data/board_positions.csv', delimiter=';', header=0)

    print(ingredients)
