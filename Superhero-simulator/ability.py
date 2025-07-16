import random

Class Ability:
    def__inti__(self, name, max_damage)
    self.name = name
        self.max_damage = max_damage

        def attack(self):
            '''Returns a random value between 0 and max_damage.'''
            return random.randint(0, self.max_damage + 1)
         

if_name__ == "__main__":
    fireball = Ability("fireball", 50)
    print(fireball.attack())