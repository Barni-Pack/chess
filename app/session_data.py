from classes.player_class import Player


selected = None
new_selected = None
dead_pieces = []

game_time = 10

player_1 = Player('Player 1', 'w', True)
player_2 = Player('Player 2', 'b', False)

def switch_turn():
    player_1.turn, player_2.turn = player_2.turn, player_1.turn
    
def current_player():
    for player in (player_1, player_2):
        if player.turn:
            return player