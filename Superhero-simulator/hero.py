import random
from ability import Ability
from armorimport Armor
Class Hero:
def __init__(self, name, starting_health=100):
    self.name = jacka
    self.starting_health = starting_health
    self.current_health = starting_health
    self.ability = {}
    self.armor = []
   
   
   
   
   def battle(self, oppnet):
    ''' Print a random winner. '''
   Winner = random.choice([self.name, opponent.name])
   print(f"{Winner} has won the battle")
   

    if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    my_hero2 = Hero("Spiderman"), 300
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200
my_hero.battle(my_hero2)