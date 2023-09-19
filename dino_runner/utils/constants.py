import pygame
import os

# Global Constants
TITLE = "Dino Runner - By Eugênio Jefferson"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = [
    pygame.image.load(os.path.join(DIR, "Light DinoWallpaper.png")),
    pygame.image.load(os.path.join(DIR, "Dark DinoWallpaper.png"))
] # Adicionei a imagem escura;

RUNNING = [
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoRun1.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoRun2.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoRun1.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoRun2.png"))
] # Alterei por causa do tema;

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoRun1Shield.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoRun2.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoRun1Shield.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoRun2.png"))
] # Alterei por causa do tema;

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoRun2Hammer1.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoRun2Hammer1.png"))
] # Alterei por causa do tema;

JUMPING = [
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoJump.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoJump.png"))
] # Alterei por causa do tema;

JUMPING_SHIELD = [
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoJumpShield.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoJumpShield.png"))
] # Alterei por causa do tema;

JUMPING_HAMMER = [
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoJumpHammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoJumpHammer.png"))
] # Alterei por causa do tema;

DUCKING = [
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoDuck1.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoDuck2.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoDuck1.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoDuck2.png"))
] # Alterei por causa do tema;

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoDuck2.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoDuck2.png")),
] # Alterei por causa do tema;

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Light DinoDuck2Hammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/Dark DinoDuck2Hammer.png"))
] # Alterei por causa do tema;

SMALL_CACTUS = [
    pygame.image.load(os.path.join(DIR, "Cactus/Light SmallCactus1.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Light SmallCactus2.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Light SmallCactus3.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Dark SmallCactus1.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Dark SmallCactus2.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Dark SmallCactus3.png"))
] # Alterei por causa do tema;

LARGE_CACTUS = [
    pygame.image.load(os.path.join(DIR, "Cactus/Light LargeCactus1.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Light LargeCactus2.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Light LargeCactus3.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Dark LargeCactus1.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Dark LargeCactus2.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/Dark LargeCactus3.png"))
] # Alterei por causa do tema;

BIRD = [
    pygame.image.load(os.path.join(DIR, "Bird/Light Bird1.png")),
    pygame.image.load(os.path.join(DIR, "Bird/Light Bird2.png")),
    pygame.image.load(os.path.join(DIR, "Bird/Dark Bird1.png")),
    pygame.image.load(os.path.join(DIR, "Bird/Dark Bird2.png"))
] # Alterei por causa do tema;

CLOUD = [
    pygame.image.load(os.path.join(DIR, 'Other/Light Cloud.png')),
    pygame.image.load(os.path.join(DIR, 'Other/Dark Cloud.png'))
] # adicionei a do outro tema

SHIELD = pygame.image.load(os.path.join(DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(DIR, 'Other/hammer.png'))

BG = [
    pygame.image.load(os.path.join(DIR, 'Other/Light Track.png')),
    pygame.image.load(os.path.join(DIR, 'Other/Dark Track.png'))
] # Alterei para mudar de tema;

HEART = [
    pygame.image.load(os.path.join(DIR, 'Other/Black SmallHeart.png')),
    pygame.image.load(os.path.join(DIR, 'Other/Red SmallHeart.png')),
    pygame.image.load(os.path.join(DIR, 'Other/Red Heart.png'))
] # Adicionei mais imagens do coração

DEFAULT_TYPE = "default"
SHIELD_TYPE = "Escudo" # Traduzi
HAMMER_TYPE = "Martelo" # Adicionei o tipo do hammer;
HEART_TYPE = "Coração" # Adicionei o tipo do coração;

THEME_ICON = [
    pygame.image.load(os.path.join(DIR, 'Other/Light mode.png')),
    pygame.image.load(os.path.join(DIR, 'Other/Dark mode.png'))
] # Adicionei para pegar o icone do tema;

GAME_OVER = pygame.image.load(os.path.join(DIR, 'Other/GameOver.png')) # Adicione a constante da imagem de game over;

RESET = [
    pygame.image.load(os.path.join(DIR, 'Other/Light Reset.png')),
    pygame.image.load(os.path.join(DIR, 'Other/Dark Reset.png'))
] # Adicione para colocar imagem de acordo com o tema, no botão de resete;

DINO_DEAD = [
    pygame.image.load(os.path.join(DIR, 'Dino/Light DinoDead.png')),
    pygame.image.load(os.path.join(DIR, 'Dino/Dark DinoDead.png'))
] # Adicione para alterar a imagem do Dino quando ele morre;

DUCKING_DEAD = [
    pygame.image.load(os.path.join(DIR, 'Dino/Light Dead DinoDuck.png')),
    pygame.image.load(os.path.join(DIR, 'Dino/Dark Dead DinoDuck.png'))
] # Adicionei para alterar a imagem do Dino quando ele morre abaixado;

pygame.mixer.init() # Iniciar o tocador de som;

JUMP_SOUND = pygame.mixer.Sound(os.path.join(DIR, 'Sounds/Jump.wav')) # Adicionei para carregar o arquivo de som do pulo;
JUMP_SOUND.set_volume(0.3) # Aumenta o volume;

DEATH_SOUND = pygame.mixer.Sound(os.path.join(DIR, 'Sounds/Death.wav')) # Adicionei para carregar o arquivo de som de morte;
DEATH_SOUND.set_volume(1) # Aumenta o volume;

SCORE_SOUND = pygame.mixer.Sound(os.path.join(DIR, 'Sounds/Score.wav')) # Adicionei para carregar o arquivo de som de quando a pontuação aumenta;
SCORE_SOUND.set_volume(0.2) # Aumenta o volume;

ARROW_KEY = pygame.image.load(os.path.join(DIR, 'Other/Arrow Keys.png')) # Imagem de setas para jogar;

DINO_RUNNER = pygame.image.load(os.path.join(DIR, 'Other/Dino Runner.png')) # Imagem de título do jogo;
