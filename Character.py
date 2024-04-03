class Character(object):
    def __init__(self,name='',max_health=200,inventory=30,level=1,damage_modifier=1.0):
        self.name = name
        self.max_health = max_health
        self.inventory = inventory
        self.damage_modifier = damage_modifier
        self.level = level
        self.health = max_health
