import random

CLASS Armor:
def__inti__(self, name, max_block):
    self.name = name
    self.max_block = max_block

    def block(self)
    '''return a random value between 0 max_block'''
    return random.randint(0, self.max_block)


    if __name__ == ""__main__:
        sheield = Armor("shield", 30)
        print(sheield.block())