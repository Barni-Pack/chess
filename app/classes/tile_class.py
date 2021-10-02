from config import board_size, tile_size, white_tile_color, black_tile_color, selected_white_tile_color, selected_black_tile_color, red_tile_color
import pygame
from config import surface

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
        # Choose team based on coordinates
        self.team = 'white' if (self.x + self.y) % 2 == 0 else 'black'
        self.selected = False
        self.die = False
        self.set_color()
        self.draw()

    # Set tile color based on tiile team and selected state
    def set_color(self):
        if self.die:
            self.color = red_tile_color
            return

        if self.team == 'white':
            if self.selected:
                self.color = selected_white_tile_color
            else:
                self.color = white_tile_color
        else:
            if self.selected:
                self.color = selected_black_tile_color
            else:
                self.color = black_tile_color

    # Draws tile

    def draw(self):
        pygame.draw.rect(surface,
                         self.color,
                         pygame.Rect(self.x_pixels, self.y_pixels, self.size, self.size))
        pygame.display.flip()

    # Selects or deselects tile

    def select(self):
        self.selected = not self.selected
        self.set_color()
        self.draw()

    # def deselect(self):
    #     self.selected = False
    #     self.set_color()
    #     self.draw()
    #     pygame.display.flip()

    def select2die(self):
        self.die = not self.die
        self.select()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name + '|' + str(self.x) + ':' + str(self.y)
