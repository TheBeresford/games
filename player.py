import random
import copy

class ingredient:
  def __init__(self, name: str, value: int) -> None:
    self.name = name
    self.value = value

class player:
  def __init__(self) -> None:
    # Initiate the bag for the player, starting bags are always the same.
    self.bag_reference: list = [
      ingredient(cherry, 1),
      ingredient(cherry, 1),
      ingredient(cherry, 1),
      ingredient(cherry, 1),
      ingredient(cherry, 2),
      ingredient(cherry, 2),
      ingredient(cherry, 4),
      ingredient(pumpkin, 1),
      ingredient(spider, 1)
    ]
    self.bag: list = copy.deepcopy(self.bag_reference)
    self.potion: bool = True
    self.rubies: int = 0
    self.victory_points: int = 0

  def replenish_bag(self) -> None:
    # Method to replenish the player bag every round, from the "stable" bag_reference list.
    # This method uses "deepcopy" from the copy library.
    self.bag = copy.deepcopy(self.bag_reference)
  
  def draw_from_bag(self) -> ingredient:
    # Get a random index from the bag and return that item.
    random_index = random.randit(0, len(self.bag) - 1)
    return self.bag.pop(random_index)

  def add_item(self, ingredient):
    self.bag.append(ingedient)
    self.bag_reference.append(ingedient)

if __name__ == "__main__":

  # Initiate the player
  Player1 = player()
  
