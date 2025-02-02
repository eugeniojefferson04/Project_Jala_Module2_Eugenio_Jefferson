import random, pygame
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.components.powerups.heart import Heart

class PowerUpManager:
    """
    Gerencia os itens. Modified by Eugênio Jefferson.
    """
    def __init__(self):
        self.power_ups = []
        self.when_appars = 0


    def generate_power_up(self, score):
        """
        Faz o item aparecer no jogo. Modified by Eugênio Jefferson.
        """
        power_up_type = [
            Shield(),
            Hammer(),
            Heart()
        ] # Criei essa lista com os tipos de itens disponíveis;

        if len(self.power_ups) == 0 and self.when_appars == score:
            self.when_appars += random.randint(80, 100) # Alterei o valor da chance de aparecer um item;
            # 1- Alterei para escolher um item aleatório; (RETIREI)
            #index = random.randint(0,2)

            # if index == 2 and random.randint(0, 99) < 70:
            #     index = 2

            # elif index == 2:
            #     index = 5

            # try:
            #     self.power_ups.append(power_up_type[index]) 
            # except Exception as e:
            #     pass
            # Fim 1
            self.power_ups.append(power_up_type[random.randint(0,2)])


    def update(self, score, game_speed, player, heart):
        """
        Gerencia os itens, verifica se foram coletados ou não. Modified by Eugênio Jefferson.
        """
        self.generate_power_up(score)

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()

                # 1- Verifica o tipo do item e ativa ele
                if power_up.type == "Escudo":
                    player.shield = True
                    player.hammer = False
                    player.heart = False
                
                if power_up.type == "Martelo":
                    player.hammer = True
                    player.shield = False
                    player.heart = False

                if power_up.type2 == "Coração":
                    player.heart = True
                    player.shield = False
                    player.hammer = False
                    player.type2 = power_up.type2
                    #player.type = power_up.type
                    heart.update_life(collected=True)
                
                if player.shield or player.hammer:
                    player.has_power_up = True
                    player.type = power_up.type
                    player.power_up_timing = power_up.start_time + (power_up.duration * 1000)                   

                self.power_ups.remove(power_up)
                # Fim 1


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)


    def reset_power_ups(self):
        """
        Exclui o item. Modified by Eugênio Jefferson.
        """
        self.power_ups = []
        self.when_appars = random.randint(50, 120) # Alterei o valor da chance de aparecer um item;
        