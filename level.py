import pygame
from settings import *

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def update(self):
        pass

    def draw(self):
        # Draw basic floor grid
        for x in range(0, WINDOW_WIDTH, TILE_SIZE):
            pygame.draw.line(self.display_surface, (50, 50, 50), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
            pygame.draw.line(self.display_surface, (50, 50, 50), (0, y), (WINDOW_WIDTH, y))
