from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_x, cos_x = math.sin(self.angle), math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_cos, speed_sin = speed * cos_x, speed * sin_x

        #pega teclas apertadas WASD e calcula o movimento de direcao baseado em cosseno e seno
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += -speed_cos
            dy += speed_sin
        if keys[pg.K_d]:
            dx += speed_cos
            dy += -speed_sin

        #atualiza movimento do personagem
        self.check_wall_collision(dx, dy)

        #character angle
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    #check if coordinates hit the wall
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    #check coordinates of the walls and allow movement if there's no wall
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x+dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y+dy)):
            self.y += dy

#VIDEO TIME = 7:38

    def draw_player(self):
        #draw direction of movement
        pg.draw.line(self.game.screen,'yellow', (self.x*100, self.y*100),
                     (self.x*100 + WIDTH*math.cos(self.angle), self.y*100 + WIDTH*math.sin(self.angle)), 2)

        #draw player
        pg.draw.circle(self.game.screen,'green', (self.x*100, self.y*100),15)


    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)