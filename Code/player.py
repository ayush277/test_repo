import pygame



pygame.init()  # Initializing pygame.
screen = pygame.display.set_mode((400, 400))

def isCollsion(obj1, obj2):
        collide_result = obj1.colliderect(obj2)
        if collide_result :
            print('2222')


pygame.display.set_caption("Space Invaders")
x_rect1 = 400
while True:
    screen.fill((30, 30, 30))  # Set the Backgroud Color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    


    rect1 = pygame.Rect((x_rect1 ,100, 100, 100))
    rect2 = pygame.Rect(0, 100, 100, 100)


    pygame.draw.rect(screen, (40,60,80), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)

    x_rect1 -= 0.02
    isCollsion(rect1, rect2)
    pygame.display.update()