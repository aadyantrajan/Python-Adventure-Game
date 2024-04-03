import random
class Scene(object):
    def __init__(self, width, height, npc_count, player_count):
        self.width = width
        self.height = height
        self.npcs = {}
        for npc in range(npc_count):
            npcs[npc] = (random(0, self.width), random(0, self.height))
        self.players = {}
        for player in range(player_count):
            players[player] = (random(0, self.width), random(0, self.height))

    def update_player_loc(player, direction):
        x, y = players[player]
        newx, newy = direction
        players[player] = (x + newx, y + newy)
