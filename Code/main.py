import pygame #importing pygame library
from sys import exit # Importing 'sys' important for various functions 

player_x = 200
player_y = 350
player_x_change = 0
player_y_change = 0

def player(x, y):
    spaceship = pygame.image.load('space-invaders\Elements\player.png')
    screen.blit(spaceship, (x, y))

#standard input
pygame.init() # Initializing pygame.
icon = pygame.image.load('Elements\player.png')
pygame.display.set_icon(icon)
screen= pygame.display.set_mode((400,400))  # Setup display scrren parameters.
pygame.display.set_caption("Space Invaders") # Here we also set the clock function to set the framerate for the game so that the the game does'nt run too fast, or too slow.

# Assigning 'while loop' to keep the display window runnig.
#while True:
    # Here we import our functions and graphics for the game in sections.
    # Keep the game updated for it to run.
    #pygame.display.update()
    # Now if we run the code here we won't be able to close it as there is no player input and the while loop keeps the code running.

# However if we implement a for loop within the while loop in the manner below we can get an exit option to properly close the window.
while True:
    screen.fill((30,30,30)) #Set the Backgroud Color 

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()   # Here the 'X' button is already dedicated for closing the window
        #Player Control 
        if event.type == pygame.KEYDOWN: #whem key is pressed 
            if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
                player_x_change -= 0.2 
            elif pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
                player_y_change -= 0.2 
            elif pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
                player_y_change += 0.2 
            elif pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
                player_x_change += 0.2
        if event.type == pygame.KEYUP:
                player_x_change = 0
                player_y_change = 0
        

    player_x += player_x_change 
    player_y += player_y_change 
    player(player_x, player_y)
    pygame.display.update() 
