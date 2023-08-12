import pygame as pg
from random import randrange, choices
from settings import *


class Finish:
    def __init__(self, game):
        self.game = game
        self.player = game.player
        self.npc_list = game.npc_control.npc_list
        self.p_x, self.p_y = game.player.x, game.player.y
        self.x, self.y = START_POS
        self.change_finish_delay = DELAY
        self.trigger = False
        self.time_prev = pg.time.get_ticks()

    def update(self):
        self.p_x, self.p_y = self.player.x, self.player.y
        self.change_finish_pos()

    def change_finish_pos(self):
        time_now = pg.time.get_ticks()
        for i in range(len(self.npc_list)):
            if not self.npc_list[i].player_search:
                self.time_prev = time_now
                return
        if not self.trigger:
            npc = choices(self.npc_list)[0]
            self.x, self.y = npc.x, npc.y
            self.time_prev = time_now
            self.trigger = True
            return

        if time_now - self.time_prev > self.change_finish_delay:
            self.time_prev = time_now
            self.rand_change()

    def rand_change(self):
        pos = x, y = randrange(
            self.game.map.cols), randrange(self.game.map.rows)
        while pos in self.game.map.world_map:
            pos = x, y = randrange(
                self.game.map.cols), randrange(self.game.map.rows)
        self.x, self.y = pos
        self.x += 0.5
        self.y += 0.5

    def draw(self):
        x_p = self.player.x
        y_p = self.player.y
        len = ((x_p - self.x) ** 2 + (y_p - self.y) ** 2)
        if len > WIN_LEN:
            pg.draw.circle(self.game.screen, "yellow",
                           (self.x * 100, self.y * 100), 15)
            pg.draw.circle(self.game.screen, "yellow",
                           (self.x * 100, self.y * 100), 25, 2)
        else:
            self.player.status_game = 2
            
