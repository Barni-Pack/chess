from classes.piece_classes import Bishop, King, Knight, Pawn, Queen, Rook, Piece
from mappings.board import board
from typing import List, Optional
from itertools import chain

# Creates mapping of piece name and Piece instance

_piece_classes = (Bishop, King, Knight, Pawn, Queen, Rook)


def piece_creator(piece_name: str) -> Piece:
    # Creates Piece class
    for piece_class in _piece_classes:
        if piece_class.__name__.lower() in piece_name:
            return piece_class(piece_name)
    raise KeyError('Piece name did not match any of available classes')


def used_pieces(board: List[List[Optional[str]]]) -> List[str]:
    # Returns list of used pieces
    board_1d = list(chain.from_iterable(board))
    used_pieces = [piece for piece in board_1d if piece]
    
    duplicated_pieces = set([piece for piece in used_pieces
                             if used_pieces.count(piece) > 1])
    if duplicated_pieces:
        raise ValueError('Duplicated pieces in the board. (board.py)')
    
    return used_pieces


pieces_map = {piece_name: piece_creator(piece_name)
              for piece_name in used_pieces(board)}


# pieces_map = {
#     'b_rook_1': Rook('b_rook_1'),
#     'b_knight_1': Knight('b_knight_1'),
#     'b_bishop_1': Bishop('b_bishop_1'),
#     'b_queen': Queen('b_queen'),
#     'b_king': King('b_king'),
#     'b_bishop_2': Bishop('b_bishop_2'),
#     'b_knight_2': Knight('b_knight_2'),
#     'b_rook_2': Rook('b_rook_2'),

#     'b_pawn_1': Pawn('b_pawn_1'),
#     'b_pawn_2': Pawn('b_pawn_2'),
#     'b_pawn_3': Pawn('b_pawn_3'),
#     'b_pawn_4': Pawn('b_pawn_4'),
#     'b_pawn_5': Pawn('b_pawn_5'),
#     'b_pawn_6': Pawn('b_pawn_6'),
#     'b_pawn_7': Pawn('b_pawn_7'),
#     'b_pawn_8': Pawn('b_pawn_8'),

#     'w_pawn_1': Pawn('w_pawn_1'),
#     'w_pawn_2': Pawn('w_pawn_2'),
#     'w_pawn_3': Pawn('w_pawn_3'),
#     'w_pawn_4': Pawn('w_pawn_4'),
#     'w_pawn_5': Pawn('w_pawn_5'),
#     'w_pawn_6': Pawn('w_pawn_6'),
#     'w_pawn_7': Pawn('w_pawn_7'),
#     'w_pawn_8': Pawn('w_pawn_8'),

#     'w_rook_1': Rook('w_rook_1'),
#     'w_knight_1': Knight('w_knight_1'),
#     'w_bishop_1': Bishop('w_bishop_1'),
#     'w_queen': Queen('w_queen'),
#     'w_king': King('w_king'),
#     'w_bishop_2': Bishop('w_bishop_2'),
#     'w_knight_2': Knight('w_knight_2'),
#     'w_rook_2': Rook('w_rook_2'),
# }

for _, piece in pieces_map.items():
    piece.set_pieces_map(pieces_map)
    piece.get_moves()
