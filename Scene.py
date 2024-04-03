import random
class Scene(object):
    def __init__(self, width, height, npc_count, player_count):
        self.width = width
        self.height = height
        self.npcs = {}
        for npc in range(npc_count):
            self.npcs[npc] = (random.randint(0, self.width), random.randint(0, self.height))
        self.players = {}
        for player in range(player_count):
            self.players[player] = (random.randint(0, self.width), random.randint(0, self.height))

    def update_player_loc(self, player, direction):
        x, y = self.players[player]
        newx, newy = direction
        self.players[player] = (x + newx, y + newy)

class Tavern(Scene):
    def __init__(self, width, height, npc_count, player_count):
        self.width = width
        self.height = height
        self.npcs = {}
        for npc in range(npc_count):
            self.npcs[npc] = (random.randint(0, self.width), random.randint(0, self.height))
        self.npcs["bartender"] = (int(self.width / 2), int(self.height / 2))
        self.players = {}
        for player in range(player_count):
            self.players[player] = (random.randint(0, self.width), random.randint(0, self.height))

