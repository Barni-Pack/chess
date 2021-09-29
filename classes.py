import pygame

from config import tile_size, surface, board_size
from os import path
import svg
from grid_map import grid_map

from tiles import tile_map, Tile


def index_2d(list_2d, key):
    for x, column in enumerate(list_2d):
        if key in column:
            y = column.index(key)
            return x+1, y+1


# print(index_2d(grid_map, 'w_pawn_1'))


class Piece:
    def __init__(self, name, killable=False):
        self.name = name
        self.team = name[0]
        self.type = name.split('_')[1]
        self.killable = killable

        self.coordinates = index_2d(grid_map, name)
        self.set_coordinates(*self.coordinates)

        if self.team == 'w':
            self.image = f'w_{self.type}.svg'
        else:
            self.image = f'b_{self.type}.svg'

        self.draw()

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = self.x, self.y
        self.tile = tile_map[self.x][self.y]

    def draw(self):
        pawn_image = svg.load_svg(path.join('svg', self.image))

        scale = 0.75
        pawn_image = pygame.transform.smoothscale(pawn_image, (int(tile_size * scale),
                                                               int(tile_size * scale)))

        image_width, image_height = pawn_image.get_width(), pawn_image.get_height()

        x_pixels = (self.x - 1) * tile_size
        y_pixels = (board_size - self.y) * tile_size

        surface.blit(pawn_image, (x_pixels + (tile_size - image_width) / 2,
                                  y_pixels + (tile_size - image_height) / 2))
        pygame.display.flip()

    def select(self):
        self.tile.select()
        self.draw()

    def move2field(self, field_index: tuple):
        self_x, self_y = index_2d(grid_map, self.name)
        field_x, field_y = field_index

        # print(self_x, self_y)

        self_map = grid_map[self_y][self_x]
        new_map = grid_map[field_y][field_x]

        # print(self_map, new_map)

        new_map, self_map = self_map, None

        # new_x, new_y = index_2d(grid_map, new_map)
        # pieces_map[new_map].select()

        # print(self_map, new_map)

        # self.set_coordinates(*index_2d(grid_map, new_map))
        # print(self.coordinates)
        # self.draw()


class Pawn(Piece):
    def show_moves(self):
        return


class Rook(Piece):
    def show_moves(self):
        return


class Knight(Piece):
    def show_moves(self):
        return


class Bishop(Piece):
    def show_moves(self):
        return


class Queen(Piece):
    def show_moves(self):
        return


class King(Piece):
    def show_moves(self):
        return
