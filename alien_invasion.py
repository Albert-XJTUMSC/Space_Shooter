import pygame
import sys

from settings import Settings
from ship import Ship
from pygame.sprite import Group

import game_functions as gf

def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update(ai_settings)
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()