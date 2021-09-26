from classes import Pawn

pieces = {
    # 'b_rook_1': Rook(),
    # 'b_knight_1': Knight(),
    # 'b_bishop_1': Bishop(),
    # 'b_queen': Queen(),
    # 'b_king': King(),
    # 'b_bishop_2': Bishop(),
    # 'b_knight_2': Knight(),
    # 'b_rook_2': Rook(),
    'b_pawn_1': Pawn('b_pawn_1'),
}


# x, y = index_2d(grid_map, 'b_rook_1')
# grid_map_key = grid_map[x][y]
# print(grid_map[x][y])

print(pieces['b_pawn_1'].x)