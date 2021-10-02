import pygame

from config import tile_size, surface, board_size
from os import path
import svg

from mappings.board import board
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
        self.coordinates = index_2d(board, self.name)
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
        self.show_moves()

    def select2die(self):
        self.tile.select2die()
        self.draw()

    def move2field(self, tile: Tile):
        # Deselects tiles if move was not possible
        if not tile.selected:
            self.select()
            print('nigga')
            return

        # Clear current selection
        self.select()

        self_x, self_y = index_2d(board, self.name)
        field_x, field_y = tile.coordinates

        # Swap two values in grid map
        self_map = board[self_x][self_y]

        new_map = board[field_x][field_y]

        board[field_x][field_y] = self_map
        board[self_x][self_y] = new_map

        # Draw new piece
        self.set_coordinates()
        self.draw()

        # Redraw old tile
        tile_map[self_x][self_y].draw()


class Pawn(Piece):
    def show_moves(self):

        # White team
        if self.team == 'w':

            # Single step
            if self.y in [2, 3, 4, 5, 6, 7] and not board[self.x][self.y + 1]:
                tile_map[self.x][self.y + 1].select()

                # Double step
                if self.y == 2 and not board[self.x][self.y + 2]:
                    tile_map[self.x][self.y + 2].select()

        # Black team
        if self.team == 'b':

            # Single step
            if self.y in [7, 6, 5, 4, 3, 2] and not board[self.x][self.y - 1]:
                tile_map[self.x][self.y - 1].select()

                # Double step
                if self.y == 7 and not board[self.x][self.y - 2]:
                    tile_map[self.x][self.y - 2].select()

    def show_edible(self, pieces_map):
        left_enemy_x = None
        right_enemy_x = None

        # White team
        if self.team == 'w':
            if self.x > 1:
                left_enemy_x = self.x - 1
            if self.x < 8:
                right_enemy_x = self.x + 1

            if self.y < 8:
                if board[left_enemy_x][self.y + 1] in pieces_map:
                    left_enemy = pieces_map[board[left_enemy_x][self.y + 1]]

                    if left_enemy.team != self.team:
                        left_enemy.select2die()

                if board[right_enemy_x][self.y + 1] in pieces_map:
                    right_enemy = pieces_map[board[right_enemy_x][self.y + 1]]

                    if right_enemy.team != self.team:
                        right_enemy.select2die()

        # Black team
        if self.team == 'b':
            if self.x > 1:
                left_enemy_x = self.x - 1
            if self.x < 8:
                right_enemy_x = self.x + 1

            if self.y > 1:
                if board[left_enemy_x][self.y - 1] in pieces_map:
                    left_enemy = pieces_map[board[left_enemy_x][self.y - 1]]

                    if left_enemy.team != self.team:
                        left_enemy.select2die()

                if board[right_enemy_x][self.y - 1] in pieces_map:
                    right_enemy = pieces_map[board[right_enemy_x][self.y - 1]]

                    if right_enemy.team != self.team:
                        right_enemy.select2die()


class Rook(Piece):
    def show_moves(self):
        moves = []

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
        x, y = self.x, self.y
        
        # bottom left
        try:
            if not board[x - 1][y - 1]:
                tile_map[x - 1][y - 1].select()
        except IndexError:
            return None
        
        # middle left
        try:
            if not board[x - 1][y]:
                tile_map[x - 1][y].select()
        except IndexError:
            return None
        
        # top left
        try:
            if not board[x - 1][y + 1]:
                tile_map[x - 1][y + 1].select()
        except IndexError:
            return None
        
        # top middle
        try:
            if not board[x][y + 1]:
                tile_map[x][y + 1].select()
        except IndexError:
            return None
        
        # top right
        try:
            if not board[x + 1][y + 1]:
                tile_map[x + 1][y + 1].select()
        except IndexError:
            return None
        
        # middle right
        try:
            if not board[x + 1][y]:
                tile_map[x + 1][y].select()
        except IndexError:
            return None
        
        # bottom right
        try:
            if not board[x + 1][y - 1]:
                tile_map[x + 1][y - 1].select()
        except IndexError:
            return None
        
        # bottom middle
        try:
            if not board[x][y - 1]:
                tile_map[x][y - 1].select()
        except IndexError:
            return None
    
    def show_edible(self, pieces_map):
        return