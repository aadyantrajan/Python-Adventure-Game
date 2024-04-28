import random
class Scene(object):
    def __init__(self, width, height, enemy_count):
        self.width = width
        self.height = height
        self.enemies = {}
        true_enemy_count = min(enemy_count, width*height)
        for enemy in range(true_enemy_count):
            location = (random.randint(0, self.width), random.randint(0, self.height))
            while location in self.enemies.values():
                location = (random.randint(0, self.width), random.randint(0, self.height))
            self.enemies[enemy] = location
        self.player = (0,0)

    def remove_enemy(self):
        removed_enemy = -1
        for enemy in self.enemies:
            if self.enemies[enemy] == self.player:
                removed_enemy = enemy
        if removed_enemy > -1:
            self.enemies.pop(removed_enemy)

    def enemy_exists(self):
        enemy_exists = False
        for enemy in self.enemies:
            if self.enemies[enemy] == self.player:
                enemy_exists = True
        return enemy_exists

    def get_enemy_index(self):
        index = -1
        for enemy in self.enemies:
            if self.enemies[enemy] == self.player:
                index = enemy
        return index

    def update_player_loc(self, direction):
        x, y = self.player
        x1, y1 = direction
        newx = x + x1
        newy = y + y1
        if newx > self.width:
            newx = self.width
            print('Out of bounds')
        elif newx < 0:
            newx = 0
            print("Out of bounds")
        if newy > self.height:
            newy = self.height
            print('Out of bounds')
        elif newy < 0:
            newy = 0
            print("Out of bounds")
        self.player = (newx, newy)
        print(f'You moved from ({x}, {y}) to ({newx}, {newy})')