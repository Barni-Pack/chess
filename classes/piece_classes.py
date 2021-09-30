import pygame

from config import tile_size, surface, board_size
from os import path
import svg

from mappings.grid_map import grid_map
from mappings.tile_map import tile_map

from .tile_class import Tile



def index_2d(list_2d, key):
    for x, column in enumerate(list_2d):
        if key in column:
            y = column.index(key)
            return x+1, y+1


class Piece:
    def __init__(self, name, killable=False):
        self.name = name
        self.team = name[0]
        self.type = name.split('_')[1]
        self.killable = killable

        self.set_coordinates()

        if self.team == 'w':
            self.image = f'w_{self.type}.svg'
        else:
            self.image = f'b_{self.type}.svg'

        self.draw()

    def set_coordinates(self):
        self.coordinates = index_2d(grid_map, self.name)
        self.x, self.y = self.coordinates
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

    def move2field(self, tile: Tile):
        self_x, self_y = index_2d(grid_map, self.name)
        field_x, field_y = tile.coordinates

        # Swap two values in grid map
        self_map = grid_map[self_x][self_y]

        new_map = grid_map[field_x][field_y]

        grid_map[field_x][field_y] = self_map
        grid_map[self_x][self_y] = new_map

        # Draw new piece
        self.set_coordinates()
        self.draw()

        # Redraw old tile
        tile_map[self_x][self_y].select()


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
