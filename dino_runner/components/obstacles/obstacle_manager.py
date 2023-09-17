import pygame, random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class Obstacle_Manager: # Alterei o nome da classe de 'ObstacleManager' para 'Obstacle_Manager', que é como está sendo chamada nos outros modulos
    """
    Gerencia os obstaculos.
    """
    def __init__(self):
        self.obstacles = []
        

    def update(self, game, theme:str):
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
                    #pygame.time.delay(2000) Removi o delay daqui para suavizar a colisão;
                    game.playing = False
                    game.death_count += 1
                    break

                else:
                    self.obstacles.remove(obstacle)


    def reset_obstacles(self):
        self.obstacles = []


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)