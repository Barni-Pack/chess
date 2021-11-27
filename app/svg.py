import io
import pygame
import cairosvg

def load_svg(filename):
    new_bites = cairosvg.svg2png(url=filename)
    byte_io = io.BytesIO(new_bites)
    return pygame.image.load(byte_io)