import pygame
from test import *
from classes import Tile, Pawn, Rook, Knight, Bishop, Queen, King
from tiles import tiles_2d
from config import tiles_in_a_row


def draw_all_tiles(tiles_2d_: list):
    # Creates instances of tiles and draws them
    for tile_columns in tiles_2d_:
        for tile in tile_columns:
            tile.draw()


def init_pieces(tiles_2d_):
    # WHITE
    
    # Pawns
    for row in range(tiles_in_a_row):
        tiles_2d_[row][1].piece = Pawn('white')
        tiles_2d_[row][1].draw_piece()
    
    # Rooks
    for row in [0, 7]:
        tiles_2d_[row][0].piece = Rook('white')
        tiles_2d_[row][0].draw_piece()
        
    # Knigts
    for row in [1, 6]:
        tiles_2d_[row][0].piece = Knight('white')
        tiles_2d_[row][0].draw_piece()
        
    # Bishops
    for row in [2, 5]:
        tiles_2d_[row][0].piece = Bishop('white')
        tiles_2d_[row][0].draw_piece()
        
    # Queen
    tiles_2d_[3][0].piece = Queen('white')
    tiles_2d_[3][0].draw_piece()
        
    # King
    tiles_2d_[4][0].piece = King('white')
    tiles_2d_[4][0].draw_piece()
        


if __name__ == "__main__":
    pygame.init()

    tiles = draw_all_tiles(tiles_2d)
    init_pieces(tiles_2d)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
