import pygame
from settings import *

class Customer(pygame.sprite.Sprite):
    def __init__(self, x, y, dest_x, dest_y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE - 20, TILE_SIZE - 20))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.state = "walking_in"
        self.wait_timer = 0
        
    def update(self):
        if self.state == "walking_in":
            if self.rect.x < self.dest_x: self.rect.x += self.speed
            elif self.rect.x > self.dest_x: self.rect.x -= self.speed
            if self.rect.y < self.dest_y: self.rect.y += self.speed
            elif self.rect.y > self.dest_y: self.rect.y -= self.speed
            
            if abs(self.rect.x - self.dest_x) <= self.speed and abs(self.rect.y - self.dest_y) <= self.speed:
                self.state = "waiting"
                
        elif self.state == "waiting":
            self.wait_timer += 1
            if self.wait_timer > 300: # Wait 5 seconds
                self.state = "walking_out"
                
        elif self.state == "walking_out":
            self.rect.y += self.speed
            if self.rect.y > WINDOW_HEIGHT:
                self.kill()
