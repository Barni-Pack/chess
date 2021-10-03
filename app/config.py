import pygame

screen_width = 400
screen_height = int(screen_width * 9 / 4)
screen = pygame.display.set_mode((screen_width, screen_height))

screen_height_block = int(screen_height / 18)

header_window_h = 2 * screen_height_block
player_window_h = 3 * screen_height_block
board_window_h = 8 * screen_height_block
footer_window_h = 2 * screen_height_block

player_1_window_offset = header_window_h
board_window_offset = header_window_h + player_window_h
player_2_window_offset = header_window_h + player_window_h + board_window_h

board_row_tiles = 8
tile_size = int(board_window_h / board_row_tiles)

# Colors
background_color = (22, 21, 17)
screen.fill(background_color)

default_black_tile_color = (181, 136, 103)
default_white_tile_color = (240, 218, 181)

green_white_tile_color = (207, 207, 121)
green_black_tile_color = (168, 161, 76)

red_white_tile_color = (247, 145, 146)
red_black_tile_color = (207, 105, 106)

timer_background_color = (38, 38, 38)