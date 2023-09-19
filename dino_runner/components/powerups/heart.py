from dino_runner.utils.constants import HEART, HEART_TYPE, DEFAULT_TYPE
from dino_runner.components.powerups.power_up import PowerUp


HEARTS = {
    1: [False, HEART[0]],
    2: [False, HEART[0]],
    3: [False, HEART[0]]
}


class Heart(PowerUp):
    """
    Cria o coração. By Eugênio Jefferson.
    """
    def __init__(self):
        self.image = HEART[2]
        self.type = DEFAULT_TYPE
        super().__init__(self.image, self.type, type2=HEART_TYPE) # modifiquei para ter o tipo do coração


    def update_life(self, collected=False, used=False):
        if collected:
            for h in HEARTS.values():
                if not h[0]:
                    h[0] = True
                    h[1] = HEART[1]
                    break
        
        if used:
            for h in reversed(HEARTS.values()):
                if h[0]:
                    h[0] = False
                    h[1] = HEART[0]
                    break

    
    def has(self):
        has = False
        for h in HEARTS.values():
            if h[0]:
                has = True
                break
        return has


    def draw_lifes(self, screen):
        x_pos = 0
        for heart in HEARTS.values():
            if x_pos == 0:
                x_pos += 20
            else:
                x_pos += 20 + self.image.get_width()

            screen.blit(heart[1], (x_pos, 20))