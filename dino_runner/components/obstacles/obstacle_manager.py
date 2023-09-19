import pygame, random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import DINO_DEAD, DUCKING_DEAD, DEATH_SOUND # Importei para alterar a imagem do dino quando ele morrer, e tocar som;

class Obstacle_Manager: # Alterei o nome da classe de 'ObstacleManager' para 'Obstacle_Manager', que é como está sendo chamada nos outros modulos
    """
    Gerencia os obstaculos. Modified by Eugênio Jefferson.
    """
    def __init__(self):
        self.obstacles = []
        

    def update(self, game, theme:str, heart):
        """
        Adiciona o obstáculo no jogo e verifica se o Dino bateu nele. Modified by Eugênio Jefferson.
        :theme - Recebe o tema atual, para definir a cor do obstáculo.
        """
        self.theme = theme  # Criei para passar o valor do tema para a classe dos obstáculos;
        obstacle_type = [
            Cactus(self.theme), # Alterei por causa do tema;
            Bird(self.theme) # Alterei por causa do tema;
        ]
        
        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0, 1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    # 2- Faz a função do coração
                    if heart.has():
                        heart.update_life(used=True)
                        self.obstacles.remove(obstacle)
                        
                    else:
                        # 1 - Altera a imagem quando o Dino morre
                        x_pos = game.player.dino_rect.x
                        y_pos = game.player.dino_rect.y
                        
                        if not game.player.dino_duck:
                            game.player.image = DINO_DEAD[1] if theme == 'light' else DINO_DEAD[0]
                            
                        else: 
                            game.player.image = DUCKING_DEAD[1] if theme == 'light' else DUCKING_DEAD[0]

                        game.player.dino_rect = game.player.image.get_rect()
                        game.player.dino_rect.x = x_pos
                        game.player.dino_rect.y = y_pos
                        # Fim 1
                        #pygame.time.delay(2000) #Removi o delay daqui para suavizar a colisão;
                        game.playing = False
                        game.death_count += 1
                        DEATH_SOUND.play() # toca som de morte;
                        break
                    # Fim 2

                else:
                    self.obstacles.remove(obstacle)


    def reset_obstacles(self):
        self.obstacles = []


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)