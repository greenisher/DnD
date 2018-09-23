from random import randint

class Item():
    """The base class for items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    
class Gold(Item):
    def __init__(self):
        super().__init__(name="Gold",
                         description="A round coin.",
                         value=1)

                         
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Axe",
                         description="A woodcutter's axe",
                         value=10,
                         damage = randint(1, 4))

class Knife(Weapon):
    def __init__(self):
        super().__init__(name="Knife",
                     description="A simple knife",
                     value=5,
                     damage = randint(1, 4))

class Spear(Weapon):
    def __init__(self):
        super().__init__(name="Spear",
                     description="A light spear",
                     value=15,
                     damage = randint(1, 6))
class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                     description="A rusted sword",
                     value=15,
                     damage = randint(1, 6))

class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(name="Great Axe",
                         description="A large and heavy axe",
                         value=20,
                         damage = randint(1, 8))

class CuttingKnife(Weapon):
    def __init__(self):
        super().__init__(name="Cutting Riposte",
                     description="A very sharp knife",
                     value=15,
                     damage = randint(1, 8))

class LongSpear(Weapon):
    def __init__(self):
        super().__init__(name="Long Spear",
                     description="A large and easily thrown spear",
                     value=30,
                     damage = randint(1, 12))
class WhirlingSword(Weapon):
    def __init__(self):
        super().__init__(name="Whirling Sword",
                     description="A shining blade",
                     value=30,
                     damage = randint(1, 12))
