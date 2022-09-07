from random import randint

class Guessing():

    def __init__(self):
        """Core of the class Guessing which contains all variables used below"""
        self.results = []

        self.tryouts = 1
        self.max_number = ''
        self.variable = ''
        self.trying = ''
        self.input_1 = 'Hello. Do you want to play a game? '
        self.input_2 = 'Do you want to play again? '
        self.input_3 = 'Pick a number! '


    def entrance(self):
        """Asking if player wants to play a game"""
        play = input(self.input_1)
        if play in ['no','No']:
            print('Why would you even open this app then?')
            print('Goodbye!')
            exit()
        else:
            print('Okay!')


    def game(self):
        """Key function of our class which
        a) Asks for a max number for a range in which we are going to be playing
        b) Sets a variable to play for and prompts user for his choice
        c) Checks if user's choice is equal to set variable
        d) When the round is complete shows the amount of attempts done by user"""
        if self.max_number == '':
            try:
                self.max_number = int(input(self.input_3))  # Prompting maximum number in range
            except ValueError:
                print('Please, pick a real number!')
            except TypeError:
                print('Please, pick a real number!')
        elif self.max_number == 1 or self.max_number == 2:
            print('That would be too easy.')
            pass
        self.variable = randint(1, self.max_number)  # Evaluating the variable to search for
        while True:
            try:
                self.trying = int(input(f"Guess a number between 1 and {self.max_number} "))  # Prompts user for his choice
            except ValueError:
                print('Please, pick a number!')
            except TypeError:
                print('Please, pick a number!')
            else:
                if self.trying > self.max_number:  # From here on checks the value
                    print("This number is higher than the maximum one! Please, choose another one!")
                    pass
                elif self.trying < 1:
                    print("You can't enter a number below 1! Please, choose another one!")
                    pass
                elif self.trying > self.variable:
                    print('Too much!')
                    self.tryouts += 1
                    pass
                elif self.trying < self.variable:
                    print('Too low!')
                    self.tryouts += 1
                    pass
                elif self.trying == self.variable:  # Statement of winning
                    print("Nice! You've won!")
                    print(f"The amount of attempts on this run was: {self.tryouts} times! Good job!")
                    self.results.append(self.tryouts)  # Appending result to final list
                    self.tryouts = 1
                    break


    def play_again(self):
        """
        Asks player if he wants to play again.
        If he refuses, prints final results"""

        again = input('Do you want to play again? ')  # Asking if user wants to play again
        if again in ['yes', 'Yes']:
            print('Okay!')
            return True
        else:
             print('Fine!')
            for i, trying in enumerate(self.results, 1):  # Passing final results at the end
                print(f"Attempt number {i}'s result was: {trying}")
            exit()


    def change_number(self):
        """ Asks player if they want to change maximum number"""
        new_n_q = input('Do you want to change a number? ')  # Asking if he wants to change a numb.
        if new_n_q in ['yes','Yes']:
            self.max_number = int(input(self.input_3))
            self.variable = randint(1, self.max_number)
            pass
        else:
            print(f"The number remains {self.max_number}!")
            self.variable = randint(1, self.max_number)
            pass


guess = Guessing()
guess.entrance()
while True:
    guess.game()
    if guess.play_again():
        guess.change_number()
