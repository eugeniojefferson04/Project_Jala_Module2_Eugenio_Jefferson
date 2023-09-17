import pygame
import os

# Global Constants
TITLE = "Dino Runner - By Eugênio Jefferson"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = [
    pygame.image.load(os.path.join(IMG_DIR, "Light DinoWallpaper.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dark DinoWallpaper.png"))
] # Adicionei a imagem escura;

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoRun2.png"))
] # Alterei por causa do tema;

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoRun2.png"))
] # Alterei por causa do tema;

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoRun2.png")),
]

JUMPING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoJump.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoJump.png"))
] # Alterei por causa do tema;

JUMPING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoJumpShield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoJumpShield.png"))
] # Alterei por causa do tema;

JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoDuck2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoDuck2.png"))
] # Alterei por causa do tema;

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Light DinoDuck2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoDuck2.png")),
] # Alterei por causa do tema;

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Dark DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Light SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Light SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Light SmallCactus3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Dark SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Dark SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Dark SmallCactus3.png"))
] # Alterei por causa do tema;

LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Light LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Light LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Light LargeCactus3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Dark LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Dark LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Dark LargeCactus3.png"))
] # Alterei por causa do tema;

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Light Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Light Bird2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Dark Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Dark Bird2.png"))
] # Alterei por causa do tema;

CLOUD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Light Cloud.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Dark Cloud.png'))
] # adicionei a do outro tema

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Light Track.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Dark Track.png'))
] # Alterei para mudar de tema;

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "Escudo" # Traduzi

THEME_ICON = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Light mode.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Dark mode.png'))
] # Adicionei para pegar o icone do tema;

