import random
class Scene(object):
    def __init__(self, width, height, enemy_count):
        self.width = width
        self.height = height
        self.enemies = {}
        for enemy in range(enemy_count):
            self.enemies[enemy] = (random.randint(0, self.width), random.randint(0, self.height))
        self.player = (0,0)

    def remove_enemy(self):
        for enemy in self.enemies:
            if self.enemies[enemy] == self.player:
                del self.enemies[enemy]

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
        if newy > self.height:
            newy = self.height
        self.player = (newx, newy)
        print(f'You moved from ({x}, {y}) to ({newx}, {newy})')