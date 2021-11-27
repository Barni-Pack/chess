from pygame import font
from pygame.draw import circle
from classes.player_class import Player
from config import player_1_window_offset, player_2_window_offset, player_window_h, screen_width, screen, timer_background_color
import pygame

selected = None
new_selected = None
dead_pieces = []

game_time = 10

player_1 = Player('Player 1', 'w', True)
player_2 = Player('Player 2', 'b', False)


def switch_turn():
    player_1.turn, player_2.turn = player_2.turn, player_1.turn
    switch_timer()


def current_player():
    for player in (player_1, player_2):
        if player.turn:
            return player


def draw_gui():
    draw_player_block(player_1)
    draw_timer(player_1)
    draw_player_block(player_2)
    draw_timer(player_2)
    return


def switch_timer():
    return


def draw_timer(player):
    if player.team == 'b':
        offset = player_1_window_offset
    else:
        offset = player_2_window_offset

    font_size = 60
    font_type = 'static/fonts/ttf/Roboto-Regular.ttf'
    time = '09:27'

    text_width = get_text_width(time, font_type, font_size)

    x = screen_width - player_window_h
    gap = 35

    x, y = get_postion_to_place_in_middle(parent_x=screen_width - player_window_h,
                                          parent_y=offset + gap,
                                          parent_width=player_window_h,
                                          parent_height=player_window_h - gap * 2,
                                          self_width=text_width,
                                          self_height=font_size)

    text_to_screen(time,
                   x=x,
                   y=y,
                   size=font_size,
                   font_type='static/fonts/ttf/Roboto-Regular.ttf')

    return


def get_text_width(text, font_type, font_size):
    font_size = int(font_size * 0.85)
    font = pygame.font.Font(font_type, font_size)
    text_width, text_height = font.size(text)
    return text_width


def draw_player_block(player):
    if player.team == 'b':
        offset = player_1_window_offset
    else:
        offset = player_2_window_offset

    # Online indicator
    circle_radius = 8
    _, y = get_postion_to_place_in_middle(parent_y=offset,
                                          parent_height=player_window_h,
                                          self_height=circle_radius*2)

    pygame.draw.circle(screen, (117, 153, 1),
                       (10 + circle_radius, y + circle_radius + 3), circle_radius)

    # Player name
    font_size = 30
    _, y = get_postion_to_place_in_middle(parent_y=offset,
                                          parent_height=player_window_h,
                                          self_height=font_size)
    text_to_screen(player.name,
                   10 + circle_radius * 2 + 5, y,
                   size=font_size)

    # Timer block
    gap = 35

    pygame.draw.rect(screen,
                     timer_background_color,
                     pygame.Rect(screen_width - player_window_h, offset + gap,
                                 player_window_h, player_window_h - gap * 2))


def get_postion_to_place_in_middle(parent_x=None, parent_y=None,
                                   parent_width=None, parent_height=None,
                                   self_width=None, self_height=None):
    """Returns x and y. Block on that position will be in the middle of its parent"""

    if parent_x and parent_width and self_width:
        x = parent_x + int((parent_width - self_width) / 2)
    else:
        x = None

    if parent_y and parent_height and self_height:
        y = parent_y + int((parent_height - self_height) / 2)
    else:
        y = None

    return x, y


def text_to_screen(text, x, y, size,
                   color=(200, 200, 200), font_type='static/fonts/ttf/NotoSans-Regular.ttf'):
    global screen
    try:
        text = str(text)
        size = int(size * 0.85)
        font = pygame.font.Font(font_type, size)

        background_color = None
        # background_color=(100, 0, 0)
        text = font.render(text, True, color, background_color)
        screen.blit(text, (x, y))

    except Exception as e:
        print(f'Font Error, saw it coming^ {e}')
        raise e
