from config import board_size, tile_size, white_tile_color, black_tile_color
from classes import Tile


grid = [[None for j in range(board_size)] for i in range(board_size)] # type: list[list]

for column in range(1, board_size + 1):
    for row, letter in zip(range(1, board_size + 1),
                           ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        color = white_tile_color if (row + column) % 2 == 0 else black_tile_color
        grid[row-1][column-1] = Tile(letter + str(column),
                                     x=(row - 1) * tile_size,
                                     y=(board_size - column) * tile_size,
                                     color=color)
