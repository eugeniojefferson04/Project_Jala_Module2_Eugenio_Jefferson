import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    """
    Cria o objeto do cacto.
    """

    CACTUS = [
        (LARGE_CACTUS, 300),
        (SMALL_CACTUS, 325),
    ]

    def __init__(self, theme:str):
        """
        Constrói um cacto. Modified by Eugênio Jefferson.
        :theme - Recebe o tema atual, para definir a cor do cacto.
        """
        self.CACTUS[0] = (LARGE_CACTUS[3:] if theme == 'light' else LARGE_CACTUS[:3], 300)
        self.CACTUS[1] = (SMALL_CACTUS[3:] if theme == 'light' else SMALL_CACTUS[:3], 325)

        image, cactus_pos = self.CACTUS[random.randint(0, 1)]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = cactus_pos