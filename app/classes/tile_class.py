from pygame.surfarray import blit_array
from config import board_row_tiles, tile_size, default_white_tile_color, default_black_tile_color, green_white_tile_color, green_black_tile_color, red_white_tile_color, red_black_tile_color
from config import board_window_offset
import pygame
from config import screen

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

         # Gui pixel offset
        self.offset = board_window_offset
        
        self.y_pixels = (board_row_tiles - self.y) * tile_size + self.offset
        self.x_pixels = (self.x - 1) * tile_size

        self.size = tile_size
        # Choose team based on coordinates
        self.team = 'white' if (self.x + self.y) % 2 == 0 else 'black'
        self.draw_default()
                
    def draw_default(self):
        if self.team == 'white':
            self.color = default_white_tile_color
        else:
            self.color = default_black_tile_color
            
        self.draw()
    
    def draw_green(self):
        if self.team == 'white':
            self.color = green_white_tile_color
        else:
            self.color = green_black_tile_color
            
        self.draw()
    
    def draw_red(self):
        if self.team == 'white':
            self.color = red_white_tile_color
        else:
            self.color = red_black_tile_color
            
        self.draw()

    # Draws tile
    def draw(self):
        pygame.draw.rect(screen,
                         self.color,
                         pygame.Rect(self.x_pixels, self.y_pixels, self.size, self.size))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
