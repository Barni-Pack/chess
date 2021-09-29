from config import board_size, tile_size, white_tile_color, black_tile_color, selected_white_tile_color, selected_black_tile_color
import pygame
import svg
from config import surface
from os import path
# from grid_map import MyList


class MyList(list):
    def __init__(self, *args, **kwargs):
        super(MyList, self).__init__(args[0])

    def __getitem__(self, n):
        return super(MyList, self).__getitem__(n-1)


tile_map = [
    ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
    ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'],
    ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'],
    ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8'],
    ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8'],
    ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'],
    ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'],
    ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
]

tile_letter = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}


class Tile:
    """Tile class. Draw method"""

    def __init__(self, name):
        self.name = name

        self.x = tile_letter[name[0]]
        self.y = int(name[1])

        self.coordinates = self.x, self.y
        self.y_pixels = (board_size - self.y) * tile_size
        self.x_pixels = (self.x - 1) * tile_size
        self.size = tile_size
        self.type = 'white' if (self.x + self.y) % 2 == 0 else 'black'
        self.selected = False
        self.set_color()
        self.draw()

    def set_color(self):
        if self.type == 'white':
            if self.selected:
                self.color = selected_white_tile_color
            else:
                self.color = white_tile_color
        else:
            if self.selected:
                self.color = selected_black_tile_color
            else:
                self.color = black_tile_color

    def draw(self):
        pygame.draw.rect(surface,
                         self.color,
                         pygame.Rect(self.x_pixels, self.y_pixels, self.size, self.size))

    def select(self):
        self.selected = not self.selected
        self.set_color()
        self.draw()
        pygame.display.flip()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name + '|' + str(self.x) + ':' + str(self.y)


for x, row in enumerate(tile_map):
    for y, column in enumerate(row):
        tile_map[x][y] = Tile(tile_map[x][y])


tile_map = MyList([MyList(row) for row in tile_map])
print(tile_map)