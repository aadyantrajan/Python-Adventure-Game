import random
from enum import Enum
from inventory import *
Weapon = Enum('Weapon', ['Iron', 'Bronze', 'Copper', 'Silver', 'Wood', 'Gold', 'Platinum', 'DragonBone'])
Shield = Enum('Shield', ['Iron', 'Bronze', 'Copper', 'Silver', 'Wood', 'Gold', 'Platinum', 'DragonBone'])

class Character(object):
    def __init__(self, name='', max_health=200, damage_modifier=1):
        self.name = name
        self.max_health = max_health
        self.inventory = Inventory()
        self.damage_modifier = damage_modifier
        self.health = max_health

    def attack(self, enemy):
        damage = 0 * self.damage_modifier
        if self.inventory.getWeapon() is Weapon.Iron.name:
            damage = 15*self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Bronze.name:
            damage = 18*self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Copper.name:
            damage = 10*self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Silver.name:
            damage = 20*self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Wood.name:
            damage = 8*self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Gold.name:
            damage = 24*self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Platinum.name:
            damage = 40*self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.DragonBone.name:
            damage = 100*self.damage_modifier
        enemy.defend(damage)

    def defend(self, damage):
        if self.inventory.getShield() is Shield.Iron.name:
            damage = damage/1.4
        elif self.inventory.getShield() is Shield.Bronze.name:
            damage = damage/1.5
        elif self.inventory.getShield() is Shield.Copper.name:
            damage = damage/1.2
        elif self.inventory.getShield() is Shield.Silver.name:
            damage = damage/1.6
        elif self.inventory.getShield() is Shield.Wood.name:
            damage = damage/1.1
        elif self.inventory.getShield() is Shield.Gold.name:
            damage = damage/1.7
        elif self.inventory.getShield() is Shield.Platinum.name:
            damage = damage/2
        elif self.inventory.getShield() is Shield.DragonBone.name:
            damage = damage/3
        self.health = self.health - int(damage)

    def heal(self, heal_rate):
        self.health += heal_rate
        if self.health > self.max_health:
            self.health = self.max_health

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

    def get_shield_and_sword(self):
        print(f'Your shield: {self.inventory.getShield()}')
        print(f'Your sword: {self.inventory.getWeapon()}')

class Tank(Character):
    def __init__(self, name='', max_health=500, damage_modifier=3):
        self.name = name
        self.max_health = max_health
        self.inventory = Inventory()
        self.damage_modifier = damage_modifier
        self.health = max_health

class Healer(Character):
    def __init__(self, name='', max_health=150, damage_modifier=0.7):
        self.heal_counter = 0
        self.name = name
        self.max_health = max_health
        self.inventory = Inventory()
        self.damage_modifier = damage_modifier
        self.health = max_health

    def attack(self, enemy):
        self.heal_counter += 1
        damage = 0 * self.damage_modifier
        if self.inventory.getWeapon() is Weapon.Iron.name:
            damage = 15 * self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Bronze.name:
            damage = 18 * self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Copper.name:
            damage = 10 * self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Silver.name:
            damage = 20 * self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Wood.name:
            damage = 8 * self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Gold.name:
            damage = 24 * self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.Platinum.name:
            damage = 40 * self.damage_modifier
        elif self.inventory.getWeapon() is Weapon.DragonBone.name:
            damage = 100 * self.damage_modifier
        enemy.defend(damage)

    def defend(self, damage):
        if self.inventory.getShield() is Shield.Iron.name:
            damage = damage / 1.4
        elif self.inventory.getShield() is Shield.Bronze.name:
            damage = damage / 1.5
        elif self.inventory.getShield() is Shield.Copper.name:
            damage = damage / 1.2
        elif self.inventory.getShield() is Shield.Silver.name:
            damage = damage / 1.6
        elif self.inventory.getShield() is Shield.Wood.name:
            damage = damage / 1.1
        elif self.inventory.getShield() is Shield.Gold.name:
            damage = damage / 1.7
        elif self.inventory.getShield() is Shield.Platinum.name:
            damage = damage / 2
        elif self.inventory.getShield() is Shield.DragonBone.name:
            damage = damage / 3
        self.health = self.health - int(damage)
        if self.heal_counter == 4:
            self.heal(int(self.health*0.5))
            self.heal_counter = 0

    def move(self, direction):
        self.heal_counter += 1
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
        if self.heal_counter == 4:
            self.heal(int(self.health*0.5))
            self.heal_counter = 0
        return x, y

class Enemy(Character):
    def attack(self, enemy):
        damage = 5 * self.damage_modifier
        enemy.defend(damage)

    def defend(self, damage):
        self.health = self.health - int(damage)