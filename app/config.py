import pygame

screen_size = 800
surface = pygame.display.set_mode((screen_size, screen_size))

board_size = 8
tile_size = int(screen_size / board_size)

default_black_tile_color = (181, 136, 103)
default_white_tile_color = (241, 217, 183)

green_white_tile_color = (207, 207, 121)
green_black_tile_color = (168, 161, 76)

red_white_tile_color = (247, 145, 146)
red_black_tile_color = (207, 105, 106)