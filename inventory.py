import random
class Inventory(object):
    def __init__(self):
        potion_type = random.randint(0, 10)
        self.shield = "Copper"
        self.potion = ""

        if potion_type <= 2:
            self.potion = "Healing"
        elif potion_type == 3:
            self.potion = "DamageBoost"

        self.weapon = "Copper"
        self.coins = 30

    def getShield(self):
        return self.shield

    def setShield(self, newShield):
        self.shield = newShield

    def getPotion(self):
        return self.potion

    def setPotion(self, newPotion):
        self.potion = newPotion

    def getWeapon(self):
        return self.weapon

    def setWeapon(self, newWeapon):
        self.weapon = newWeapon

    def getCoins(self):
        return self.coins

    def addCoins(self, coins):
        self.coins += coins

    def spendCoins(self, purchase):
        if purchase <= self.coins:
            self.coins -= purchase
        else:
            print("Not enough coins")



