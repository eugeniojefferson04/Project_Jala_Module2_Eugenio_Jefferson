from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle
from random import randint


class Bird(Obstacle):
    """
    Cria o objeto do pássaro. Modified by Eugênio Jefferson.
    """
    def __init__(self, theme:str):
        """
        Constrói o pássaro. Modified by Eugênio Jefferson.
        :theme - Recebe o tema atual, para definir a cor do pássaro.
        """
        bird_image = BIRD[2:] if theme == 'light' else BIRD[:2]
        super().__init__(bird_image, 0) # Alterei para mudar a cor de acordo com o tema;
        self.rect.y = randint(245, 300) # Coloquei um randint para o pássaro vim na altura aleatória;
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0