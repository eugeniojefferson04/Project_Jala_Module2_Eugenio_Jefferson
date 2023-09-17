import pygame, random # Importem a biblioteca random
# importei CLOUD, THEME_ICON, GAME_OVER, RESET, SCORE_SOUND, ARROW_KEY, DINO_RUNNER
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, CLOUD, THEME_ICON, GAME_OVER, RESET, SCORE_SOUND, ARROW_KEY, DINO_RUNNER
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import Obstacle_Manager # Adicionei a pasta no caminho da importação
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.utils.text_utils import draw_message_component # Importei a função 'draw_message_component' pois estamos chamando ela


class Game:
    """
    Gerencia as interfaces e os eventos do jogo
    """

    def __init__(self):
        """
        Constroe a classe game e seus atributos. Modified by Eugênio Jefferson.
        """
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON[1])

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.x_pos_clound1 = SCREEN_WIDTH # Adicionei a posição x para a movimentação da nuvem;
        self.y_pos_clound1 = 5 # Adicionei a posição y para a movimentação da nuvem;
        self.x_pos_clound2 = SCREEN_WIDTH + 900 # Adicionei a posição x para a movimentação da nuvem2;
        self.y_pos_clound2 = 20 # Adicionei a posição y para a movimentação da nuvem2;
        self.theme = 'light' # Adicionei para definir o tema inicial;
        self.bg_color = (219, 216, 188) # Adicionei essa variável para trocar a cor do fundo de acordo com o tema;
        self.font_color = (0, 0, 0) # Adicionei essa variável para trocar a cor da letra;
        self.theme_icon = THEME_ICON[1] # Adicionei para mudar a cor da imagem de alteração do tema;
        self.score_record = 0 # Adicionei essa variável para registrar o recorde de pontução;
        self.reset_button = pygame.Rect(-1,-1,0,0) # Iniciei o botão de resete;

        self.player = Dinosaur()
        self.obstacle_manager = Obstacle_Manager()
        self.power_up_manager = PowerUpManager()


    def execute(self):
        """
        Inicia o jogo.
        """
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()


    def run(self):
        """
        Inicia a corrida. Modified by Eugênio Jefferson.
        """
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0

        while self.playing:
            self.events()
            self.update()
            self.draw()

        if not self.playing: # Adicionei o delay aqui para suavizar a colisão;
            self.screen.blit(GAME_OVER, (SCREEN_WIDTH // 2 - GAME_OVER.get_width() // 2, SCREEN_HEIGHT // 2 - 240)) # Adicionei a imagem de game over;
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.event.clear() # Apaga eventos que estão na fila;
                


    def events(self):
        """
        Gerencia os eventos do usuário.
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False


    def update(self):
        """
        Atualiza as informações a cada loop. Modified by Eugênio Jefferson.
        """
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.theme) # Alterei para mudar a cor de acordo com o tema;
        self.obstacle_manager.update(self, self.theme) # Alterei para mudar a cor de acordo com o tema;
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)


    def update_score(self):
        """
        Gerencia a pontuação e velocidae do jogo. Modified by Eugênio Jefferson.
        """
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 3 # abaixei a velocidade do jogo;
            SCORE_SOUND.play() # toca som quando a pontuação aumenta;
        
        if self.score > self.score_record: # Adicionei a verificação se o recorde foi batido, e salva o novo recorde;
            self.score_record = self.score


    def draw(self):
        """
        Desenha a tela.
        """
        self.clock.tick(FPS)
        self.screen.fill(self.bg_color) # Mudei a cor fixa para a variável;
        self.draw_background()
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        self.player.draw(self.screen) # Alterei a ordem para o Dino fica em cima do obstáculo
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        """
        Desenha o fundo. Modified by Eugênio Jefferson.
        """
        # Muda a cor do chão
        if self.theme == 'light':
            bg_image = BG[1]
            cloud_image = CLOUD[1]

        elif self.theme == 'dark':
            bg_image = BG[0]
            cloud_image = CLOUD[0]

        image_width = bg_image.get_width()
        self.screen.blit(bg_image, (self.x_pos_bg, self.y_pos_bg)) # Alterei para se adaptar ao tema;
        self.screen.blit(bg_image, (image_width + self.x_pos_bg, self.y_pos_bg)) # Alterei como estava passando a posição, de '(image_width, self.x_pos_bg, self.y_pos_bg)' para '(image_width + self.x_pos_bg, self.y_pos_bg)'
        self.screen.blit(cloud_image, (self.x_pos_clound1, self.y_pos_clound1)) # Coloquei para inserir a nuvem na tela;
        self.screen.blit(cloud_image, (self.x_pos_clound2, self.y_pos_clound2)) # Coloquei para inserir a nuvem 2 na tela;
        
        if self.x_pos_bg >= -image_width: # Mudei de '<=' para '>=' para o fundo se movimentar
            self.screen.blit(bg_image, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg -= self.game_speed
            self.x_pos_clound1 -= self.game_speed # Adicionei para a nuvem se mover
            self.x_pos_clound2 -= self.game_speed # Adicionei para a nuvem 2 se mover
        
        else: # Adicionei essa verificação para voltar as posições iniciais das imagens de fundo para continuarem se movimentando.
            self.x_pos_bg = 0
            self.x_pos_clound1 = SCREEN_WIDTH
            self.y_pos_clound1 = random.randint(5, 60) # Cria a altura aleatória da nuvem.
            self.x_pos_clound2 = SCREEN_WIDTH + 900
            self.y_pos_clound2 = random.randint(5, 60) # Cria a altura aleatória da nuvem.

            

    def draw_score(self):
        """
        Desenha o componente do score na tela. Modified by Eugênio Jefferson.
        """
        draw_message_component(
            f"Pontuação: {self.score}",
            self.screen,
            pos_x_center = 950, # Alterei a posição.
            pos_y_center = 30, # Alterei a posição.
            font_color= self.font_color
        )

        if self.death_count > 0: # Inseri o recorde se o Dino tiver mais de uma morte;
            draw_message_component(f"Recorde: {self.score_record}", self.screen, pos_x_center= 964, pos_y_center= 58, font_color= (67, 67, 67) if self.theme == 'light' else (180, 180, 180))



    def draw_power_up_time(self):
        """
        Inseri a informação da duração do poder.
        """
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_timing - pygame.time.get_ticks()) / 1000, 2)
            
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} disponivel por {time_to_show} segundos",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40,
                    font_color= self.font_color
                )

            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE


    def handle_events_on_menu(self):
        """
        Gerencia os eventos que ocorrem no menu. Modified by Eugênio Jefferson.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_mods() & pygame.KMOD_CTRL: # Verifica se CTRL + T foi pressionado e muda o tema;
                    if event.key == pygame.K_t:
                        self.change_theme()

                else:
                    self.run()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.BUTTON_LEFT:
                if self.reset_button.collidepoint(event.pos):
                    self.run()


    def show_menu(self):
        """
        Mostra menu de inicio ou de morte. Modified by Eugênio Jefferson.
        """
        self.screen.fill(self.bg_color)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count == 0:
            self.screen.blit(DINO_RUNNER, (half_screen_width - DINO_RUNNER.get_width() // 2, half_screen_height - 200)) # Adicionei a imagem de título;

            draw_message_component("Pressione qualquer tecla para iniciar.", self.screen, font_color= self.font_color)

            # Adicionei instruções para o usuário poder alterar o tema.
            self.screen.blit(self.theme_icon, (SCREEN_WIDTH - 125, SCREEN_HEIGHT - 135))
            draw_message_component("Pressione 'CTRL + T'", self.screen, font_size=14, pos_x_center=SCREEN_WIDTH - 90, pos_y_center=SCREEN_HEIGHT - 50, font_color= self.font_color)
            draw_message_component("para alterar o tema.", self.screen, font_size=14, pos_x_center=SCREEN_WIDTH - 90, pos_y_center=SCREEN_HEIGHT - 30, font_color= self.font_color)

            # 1 - Instruções de jogo
            self.screen.blit(ARROW_KEY, (28, SCREEN_HEIGHT - 136))
            draw_message_component("Use as setas para", self.screen, font_size=14, pos_x_center=78, pos_y_center=SCREEN_HEIGHT - 50, font_color= self.font_color)
            draw_message_component("cima e para baixo.", self.screen, font_size=14, pos_x_center=78.5, pos_y_center=SCREEN_HEIGHT - 30, font_color= self.font_color)
            # Fim 1
            draw_message_component("By Eugênio Jefferson", self.screen, font_size=13, pos_y_center=SCREEN_HEIGHT - 12, font_color= self.font_color) # Inseri minha marca d'água
        else:
            draw_message_component("Pressione qualquer tecla para reiniciar.", self.screen, pos_y_center= half_screen_height + 100, font_color= self.font_color)
            draw_message_component(
                f"Sua pontuação: {self.score}",
                self.screen,
                pos_y_center= half_screen_height - 50,
                font_color= self.font_color
            )
            draw_message_component(f"Recorde: {self.score_record}", self.screen, pos_y_center= half_screen_height - 90, font_color= self.font_color) # Adicionei o recorde
            draw_message_component(
                f"Contagem de mortes: {self.death_count}",
                self.screen,
                pos_y_center= half_screen_height - 130,
                font_color= self.font_color
            )

            reset_image = RESET[1] if self.theme == 'light' else RESET[0] # escolhe a cor da imagem de resete de acordo com o tema;
            self.reset_button = self.screen.blit(reset_image, (half_screen_width - reset_image.get_width() // 2, half_screen_height + 140)) # Adicionei o botão de reset;
            self.screen.blit(GAME_OVER, (half_screen_width - GAME_OVER.get_width() // 2, half_screen_height - 240)) # Adicionei a imagem de game over;
            self.screen.blit(ICON[1] if self.theme == 'light' else ICON[0], (half_screen_width - 40, half_screen_height - 30)) # Modifiquei para trocar a cor

            # Adicionei instruções para o usuário poder alterar o tema.
            self.screen.blit(self.theme_icon, (SCREEN_WIDTH - 125, SCREEN_HEIGHT - 135))
            draw_message_component("Pressione 'CTRL + T'", self.screen, font_size=14, pos_x_center=SCREEN_WIDTH - 90, pos_y_center=SCREEN_HEIGHT - 50, font_color= self.font_color)
            draw_message_component("para alterar o tema.", self.screen, font_size=14, pos_x_center=SCREEN_WIDTH - 90, pos_y_center=SCREEN_HEIGHT - 30, font_color= self.font_color)

            draw_message_component("By Eugênio Jefferson", self.screen, font_size=13, pos_y_center=SCREEN_HEIGHT - 12, font_color= self.font_color) # Inseri minha marca d'água


        pygame.display.flip()
        self.handle_events_on_menu()


    def change_theme(self):
        """
        Altera entre o tema claro e escuro. By Eugênio Jefferson.
        """
        if self.theme == 'light':
            self.theme = 'dark'
            self.bg_color = (45, 45, 45)
            self.font_color = (255, 255, 255)
            self.theme_icon = THEME_ICON[0]
        
        elif self.theme == 'dark':
            self.theme = 'light'
            self.bg_color = (219, 216, 188)
            self.font_color = (0, 0, 0)
            self.theme_icon = THEME_ICON[1]

           
            