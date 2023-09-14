import random
from typing import Any
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        

    def update(self, obstacle_pos, obstacle):
        self.rect.x -= obstacle_pos

        if self.rect.x < - self.rect.width:
            object.pop()


    def draw(self, screen):
        screen.blit(self.image, self.rect)