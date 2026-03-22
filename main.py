import pygame
import sys
from settings import *
from player import Player
from level import Level
from day_phase import DayPhase
from night_phase import NightPhase
from inventory import Inventory

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.level = Level()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.all_sprites.add(self.player)
        self.inventory = Inventory()
        
        self.day_phase = DayPhase(self.screen, self.player, self.all_sprites, self.inventory)
        self.night_phase = NightPhase(self.screen, self.player, self.all_sprites, self.inventory)
        self.phase = "DAY"
        self.day_timer = 0

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        if self.phase == "DAY":
            self.all_sprites.update()
            self.day_phase.update()
            self.day_timer += 1
            if self.day_timer > 600: # 10 seconds of day
                self.phase = "NIGHT"
                for cust in self.day_phase.customers:
                    cust.kill()
        else:
            self.player.update()
            self.night_phase.update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.level.draw()
        self.all_sprites.draw(self.screen)
        self.day_phase.draw()
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()
