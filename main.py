import pygame
from test import *
from classes.piece_classes import Pawn, Rook, Knight, Bishop, Queen, King
from mappings.tile_map import tile_map
from mappings.board import board
from mappings.pieces_map import pieces_map
from config import board_size, tile_size, screen_size
from game_data import selected, new_selected


def select_piece(pos_x, pos_y):
    global selected
    global new_selected

    # print(pos_x, pos_y)

    x = int(pos_x // tile_size) + 1
    y = int(pos_y // tile_size) + 1
    # print(x, y)
    tile = tile_map[x][y]

    piece_name = board[x][y]

    # Tile with piece was selected
    if piece_name:
        try:
            piece = pieces_map[piece_name]
        except:
            print('Piece was not found (dead probably)')
            return None

        # print(piece.name)

        # Select new if not selected
        if not selected:
            if piece:
                piece.select()
                piece.show_edible(pieces_map)
                # print(piece.x, piece.y)
                return piece

            else:
                return None

        # Select second piece
        elif selected:
            if piece:
                # Deselect if self
                if piece == selected:
                    selected.select()
                    selected.show_edible(pieces_map)
                    selected = None
                    return None

                # Select other if from the same team
                if piece.team == selected.team:
                    selected.select()
                    piece.select()
                    selected = piece
                    return None
                
                # Eat other if from the other team
                else:
                    selected.move2field(tile)
                    selected.select2die()
                    selected = None 
                    return None

    # Emtpy tile was selected
    elif not piece_name:
        # Do nothing if nothing was selected previously
        if not selected:
            return None

        # Move to second selected tile
        elif tile:
            # print(tile.name)
            selected.move2field(tile)
            selected = None
            return None


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
