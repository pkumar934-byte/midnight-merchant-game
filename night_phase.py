import pygame
import random
import math
from settings import *
from enemies import Ghost

class NightPhase:
    def __init__(self, display_surface, player, all_sprites, inventory):
        self.display_surface = display_surface
        self.player = player
        self.all_sprites = all_sprites
        self.inventory = inventory
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 36)
        self.enemies = pygame.sprite.Group()
        self.spawn_timer = 0
        self.game_over = False
        self.cooldown = 0
        
    def update(self):
        if self.game_over: return
        self.spawn_timer += 1
        if self.spawn_timer > 120:
            self.spawn_timer = 0
            ghost = Ghost(random.randint(0, WINDOW_WIDTH), 0)
            self.enemies.add(ghost)
            self.all_sprites.add(ghost)
            
        self.enemies.update((self.player.rect.x, self.player.rect.y))
        
        if self.cooldown > 0: self.cooldown -= 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.inventory.items and self.cooldown == 0:
            self.inventory.remove_item(self.inventory.items[0])
            self.cooldown = 30
            for enemy in list(self.enemies):
                if math.hypot(enemy.rect.x - self.player.rect.x, enemy.rect.y - self.player.rect.y) < 150:
                    enemy.kill()
                    
        for enemy in self.enemies:
            if enemy.rect.colliderect(self.player.rect):
                self.game_over = True
        
    def draw(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(150)
        self.display_surface.blit(overlay, (0, 0))
        
        ui_rect = pygame.Rect(0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, 100)
        pygame.draw.rect(self.display_surface, (20, 0, 0), ui_rect)
        pygame.draw.rect(self.display_surface, WHITE, ui_rect, 2)
        
        info_text = self.font.render(f"NIGHT PHASE. Press SPACE to use unsellable items. Left: {len(self.inventory.items)}", True, RED)
        self.display_surface.blit(info_text, (20, WINDOW_HEIGHT - 80))
        
        if self.game_over:
            go_text = self.font.render("GAME OVER. Press ESC to quit.", True, RED)
            self.display_surface.blit(go_text, (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2))
