import pygame
import random
import os

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))


def write(text, x, y, size):
    font = pygame.font.SysFont("Arial", size)
    rend = font.render(text, True, (255, 100, 100))
    screen.blit(rend, (x, y))


class Pest:
    def __init__(self):
        self.x = random.randint(250, 500)  # distance from left edge
        self.y = random.randint(250, 500)  # distance from top edge
        self.vx = random.randint(-4, 4)  # horizontal movement
        self.vy = random.randint(-4, 4)  # vertical movement
        self.graphic = pygame.image.load(os.path.join('pest.png'))
        self.size = 20

    def draw(self):
        screen.blit(self.graphic, (self.x, self.y))

    def movement(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x <= 0 or self.x >= width - self.size:
            self.vx = self.vx * -1  # change direction in horizontal movement
        if self.y <= 0 or self.y >= height - self.size:
            self.vy = self.vy * -1  # change direction in vertical movement

    def collision(self, player):
        x_center = self.x + self.size / 2  # center of pest graphic on x axis
        y_center = self.y + self.size / 2  # center of pest graphic on y axis
        if player.collidepoint(x_center, y_center):
            font = pygame.font.SysFont("Arial", 20)
            caption = font.render('GAME OVER', True, (123, 213, 231))
            screen.blit(caption, (100, 130))
            global playing
            playing = False


pests = []
x_player = 300
y_player = 300
v = 20
player = pygame.Rect(x_player, y_player, 20, 20)

for i in range(15):  # number of pests in game
    pests.append(Pest())

points = 0

playing = True

while True:
    for event in pygame.event.get():  # event checking loop
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y_player - v > 0:
                    y_player = y_player - v
            if event.key == pygame.K_DOWN:
                if y_player + v < height - 20:
                    y_player = y_player + v
            if event.key == pygame.K_RIGHT:
                if x_player + v < width - 20:
                    x_player = x_player + v
            if event.key == pygame.K_LEFT:
                if x_player - v > 0:
                    x_player = x_player - v
            player = pygame.Rect(x_player, y_player, 20, 20)

    if playing:
        points += 1
        screen.fill((40, 110, 50))
        for i in pests:
            i.movement()
            i.draw()
            i.collision(player)
        font = pygame.font.SysFont("Arial", 20)
        caption = font.render(str(points), True, (123, 213, 231))
        screen.blit(caption, (30, 30))
        pygame.draw.rect(screen, (250, 20, 0), player, 0)
        pygame.display.update()
        pygame.time.wait(10)  # time to call out next move of pest
