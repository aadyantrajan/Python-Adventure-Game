import random
from enum import Enum
Weapon = Enum('Weapon', ['Iron', 'Bronze', 'Copper', 'Silver', 'Wood', 'Gold', 'Platinum', 'DragonBone'])
Shield = Enum('Shield', ['Iron', 'Bronze', 'Copper', 'Silver', 'Wood', 'Gold', 'Platinum', 'DragonBone'])
class Inventory(object):
    def __init__(self):
        self.shield = random.choice(list(Shield)).name
        self.weapon = random.choice(list(Weapon)).name

    def getShield(self):
        return self.shield

    def setShield(self, newShield):
        self.shield = newShield

    def getWeapon(self):
        return self.weapon

    def setWeapon(self, newWeapon):
        self.weapon = newWeapon