import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_COLOR = (0, 0, 0)
FONT_SIZE = 22
FONT_STYLE = "freesansbold.ttf"


def draw_message_component(
    message,
    screen,
    font_color=FONT_COLOR,
    font_size=FONT_SIZE,
    pos_y_center=SCREEN_HEIGHT // 2,
    pos_x_center=SCREEN_WIDTH // 2
):
    """
    Inseri um coponente de mensagem na tela;
    :message - é a mensagem que será exibida na tela;
    :screen - é a tela onde aparecerá a imagem;
    :font_color - é a cor da fonte, que recebe da constante FONT_COLOR, que vem na cor preta por parão;
    :font_size - tamanho da fonte, recebe o valor da constante FONT_SIZE, por padrão tem valor 22;
    :pos_y_center - posição do componente no eixo y, por padrão aparece no centro;
    :pos_x_center - posição do componente no eixo x, por padrão aparece no centro;
    """
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)