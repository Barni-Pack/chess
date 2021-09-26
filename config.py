import pygame

screen_size = 800
surface = pygame.display.set_mode((screen_size, screen_size))

board_size = 8
tile_size = int(screen_size / board_size)

black_tile_color = (181, 136, 103)
white_tile_color = (241, 217, 183)