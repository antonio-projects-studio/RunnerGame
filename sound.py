import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.win = pg.mixer.Sound('sounds/SUIII.mp3')
        self.win.set_volume(2)
        self.lose = pg.mixer.Sound('sounds/lox.mp3')
        self.lose.set_volume(2)
        # self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.music.load('sounds/theme.mp3')
        pg.mixer.music.set_volume(0.4)

