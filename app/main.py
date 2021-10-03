import pygame
from pygame.constants import VIDEORESIZE
from test import *
from mappings.tile_map import tile_map
from mappings.board import board
from mappings.pieces_map import pieces_map
from config import board_window_h, tile_size, board_window_offset
import config
from session_data import selected, new_selected, current_player


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
            print('Piece was not found (huh???)')
            return None

        # Select new if not selected
        if not selected:
            if piece:
                # Select only from self team
                if current_player().team == piece.team:
                    piece.select()
                    return piece

            else:
                return None

        # Select second piece
        elif selected:
            if piece:
                # Deselect if self
                if piece == selected:
                    selected.deselect()
                    selected = None
                    return None

                # Select other if from the same team
                if piece.team == selected.team:
                    selected.deselect()
                    piece.select()
                    selected = piece
                    return None
                
                # Eat other if from the other team
                else:
                    selected.kill(piece)
                    selected = None 
                    return None

    # Emtpy tile was selected
    elif not piece_name:
        # Do nothing if nothing was selected previously
        if not selected:
            return None

        # Move to second selected tile
        elif tile:
            selected.move2tile(tile)
            selected = None
            return None
        

def update_all_pieces_data():
    for piece_name in sum(board, []):
        pieces_map[piece_name].update_data() if piece_name else None        


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    
    pygame.display.flip()
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                
            # if event.type == VIDEORESIZE:
                # config.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                # config.board_window_h = config.screen.get_width()
                # print(config.screen.get_width())

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                pos_y = board_window_h - pos_y

                if not selected:
                    selected = select_piece(pos_x, pos_y + board_window_offset)
                else:
                    new_selected = select_piece(pos_x, pos_y + board_window_offset)
        
        clock.tick(30)