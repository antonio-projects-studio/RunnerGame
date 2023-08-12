from random import choices, randrange
from npc import *


class NpcControl:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_positions = {}
        self.add_npc(NPC(game))
        if game.level > 1:
            self.add_npc(NPC(game, (11.5, 7.5)))
        if game.level > 2:
            self.add_npc(NPC(game, (6.5, 7.5)))
        if game.level > 3:
            self.add_npc(NPC(game, (9.5, 1.5)))
        if game.level > 4:
            self.add_npc(NPC(game, (13, 3)))


    def update(self):
        [npc.update() for npc in self.npc_list]
        self.npc_positions = {npc.map_pos for npc in self.npc_list}

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
        
