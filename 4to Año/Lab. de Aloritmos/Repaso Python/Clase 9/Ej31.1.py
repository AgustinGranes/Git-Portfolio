import random

class dice:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
        lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        for i in lista:
            print(random.randint(1, self.sides))
        print()

dado1 = dice()
dado2 = dice(10)
dado3 = dice(20)


dado1.roll_dice()
dado2.roll_dice()
dado3.roll_dice()