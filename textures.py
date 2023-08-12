import pygame as pg
from settings import *

class Textures:
    def __init__(self, game):
        self.screen = game.screen
        self.lose_game_image = self.get_texture('textures/wasted.png', RES)
        self.win_game_image = self.get_texture('textures/sui.jpeg', RES)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def lose_game(self):
        self.screen.blit(self.lose_game_image, (0, 0))

    def win_game(self):
        self.screen.blit(self.win_game_image, (0, 0))



