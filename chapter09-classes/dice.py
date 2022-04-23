from random import randint

class Die():

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, number_of_rolls=1):
        for i in range(0, number_of_rolls):
            print(randint(1, self.sides))

if __name__ == "__main__":
    # 6-sided die
    die = Die(6)
    die.roll_die(10)

    # 10-sided die
    die_10 = Die(10)
    die_10.roll_die(10)