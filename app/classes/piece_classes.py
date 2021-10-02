import pygame

from config import tile_size, surface, board_size
from game_data import dead_pieces
from os import path
import svg

from mappings.board import board
# from mappings.pieces_map import pieces_map

from mappings.tile_map import tile_map

from .tile_class import Tile


def index_2d(list_2d, key):
    for x, column in enumerate(list_2d):
        if key in column:
            y = column.index(key)
            return x+1, y+1


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
        return self.pieces_map[board[x][y]]

    def select(self):
        print(self.moves)
        print(self.enemies)
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
            tile.draw_green()

    def draw_enemies(self):
        for piece in self.enemies:
            piece.tile.draw_red()
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

        scale = 0.75
        pawn_image = pygame.transform.smoothscale(pawn_image, (int(tile_size * scale),
                                                               int(tile_size * scale)))

        image_width, image_height = pawn_image.get_width(), pawn_image.get_height()

        x_pixels = (self.x - 1) * tile_size
        y_pixels = (board_size - self.y) * tile_size

        surface.blit(pawn_image, (x_pixels + (tile_size - image_width) / 2,
                                  y_pixels + (tile_size - image_height) / 2))
        # pygame.display.flip()

    def move2tile(self, tile: Tile):
        # Deselect self
        self.deselect()

        # Return if move was not possible
        if tile not in self.moves:
            return

        self.swap_with_tile(tile)

    def kill(self, piece):
        # Deselect self
        self.deselect()
        
        if piece not in self.enemies:
            print('huh?')
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
        # self.update_data()
        
        # Update display
        pygame.display.flip()
        
    def update_data(self):
        self.get_moves()
        self.get_enemies()
        
    def get_moves(self):
        return
    
    def get_enemies(self):
        return


class Pawn(Piece):
    def get_moves(self):
        # Init moves list
        self.moves = []

        # White team
        if self.team == 'w':

            # Single step
            if self.y in [2, 3, 4, 5, 6, 7] and not board[self.x][self.y + 1]:
                self.moves.append(tile_map[self.x][self.y + 1])

                # Double step
                if self.y == 2 and not board[self.x][self.y + 2]:
                    self.moves.append(tile_map[self.x][self.y + 2])

        # Black team
        if self.team == 'b':

            # Single step
            if self.y in [7, 6, 5, 4, 3, 2] and not board[self.x][self.y - 1]:
                self.moves.append(tile_map[self.x][self.y - 1])

                # Double step
                if self.y == 7 and not board[self.x][self.y - 2]:
                    self.moves.append(tile_map[self.x][self.y - 2])

    def get_enemies(self):
        # Init enemies list
        self.enemies = []

        left_enemy_x = None
        right_enemy_x = None

        # White team
        if self.team == 'w':
            if self.x > 1:
                left_enemy_x = self.x - 1
            if self.x < 8:
                right_enemy_x = self.x + 1

            if self.y < 8:
                if left_enemy_x:
                    if board[left_enemy_x][self.y + 1] in self.pieces_map:
                        left_enemy = self.get_piece(left_enemy_x, self.y + 1)

                        if left_enemy.team != self.team:
                            self.enemies.append(left_enemy)

                if right_enemy_x:
                    if board[right_enemy_x][self.y + 1] in self.pieces_map:
                        right_enemy = self.get_piece(right_enemy_x, self.y + 1)

                        if right_enemy.team != self.team:
                            self.enemies.append(right_enemy)

        # Black team
        if self.team == 'b':
            if self.x > 1:
                left_enemy_x = self.x - 1
            if self.x < 8:
                right_enemy_x = self.x + 1

            if self.y > 1:
                if left_enemy_x:
                    if board[left_enemy_x][self.y - 1] in self.pieces_map:
                        left_enemy = self.get_piece(left_enemy_x, self.y - 1)

                        if left_enemy.team != self.team:
                            self.enemies.append(left_enemy)

                if right_enemy_x:
                    if board[right_enemy_x][self.y - 1] in self.pieces_map:
                        right_enemy = self.get_piece(right_enemy_x, self.y - 1)

                        if right_enemy.team != self.team:
                            self.enemies.append(right_enemy)


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
