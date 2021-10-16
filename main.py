import pygame
import random

from block import Block
from wall import Wall

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([320, 700])

running = True

# The current tetris block that is moving.
selected = False

time = 0
speed = 1
sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
floor = pygame.sprite.Group()

def create_arena():
    #left side
    for i in range(1):
        for a in range(36):
            walls.add(Block(20, 20, i * 20, a*20, (160, 160, 160), False))

    #bottom
    for i in range(1):
        for a in range(36):
            floor.add(Block(20, 20, a * 20, 690 + (i * 20), (160, 160, 160), False))

    for i in range(1):
        for a in range(36):
            walls.add(Block(20, 20, 320 + (i * 20), a * 20, (160, 160, 160), False))

def create_block(val):
    if val == 1:
        sprites.add(Block(20, 20, 100, 50, color, True))
        sprites.add(Block(20, 20, 120, 50, color, True))
        sprites.add(Block(20, 20, 100, 70, color, True))
        sprites.add(Block(20, 20, 120, 70, color, True))


create_arena()
while running:

    newx = 0
    newy = 2

    if selected is False:
        selected = True
        value = 1
        color = random.randint(1, 4)
        if color == 1:
            color = (255, 51, 51)
        elif color == 2:
            color = (255, 253, 51)
        elif color == 3:
            color = (51, 51, 255)
        elif color == 4:
            color = (0, 204, 0)
        create_block(value)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                # rotate block here
                x = 0
            elif event.key == pygame.K_a:
                newx = -20
            elif event.key == pygame.K_d:
                newx = 20

        elif event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0))

    for block in sprites:
        if block.get_status() == True:
            for bottom in floor:
                if block.rect.collidepoint(bottom.get_x(), bottom.get_y() - 20):

                    for i in sprites:
                        if i.get_status() == True:
                            i.finish()
                            selected = False

            for placed in sprites:
                if placed.get_status() == False:
                    if block.rect.collidepoint(placed.get_x(), placed.get_y() - 20):
                        for i in sprites:
                            if i.get_status() == True:
                                i.finish()
                                selected = False

    flag = True

    for block in sprites:
        if block.get_status() == True:
            if newx > 0:
                if (block.get_x() + newx) > 300:
                    flag = False
            elif newx < 0:
                if (block.get_x() - newx) < 60:
                    flag = False


    if flag == True:
        for block in sprites:
            if block.get_status():
                block.update(newx, 0)


    if time == 10:
        time = 0
        for block in sprites:
            if block.get_status() == True:
                block.update(0, 20)

    time+=1


    sprites.draw(screen)
    floor.draw(screen)
    walls.draw(screen)

    clock.tick(60)


    pygame.display.update()

pygame.quit()
