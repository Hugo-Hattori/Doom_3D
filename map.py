import pygame as pg

_ = False
#layout do mapa sendo 1 as paredes e _ os espacos em que o player pode andar
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, cell in enumerate(row):
                if cell:
                    self.world_map[(i, j)] = cell

    def draw(self):
        [pg.draw.rect(self.game.screen,'darkgray', (pos[0]*100, pos[1]*100, 100, 100),2)
         for pos in self.world_map]