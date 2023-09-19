import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp(Sprite):
    """
    Cria um item na tela. Modified by Eugênio Jefferson.
    """
    def __init__(self, image, type, type2=''):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(400, 800) # alterei o valor da posição
        self.rect.y = random.randint(125, 175)
        self.start_time = 0
        self.duration = random.randint(5, 10)
        self.type2 = type2 # para adicionar um segundo tipo


    def update(self, game_speed, power_ups):
        """
        Atualiza o item, realizando a sua movimentação ou excluindo quando ele sai da tela.
        """
        self.rect.x -= game_speed
        
        if self.rect.x < -self.rect.width:
            power_ups.pop()


    def draw(self, screen):
        screen.blit(self.image, self.rect)