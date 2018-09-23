class Magic():
    """The base class for items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    

class CureWounds(Magic):

class MagicMissile(Magic):
