from my_list import MyList


board_default = [
    ['b_rook_1', 'b_knight_1', 'b_bishop_1', 'b_queen',
     'b_king', 'b_bishop_2', 'b_knight_2', 'b_rook_2'],

    ['b_pawn_1', 'b_pawn_2', 'b_pawn_3', 'b_pawn_4',
     'b_pawn_5', 'b_pawn_6', 'b_pawn_7', 'b_pawn_8'],

    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],

    ['w_pawn_1', 'w_pawn_2', 'w_pawn_3', 'w_pawn_4',
     'w_pawn_5', 'w_pawn_6', 'w_pawn_7', 'w_pawn_8'],

    ['w_rook_1', 'w_knight_1', 'w_bishop_1', 'w_queen',
     'w_king', 'w_bishop_2', 'w_knight_2', 'w_rook_2', ],
]

board_test = [
    [None, None, None, 'w_rook_1', None, None, None, None],

    [None, None, None, None, None, None, None, 'b_rook_1'],

    [None, None, 'b_pawn_1', 'w_bishop_1',
     'b_pawn_2', None, 'w_knight_1', None],

    [None, None, 'b_pawn_3', 'b_king',
     'b_pawn_4', None, None, None],

    [None, None, 'w_rook_2', 'w_knight_2',
     'b_pawn_5', None, None, None],

    [None, None, None, None, None, None, None, None],

    ['w_bishop_2', None, 'b_bishop_1', None,
     None, 'b_knight_1', None, None],

    [None, None, None, 'w_queen',
     None, None, None, 'b_rook_2'],
]


board = board_test


def transpose(l1):
    l2 = []
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row = []
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2


board.reverse()
board = transpose(board)
board = MyList([MyList(row) for row in board])
