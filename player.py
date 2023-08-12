import math
import sys
import pygame as pg
from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.status_game = 0

    def check_game(self):
        match self.status_game:
            case 1:
                self.game.textures.lose_game()
                self.game.sounds.lose.play()
                pg.display.flip()
                pg.time.delay(1500)
                if self.game.level != 1:
                    self.game.level -= 1
                self.game.new_game()
            case 2:
                self.game.textures.win_game()
                self.game.sounds.win.play()
                pg.display.flip()
                pg.time.delay(1500)
                if self.game.level != 5:
                    self.game.level += 1
                    self.game.new_game()
                else:
                    print("спустя стольк времени, ты все же прошел...\nтебе надо знать только одно...\ndanya_lox")
                    pg.quit()
                    sys.exit()

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        num_key_pressed = -1
        if keys[pg.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        # if keys[pg.K_s]:
        #     num_key_pressed += 1
        #     dx += -speed_cos
        #     dy += -speed_sin
        if keys[pg.K_a]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_d]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time

        self.angle %= math.tau

        self.check_wall_collision(dx, dy)

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        # pg.draw.line(self.game.screen, 'blue', (self.x * 100, self.y * 100),
        #              (self.x * 100 + WIDHT * math.cos(self.angle),
        #              self.y * 100 + WIDHT * math.sin(self.angle)), 2)
        pg.draw.line(self.game.screen, 'green', (self.x * 100 + 14.5 * math.sin(self.angle), self.y * 100 - 14.5 * math.cos(self.angle)),
                     (self.x * 100 + 35 * math.cos(self.angle),
                     self.y * 100 + 35 * math.sin(self.angle)), 2)
        pg.draw.line(self.game.screen, 'green', (self.x * 100 - 14.5 * math.sin(self.angle), self.y * 100 + 14.5 * math.cos(self.angle)),
                     (self.x * 100 + 35 * math.cos(self.angle),
                     self.y * 100 + 35 * math.sin(self.angle)), 2)

        pg.draw.circle(self.game.screen, 'green',
                       (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()
        self.check_game()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

