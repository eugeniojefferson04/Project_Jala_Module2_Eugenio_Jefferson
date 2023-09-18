from dino_runner.utils.constants import HEART, HEART_TYPE
from dino_runner.components.powerups.power_up import PowerUp


HEARTS = {
    1: [False],
    2: [False],
    3: [False]
}


class Heart(PowerUp):
    """
    Cria o coração. By Eugênio Jefferson.
    """
    def __init__(self):
        self.image = HEART
        self.type = HEART_TYPE
        super().__init__(self.image, self.type)

    def draw(self, screen):
        for heart in HEARTS.values():
            screen.blit()