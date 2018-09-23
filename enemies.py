import diceroll
from random import randint

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Gerblin(Enemy):
    def __init__(self):
        super().__init__(name="Gerblin", hp=10, damage=randint(1, 3))
 
 
class Kobold(Enemy):
    def __init__(self):
        super().__init__(name="Kobold", hp=15, damage=randint(1, 4))

class Hugbear(Enemy):
    def __init__(self):
        super().__init__(name="Hugbear", hp=30, damage=randint(1, 10))
