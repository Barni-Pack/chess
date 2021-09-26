import pygame
from test import *
from classes import Tile, Pawn, Rook, Knight, Bishop, Queen, King
from tiles import grid
from config import board_size


def draw_all_tiles(grid_: list):
    # Creates instances of tiles and draws them
    for tile_columns in grid_:
        for tile in tile_columns:
            tile.draw()


def init_pieces(grid_):
    # WHITE
    
    # Pawns
    for row in range(board_size):
        grid_[row][1].piece = Pawn('white')
        grid_[row][1].draw_piece()
    
    # Rooks
    for row in [0, 7]:
        grid_[row][0].piece = Rook('white')
        grid_[row][0].draw_piece()
        
    # Knigts
    for row in [1, 6]:
        grid_[row][0].piece = Knight('white')
        grid_[row][0].draw_piece()
        
    # Bishops
    for row in [2, 5]:
        grid_[row][0].piece = Bishop('white')
        grid_[row][0].draw_piece()
        
    # Queen
    grid_[3][0].piece = Queen('white')
    grid_[3][0].draw_piece()
        
    # King
    grid_[4][0].piece = King('white')
    grid_[4][0].draw_piece()
    
    
def click()

        


if __name__ == "__main__":
    pygame.init()

    tiles = draw_all_tiles(grid)
    init_pieces(grid)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    y, x = Find_Node(pos, WIDTH)
                    if selected == False:
                        try:
                            possible = select_moves((board[x][y]), (x, y), moves)
                            for positions in possible:
                                row, col = positions
                                grid[row][col].colour = BLUE
                            piece_to_move = x, y
                            selected = True
                        except:
                            piece_to_move = []
                            print('Can\'t select')
    
