import random
class Character(object):
    def __init__(self, name='', max_health=200, inventory=30, level=1, damage_modifier=1.0):
        self.name = name
        self.max_health = max_health
        self.inventory = inventory
        self.damage_modifier = damage_modifier
        self.level = level
        self.health = max_health

    def attack(self, enemy):
        damage = 30*self.damage_modifier
        enemy.defend(damage)

    def defend(self, damage):
        block = random.randint(0,10)
        if block == 5:
            damage = 0
        self.health = self.health-damage

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



