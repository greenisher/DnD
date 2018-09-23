from random import randint

class Dice():
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "Value: {}".format(self.value)

class D3(Dice):
    def __init__(self):
        super().__init__(value = randint(1, 3))

class D4(Dice):
    def __init__(self):
        super().__init__(value = randint(1, 4))

class D6(Dice):
    def __init__(self):
        super().__init__(value = randint(1, 6))

class D8(Dice):
    def __init__(self):
        super().__init__(value = randint(1, 8))

class D10(Dice):
    def __init__(self):
        super().__init__(value = randint(1, 10))

class D12(Dice):
    def __init__(self):
        super().__init__(value = randint(1, 12))

class D20(Dice):
    def __init__(self):
        super().__init__(value = randint(1, 20))
