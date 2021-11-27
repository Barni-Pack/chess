import pygame

from config import tile_size, screen, board_row_tiles, board_window_offset
from session_data import dead_pieces
from os import path
import svg

from mappings.board import board

from mappings.tile_map import tile_map

from .tile_class import Tile

from session_data import switch_turn

from typing import List


def index_2d(list_2d: List[List[str]], key: str) -> tuple:
    # Returns (x, y) position of piece on the board
    for x, column in enumerate(list_2d):
        if key in column:
            y = column.index(key)
            return (x+1, y+1)
    raise KeyError('Piece was not found.')
    

class Piece:
    def __init__(self, name, killable=False):
        self.selected = False

        self.name = name
        self.team = name[0]
        self.type = name.split('_')[1]
        self.killable = killable

        self.tile = None
        self.moves = []
        self.enemies = []

        self.set_position()

        if self.team == 'w':
            self.image = f'w_{self.type}.svg'
        else:
            self.image = f'b_{self.type}.svg'

        self.clear_selection()

    def set_position(self):
        self.x, self.y = index_2d(board, self.name)
        self.tile = tile_map[self.x][self.y]

    def set_pieces_map(self, pieces_map):
        self.pieces_map = pieces_map

    def get_piece(self, x, y):
        try:
            return self.pieces_map[board[x][y]]
        except KeyError:
            print('Piece was not found in pieces_map (probably disabled)')
            pass

    def select(self):
        self.selected = True
        self.check_selection()

    def deselect(self):
        self.selected = False
        self.check_selection()

    def check_selection(self):
        if self.selected:
            self.draw_selection()
            self.draw_moves()
            self.draw_enemies()

        else:
            self.clear_selection()
            self.clear_moves()
            self.clear_enemies()

        # Update display
        pygame.display.flip()

    def draw_selection(self):
        self.tile.draw_green()
        self.draw_piece()

    def draw_moves(self):
        for tile in self.moves:
            tile.draw_green_dot()

    def draw_enemies(self):
        for piece in self.enemies:
            piece.tile.draw_green_triangle()
            piece.draw_piece()

    def clear_selection(self):
        self.tile.draw_default()
        self.draw_piece()

    def clear_moves(self):
        for tile in self.moves:
            tile.draw_default()

    def clear_enemies(self):
        for piece in self.enemies:
            piece.clear_selection()

    def draw_piece(self):
        pawn_image = svg.load_svg(path.join('svg', self.image))

        scale = 0.95
        pawn_image = pygame.transform.smoothscale(pawn_image, (int(tile_size * scale),
                                                               int(tile_size * scale)))

        image_width, image_height = pawn_image.get_width(), pawn_image.get_height()

        x_pixels = (self.x - 1) * tile_size
        y_pixels = (board_row_tiles - self.y) * tile_size + board_window_offset

        screen.blit(pawn_image, (x_pixels + (tile_size - image_width) / 2,
                                  y_pixels + (tile_size - image_height) / 2))

    def move2tile(self, tile: Tile):
        # Deselect self
        self.deselect()

        # Return if move was not possible
        if tile not in self.moves:
            # print('This move is not possible')
            return

        self.swap_with_tile(tile)

    def kill(self, piece):
        # Deselect self
        self.deselect()

        if piece not in self.enemies:
            # print('Selected enemy piece is not killable')
            return

        global dead_pieces
        dead_pieces.append(piece)

        self.swap_with_tile(piece.tile)

    def swap_with_tile(self, tile):
        # Get coordinates
        self_x, self_y = index_2d(board, self.name)
        field_x, field_y = tile.coordinates

        # Swap two values in board
        self_map = board[self_x][self_y]

        board[field_x][field_y] = self_map
        board[self_x][self_y] = None

        # Draw new piece
        self.set_position()
        self.clear_selection()

        # Redraw old tile
        tile_map[self_x][self_y].draw()

        # Update available moves and enemies
        self.update_all_pieces_data()

        # Update display
        pygame.display.flip()
        
        # Switch player
        switch_turn()

    def update_all_pieces_data(self):
        for piece_name in sum(board, []):
            try:
                self.pieces_map[piece_name].get_moves() if piece_name else None
            except KeyError:
                # Piece was not found in pieces_map (probably disabled)
                pass

    @staticmethod
    def check_limits(x, y):
        # Check that position is in board limits
        limits = range(1, board_row_tiles + 1)

        if x not in limits or y not in limits:
            return False
        else:
            return True

    def init_moves_and_enemies(self, init=True):
        if init:
            # Init moves and enemies list
            self.moves = []
            self.enemies = []

    def get_moves_sequence(self, x_increment, y_increment, repeat=True):
        x = self.x
        y = self.y

        while True:

            x += x_increment
            y += y_increment

            # Check that position is in board limits
            if not self.check_limits(x, y):
                break

            try:
                # Add empty to moves
                if not board[x][y]:
                    self.moves.append(tile_map[x][y])

                else:
                    # Add enemy to enemies and break
                    piece = self.get_piece(x, y)
                    if not piece:
                        break

                    if piece.team != self.team:
                        self.enemies.append(piece)

                    break

                if not repeat:
                    break

            except IndexError:
                break


class Pawn(Piece):
    def get_moves(self):
        self.init_moves_and_enemies()

        # Select direction based on piece team
        y = 1 if self.team == 'w' else -1

        # Left and right exnemies
        for x in [-1, 1]:
            try:
                if board[self.x + x][self.y + y]:
                    self.get_moves_sequence(x, y, repeat=False)
            except IndexError:
                continue

        # Single step
        self.get_moves_sequence(0, y, repeat=False)
        # Double step if single available
        if self.moves:
            if (self.y == 2 and y == 1) or (self.y == board_row_tiles-1 and y == -1):
                self.get_moves_sequence(0, 2 * y, repeat=False)

        # Front enemy is not killable
        for piece in self.enemies:
            if piece.x == self.x:
                self.enemies.remove(piece)


class Rook(Piece):
    def get_moves(self, init=True):
        self.init_moves_and_enemies(init)

        # Top
        self.get_moves_sequence(0, 1)

        # Right
        self.get_moves_sequence(1, 0)

        # Bottom
        self.get_moves_sequence(0, -1)

        # Left
        self.get_moves_sequence(-1, 0)


class Knight(Piece):
    def get_moves(self):
        self.init_moves_and_enemies()

        for x, y in ((1, 2), (1, -2), (-1, 2), (-1, -2)):
            self.get_moves_sequence(x, y, repeat=False)
            self.get_moves_sequence(y, x, repeat=False)


class Bishop(Piece):
    def get_moves(self):
        self.init_moves_and_enemies()

        # Diagonals

        # Top right
        self.get_moves_sequence(1, 1)

        # Bottom right
        self.get_moves_sequence(1, -1)

        # Bottom left
        self.get_moves_sequence(-1, -1)

        # Top left
        self.get_moves_sequence(-1, 1)


class Queen(Piece):
    def get_moves(self, repeat=True):
        self.init_moves_and_enemies()

        # Check in 1 tile radius
        for x in range(-1, 2):
            for y in range(-1, 2):
                # Skip if self position
                if x == 0 and y == 0:
                    continue

                self.get_moves_sequence(x, y, repeat)


class King(Queen):
    def get_moves(self):
        super().get_moves(False)
