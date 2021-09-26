import pygame
from test import *
from classes import Tile, Pawn
from tiles import tiles_2d


def draw_all_tiles(tiles_2d_: list):
    # Creates instances of tiles and draws them
    for tile_columns in tiles_2d_:
        for tile in tile_columns:
            tile.draw()

if __name__ == "__main__":
    pygame.init()

    tiles = draw_all_tiles(tiles_2d)

    pygame.display.flip()

    pawn_1 = Pawn('white', tiles_2d[4][0])
    pawn_1.draw()
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
