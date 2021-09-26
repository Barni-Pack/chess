from typing import Optional
import pygame

from config import tile_size, surface
from os import path
import svg


class Pawn:
    def __init__(self, team):
        self.team = team
        self.killable = True
        if team == 'white':
            self.image = 'w_pawn.svg'
        else:
            self.image = 'b_pawn.svg'
            
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