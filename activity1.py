import pygame
import random
screen_width, screen_height = 500, 400
movement_speed = 5
font_size = 72
pygame.init()
background_image = pygame.transform.scale(pygame.image.load("bg.jpg"), (screen_width, screen_height))
font = pygame.font.SysFont("Times New Roman", font_size)
class sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.color("dodgerblue"))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, xchange, ychange):
        self.rect.x = max(min(self.rect.x + xchange, screen_width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + ychange, screen_height - self.rect.height), 0)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("collision game")
all_sprites = pygame.sprite.Group()
sprite1 = sprite(pygame.color("black"), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, screen_width - sprite1.rect.width),
random.randint(0, screen_height - sprite1.rect.height)
all_sprites.add(sprite1)
sprite2 = sprite(pygame.color("red"), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, screen_width - sprite2.rect.width),
random.randint(0, screen_height - sprite2.rect.height)
all_sprites.add(sprite2)
running, won = True, False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key = pygame.K_x):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
