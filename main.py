import pygame
from test import *
from classes import Pawn, Rook, Knight, Bishop, Queen, King
from tiles import tile_map
from grid_map import grid_map
from pieces_map import pieces_map
from config import board_size, tile_size, screen_size
from game_data import selected, new_selected


def draw_all_tiles(grid_: list):
    # Creates instances of tiles and draws them
    for tile_columns in grid_:
        for tile in tile_columns:
            tile.draw()


def select_piece(pos_x, pos_y):
    global selected
    global new_selected
    
    # print(pos_x, pos_y)

    x = int(pos_x // tile_size) + 1
    y = int(pos_y // tile_size) + 1
    # print(x, y)
    
    piece_name = grid_map[x][y]
    tile_name = tile_map[x][y]
    # print(tile_name, piece_name)
    # print(tile_name.coordinates)

    # Selects piece if it exists
    if piece_name:
        try:
            piece = pieces_map[piece_name]
        except:
            print('Piece was not found (dead probably)')
            return None
        
        # print(piece.name)

    # Select
    if not selected:
        if piece:
            piece.select()
            # print(piece.x, piece.y)
            return piece

        else:
            return None

    else:
     # New_selected
        if piece:
            # Deselect if self
            if piece == selected:
                selected.select()
                selected = None
                return None

            # Select other if from the same team
            if piece.team == selected.team:
                # selected.select()
                # piece.select()
                selected = piece
                return None

        # if field:
        #     selected.move2field(field)
            
        #     selected = None
        #     return None


if __name__ == "__main__":
    pygame.init()

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                pos_y = screen_size - pos_y

                if not selected:
                    selected = select_piece(pos_x, pos_y)
                else:
                    new_selected = select_piece(pos_x, pos_y)

                # print(selected, new_selected)
