import pygame
from pygame.sprite import Sprite # Removi '_Group' que não tem no modulo sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, JUMP_SOUND # Importei JUMP_SOUND

DUCK_IMG = {
    DEFAULT_TYPE: DUCKING,
    SHIELD_TYPE: DUCKING_SHIELD
}

JUMP_IMG = {
    DEFAULT_TYPE: JUMPING,
    SHIELD_TYPE: JUMPING_SHIELD
}

RUN_IMG = {
    DEFAULT_TYPE: RUNNING,
    SHIELD_TYPE: RUNNING_SHIELD
}

X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8.5

class Dinosaur(Sprite):
    """
    Cria e gerencia o Dino.
    """
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = JUMP_VEL
        self.power_up_timing = 0 # Inicializei a variável power_up_timing
        self.setup_state()


    def setup_state(self):
        """
        Define os status iniciais dos itens.
        """
        self.has_power_up = False 
        self.shield = False 
        self.show_text = False
        self.shield_time_up = 0 
        

    def update(self, user_input, theme:str):
        """
        Realiza a movimentação do Dino de acordo com os eventos assionados. Modified by Eugênio Jefferson.
        :theme - Recebe o tema atual para gerenciar as cores;
        """
        if self.dino_run:
            self.run(theme) # Alterei por causa do tema;

        elif self.dino_jump:
            self.jump(theme) # Alterei por causa do tema;

        elif self.dino_duck:
            self.duck(theme) # Alterei por causa do tema;
            
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
            JUMP_SOUND.play() # Toca o som do pulo;

        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True

        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step_index >= 9:
            self.step_index = 0


    def run(self, theme:str):
        """
        Faz a animação da corrida do Dino. Modified by Eugênio Jefferson.
        :theme - Recebe o tema atual, para definir a cor do Dino.
        """
        RUN_IMG[DEFAULT_TYPE] = RUNNING[2:] if theme == 'light' else RUNNING[:2] # Alterei para mudar a cor de acordo com o tema;
        RUN_IMG[SHIELD_TYPE] = RUNNING_SHIELD[2:] if theme == 'light' else RUNNING_SHIELD[:2] # Alterei para mudar a cor de acordo com o tema;

        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1


    def jump(self, theme:str):
        """
        Realiza o pulo do Dino. Modified by Eugênio Jefferson.
        :theme - Recebe o tema atual, para definir a cor do Dino.
        """
        JUMP_IMG[DEFAULT_TYPE] = JUMPING[1] if theme == 'light' else JUMPING[0] # Alterei para mudar a cor de acordo com o tema;
        JUMP_IMG[SHIELD_TYPE] = JUMPING_SHIELD[1] if theme == 'light' else JUMPING_SHIELD[0] # Alterei para mudar a cor de acordo com o tema;

        self.image = JUMP_IMG[self.type]
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.dino_jump = False
            self.jump_vel =  JUMP_VEL


    def duck(self, theme:str):
        """
        Faz o Dino se abaixar. Modified by Eugênio Jefferson.
        :theme - Recebe o tema atual, para definir a cor do Dino.
        """
        DUCK_IMG[DEFAULT_TYPE] = DUCKING[2:] if theme == 'light' else DUCKING[:2] # Alterei para mudar a cor de acordo com o tema;
        DUCK_IMG[SHIELD_TYPE] = DUCKING_SHIELD[2:] if theme == 'light' else DUCKING_SHIELD[:2] # Alterei para mudar a cor de acordo com o tema;

        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False


    def draw(self, screen):
        """
        Inseri o Dino na tela.
        """
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))