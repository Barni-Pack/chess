from typing import Optional
import pygame

from config import tile_size, surface, board_size
from os import path
import svg
from grid_map import grid_map


def index_2d(list_2d, key):
    for y, column in enumerate(list_2d):
        if key in column:
            x = column.index(key)
            return x, board_size-y-1


class Piece:
    def __init__(self, name, killable=False):
        self.team = name[0]
        self.killable = killable
        self.coordinate = index_2d(grid_map, name)
        self.x, self.y = self.coordinate
        self.type = name.split('_')[1]
        
        if self.team == 'w':
            self.image = f'w_{self.type}.svg'
        else:
            self.image = f'b_{self.type}.svg'
            
    def draw(self):
        pawn_image = svg.load_svg(path.join('svg', self.piece.image))

        scale=0.75
        pawn_image=pygame.transform.smoothscale(pawn_image, (int(tile_size * scale),
                                                         int(tile_size * scale)))

        image_width, image_height=pawn_image.get_width(), pawn_image.get_height()
        
        x_pixels=(self.x - 1) * tile_size,
        y_pixels=(board_size - self.y) * tile_size

        surface.blit(pawn_image, (x_pixels + (tile_size - image_width) / 2,
                                  y_pixels + (tile_size - image_height) / 2))
        


class Pawn(Piece):
    def show_moves(self):
        return
        
            
class Rook:
    def __init__(self, team):
        self.team = team
        self.killable = True
        if team == 'white':
            self.image = 'w_rook.svg'
        else:
            self.image = 'b_rook.svg'
            

class Knight:
    def __init__(self, team):
        self.team = team
        self.killable = True
        if team == 'white':
            self.image = 'w_knight.svg'
        else:
            self.image = 'b_knight.svg'
            

class Bishop:
    def __init__(self, team):
        self.team = team
        self.killable = True
        if team == 'white':
            self.image = 'w_bishop.svg'
        else:
            self.image = 'b_bishop.svg'
            

class Queen:
    def __init__(self, team):
        self.team = team
        self.killable = True
        if team == 'white':
            self.image = 'w_queen.svg'
        else:
            self.image = 'b_queen.svg'
            
            
class King:
    def __init__(self, team):
        self.team = team
        self.killable = True
        if team == 'white':
            self.image = 'w_king.svg'
        else:
            self.image = 'b_king.svg'



class Tile:
    """Tile class. Draw method"""

    def __init__(self, name, x, y, color, piece=None):
        self.name = name
        self.x, self.y = x, y
        self.size = tile_size
        self.color = color
        
        self.piece = piece

    def draw(self):
        pygame.draw.rect(surface,
                         self.color,
                         pygame.Rect(self.x, self.y, self.size, self.size))
        
    def draw_piece(self):
        # pawn_image = pygame.image.load(path.join(path.join('img',
        #                                                    'chess_pieces'),
        #                                          self.image))

        pawn_image = svg.load_svg(path.join('svg', self.piece.image))

        scale=0.75
        pawn_image=pygame.transform.smoothscale(pawn_image, (int(tile_size * scale),
                                                         int(tile_size * scale)))

        image_width, image_height=pawn_image.get_width(), pawn_image.get_height()

        surface.blit(pawn_image, (self.x + (tile_size - image_width) / 2,
                                  self.y + (tile_size - image_height) / 2))