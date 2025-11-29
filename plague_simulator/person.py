from random import randint

class Person:

    def __init__(self, name):
        self.name = name
        self.immune = True
        self.sick = False
        self.symptoms = False


        i = randint(1, 2)
        if i == 1:
            self.immune = False

        if not self.immune:
            i = randint(1, 10)
            if i == 1:
                self.sick == True

        if self.sick:
            i = randint(1, 2)
            if i == 1:
                self.symptoms == True
