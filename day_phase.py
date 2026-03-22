import pygame
import random
from settings import *
from customers import Customer

class DayPhase:
    def __init__(self, display_surface, player, all_sprites, inventory):
        self.display_surface = display_surface
        self.player = player
        self.all_sprites = all_sprites
        self.inventory = inventory
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 36)
        self.money = 100
        self.customers = pygame.sprite.Group()
        self.spawn_timer = 0
        
    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer > 180 and len(self.customers) < 3:
            self.spawn_timer = 0
            cust = Customer(random.randint(100, WINDOW_WIDTH - 100), WINDOW_HEIGHT, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)
            self.customers.add(cust)
            self.all_sprites.add(cust)
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            for cust in self.customers:
                if cust.state == "waiting" and self.inventory.items:
                    item_to_sell = self.inventory.items[0]
                    self.money += item_to_sell.value
                    self.inventory.remove_item(item_to_sell)
                    cust.state = "walking_out"
                    break
        
    def draw(self):
        ui_rect = pygame.Rect(0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, 100)
        pygame.draw.rect(self.display_surface, (40, 40, 40), ui_rect)
        pygame.draw.rect(self.display_surface, WHITE, ui_rect, 2)
        
        money_text = self.font.render(f"Gold: {self.money}", True, GOLD)
        self.display_surface.blit(money_text, (20, WINDOW_HEIGHT - 80))
        
        info_text = self.font.render(f"Press SPACE to sell. Items: {len(self.inventory.items)}", True, WHITE)
        self.display_surface.blit(info_text, (200, WINDOW_HEIGHT - 80))
