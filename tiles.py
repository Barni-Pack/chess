from config import tiles_in_a_row, tile_size, white_tile_color, black_tile_color
from classes import Tile

# tiles_map = dict()

# for column in range(1, tiles_in_a_row + 1):
#     for row, letter in zip(range(1, tiles_in_a_row + 1),
#                            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
#         tiles_map[letter + str(column)] = {'x': (row - 1) * tile_size,
#                                            'y': (tiles_in_a_row - column) * tile_size,
#                                            'color': white_tile_color if (row + column) % 2 == 0 else black_tile_color}

tiles_2d = [[None for j in range(tiles_in_a_row)] for i in range(tiles_in_a_row)] # type: list[list]
# tiles_2d = list() # type: list[list]

for column in range(1, tiles_in_a_row + 1):
    for row, letter in zip(range(1, tiles_in_a_row + 1),
                           ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        color = white_tile_color if (row + column) % 2 == 0 else black_tile_color
        tiles_2d[row-1][column-1] = Tile(letter + str(column),
                                     x=(row - 1) * tile_size,
                                     y=(tiles_in_a_row - column) * tile_size,
                                     color=color)
