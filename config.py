import pygame

screen_size = 800
surface = pygame.display.set_mode((screen_size, screen_size))

tiles_in_a_row = 8
tile_size = int(screen_size / tiles_in_a_row)

black_tile_color = (50, 50, 50)
white_tile_color = (255, 255, 255)