import pygame
import math
from settings import *

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE - 20, TILE_SIZE - 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2

    def update(self, player_pos=None):
        if player_pos:
            dx = player_pos[0] - self.rect.x
            dy = player_pos[1] - self.rect.y
            dist = math.hypot(dx, dy)
            if dist != 0:
                self.rect.x += int(dx / dist * self.speed)
                self.rect.y += int(dy / dist * self.speed)
