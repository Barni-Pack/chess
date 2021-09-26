import pygame

from config import tile_size, surface
from os import path


class Tile:
    """Tile class. Draw method"""

    def __init__(self, name, x, y, color, size=tile_size):
        self.name = name
        self.x, self.y = x, y
        self.size = size
        self.color = color

    def draw(self):
        pygame.draw.rect(surface,
                         self.color,
                         pygame.Rect(self.x, self.y, self.size, self.size))


# def create_and_draw_all_tiles(tiles_map_):
#     # Creates instances of tiles and draws them
#     for name in tiles_map_.keys():
#         exec(f'{name} = Tile("{name}")')
#         exec(f'{name}.draw()')


class Pawn:
    def __init__(self, team, tile: Tile):
        self.team = team
        self.killable = True
        if team == 'white':
            self.image = 'w_king.png'
        else:
            self.image = 'b_king.png'
        self.tile = tile

    def draw(self):
        pawn_image = pygame.image.load(path.join(path.join('img',
                                                           'chess_pieces'),
                                                 self.image))
        image_width, image_height = pawn_image.get_width(), pawn_image.get_height()
        
        # pawn_image = pygame.transform.scale(pawn_image, (int(tile_size * 0.75),
        #                                                  int(tile_size * 0.75)))

        # surface.blit(pawn_image, (self.tile.x + (tile_size - image_width) / 2,
        #                           self.tile.y + (tile_size - image_height) / 2))

        pygame.draw.rect(surface,
                         (255, 0, 0),
                         pygame.Rect(self.tile.x + (tile_size - image_width) / 2,
                                     self.tile.y + (tile_size - image_height) / 2,
                                     image_width, image_height))
