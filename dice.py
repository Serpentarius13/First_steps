from random import randint
from time import sleep

conti = True
""" This program rolls dice of n = input sides that user chooses.
 When player quits, prints average result threw while played """

class Die():
    def __init__(self):
        self.results = []
        sides = '0'
        self.sides = sides

    def inputting(self):
        sides = int(input('How many sides this dice has? '))
        self.sides = sides
        return self.sides

    def continuing(self):
        cont = input('Do we continue? ')
        if cont in ['No', 'no']:
            print('Okay!')
            avg = sum(self.results) / len(self.results)
            print('Средний результат по броскам: ')
            print(f"\t {avg}")
            exit()

    def roll_dice(self):
        dice_result = randint(1, self.sides)
        print(f"By rolling dice with {self.sides} sides, the result is:")
        sleep(1)
        print(f"\t {dice_result}")
        self.results.append(dice_result)




roll = Die()

while conti:
    roll.inputting()
    roll.roll_dice()
    roll.continuing()






