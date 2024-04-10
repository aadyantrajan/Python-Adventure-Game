import random
from enum import Enum
from inventory import *
Weapon = Enum('Weapon', ['Iron', 'Bronze', 'Copper', 'Silver', 'Wood', 'Gold', 'Platinum', 'DragonBone'])
Shield = Enum('Shield', ['Iron', 'Bronze', 'Copper', 'Silver', 'Wood', 'Gold', 'Platinum', 'DragonBone'])
Potion = Enum('Potion', ['Healing', 'DamageBoost'])
class Character(object):
    def __init__(self, name='', max_health=200, level=1, damage_modifier=1.0):
        self.name = name
        self.max_health = max_health
        self.inventory = Inventory()
        self.damage_modifier = damage_modifier
        self.level = level
        self.health = max_health

    def attack(self, enemy):
        damage = 5*self.damage_modifier
        if self.inventory.getWeapon() == Weapon.Iron.name:
            damage = 15*self.damage_modifier
        elif self.inventory.getWeapon() == Weapon.Bronze.name:
            damage = 18*self.damage_modifier
        elif self.inventory.getWeapon() == Weapon.Copper.name:
            damage = 10*self.damage_modifier
        elif self.inventory.getWeapon() == Weapon.Silver.name:
            damage = 20*self.damage_modifier
        elif self.inventory.getWeapon() == Weapon.Wood.name:
            damage = 8*self.damage_modifier
        elif self.inventory.getWeapon() == Weapon.Gold.name:
            damage = 24*self.damage_modifier
        elif self.inventory.getWeapon() == Weapon.Platinum.name:
            damage = 40*self.damage_modifier
        elif self.inventory.getWeapon() == Weapon.DragonBone.name:
            damage = 100*self.damage_modifier
        enemy.defend(damage)

    def defend(self, damage):
        if self.inventory.getShield() == Shield.Iron.name:
            damage = damage/1.4
        elif self.inventory.getShield() == Shield.Bronze.name:
            damage = damage/1.5
        elif self.inventory.getShield() == Shield.Copper.name:
            damage = damage/1.2
        elif self.inventory.getShield() == Shield.Silver.name:
            damage = damage/1.6
        elif self.inventory.getShield() == Shield.Wood.name:
            damage = damage/1.1
        elif self.inventory.getShield() == Shield.Gold.name:
            damage = damage/1.7
        elif self.inventory.getShield() == Shield.Platinum.name:
            damage = damage/2
        elif self.inventory.getShield() == Shield.DragonBone.name:
            damage = damage/3
        self.health = self.health - damage

    def heal(self, heal_rate):
        self.health += heal_rate

    def move(self, direction):
        x = 0
        y = 0
        if direction == 'forward':
            y = 1
        elif direction == 'backward':
            y = -1
        elif direction == 'left':
            x = -1
        elif direction == 'right':
            x = 1
        return x, y



