import pygame  # importing pygame library
import random
from sys import exit  # Importing 'sys' important for various functions

pygame.init()  

screen = pygame.display.set_mode((400, 400)) #showing the screen
started = False #declaring a variable to show the state of game

class Player: 
    speed = 0.5 #speed of the spaceship on press of button
    #initial x and y position of the player
    player_x = 170 #170 to keep it in center of screen as our spaceship is 60px wide
    player_y = 350 #setting y coordinate of spaceship
    player_x_change = 0

    #adding the spaceship image in code
    spaceship = pygame.image.load(
            'C:\Projects\Space Invaders\space-invaders\Elements\player.png')
    
    def player(x, y):
        screen.blit(Player.spaceship, (x, y)) #showing the image on screen

    def player_movement():
            Player.player_x += Player.player_x_change #this will increase or decrease (depending when the function is called) the x coordinate of position by continuosly adding 0.5 (speed variable) to it.

    def player_boundary():
        if Player.player_x < 0:  # adding boundary to the game
            Player.player_x = 0  # adding boundary to the game
        elif Player.player_x >= 340:  # adding boundary to the game
            Player.player_x = 340  # adding boundary to the game
        
    def line():
        rect1 = pygame.Rect((0 ,330 , 400, 200)) #making a rectangle the endline of the screen (0,330) : coordinates of top left corner of rectangle
                                    #(400,200) size of rectangle
        pygame.draw.rect(screen, (40,40,40), rect1) #dsiplaying the rectangle on 'screen' and color is (40,40,40)

class Enemy:

    enemy_speed = 0.2 #speed at which enemy moves
    enemy_fasten = 0.2 #speed at which enemy moves when it hit the wall

    enemy_red = [] #list to store enemy_images as there are multiple

    enemy_x = [] #list to store the x coordinates of enemy_image corresponding to the image stored in enemy_red list
    enemy_y = [] #list to store the y coordinates of enemy_image corresponding to the image stored in enemy_red list

    enemy_x_change = [] #list to store the change in x coordinates of enemy_image corresponding to the image stored in enemy_red list
    enemy_y_change = [] #list to store the change in y coordinates of enemy_image corresponding to the image stored in enemy_red list

    number_of_enemies = 4 #number of enemies

    #making/adding the enemies in game
    for enemies in range(number_of_enemies):
        #adding the enemies to the list enemy_red
        enemy_red.append(pygame.image.load(
            'C:\Projects\Space Invaders\space-invaders\Elements\enemy_red.png')) 
        # locates the enemy on a random point between 0, 360
        enemy_x.append(random.randint(0, 360))
        # locates the enemy on a random point between 32, 64
        enemy_y.append(random.randint(32, 64))
        #adding enemy to the corresponding list so that each sprite moves individually at its own speed
        enemy_x_change.append(enemy_speed)
        enemy_y_change.append(32) #change in y coordinate, it is 32 because the heigth of enemy is 32px. As we want the enemy to move to next row on hitting wall, we kept the change to 32


    def enemy1(x,y,i):
        #showing enemies on screen
        #here x and y are the variable coordinates
        #and i is a variable which will be used in a future loop 
        screen.blit(Enemy.enemy_red[i], (x,y))

class Laser:
    laser_x = Player.player_x + 30 #spaceship initial posn + 30
    laser_y = Player.player_y + 5  #spaceship initial posn + 5
    laser_x_change = 0
    laser_y_change = 1
    laser_state = 'rest'
    #addiing and resizing laser image 
    laser = pygame.image.load(
        'C:\Projects\Space Invaders\space-invaders\Elements\laser_bullet.jpg')
    laser = pygame.transform.scale(laser, (4, 20))

    def laser_fire(x, y):
        global laser_state #this is same laser state shown in laser.py
        laser_state = 'fired' #changing the state, will change the value to 'fired' when this function is called
        screen.blit(Laser.laser, (x, y)) #displaying image on screen when function is called

    def laserstate():
        #when this function is called
        if Laser.laser_state == 'fired' : #it will check the state of laser, if it is fired then
            #it will display the laser and change its coordinate by 'laser_y_change' value, so that it appears that laser is moving upwards. 
            Laser.laser_fire(Laser.laser_x + 26, Laser.laser_y)  
            Laser.laser_y -= Laser.laser_y_change

    def laser_boundary():
        #this function will reset the state of the laser once it is out of window, so that we can shoot the laser again
        if Laser.laser_y <= 0 :  #if the coordinate of laser goes out of screen then
            Laser.laser_y = Player.player_y #reset the y coordinate of the laser to the y coordinate of player (spaceship)
            Laser.laser_state = 'rest' #and change the laser state to rest so that we can fire it again

class Controls:
    def player_control():
        #this function has the controls of player
        if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
            Player.player_x_change -= Player.speed #will decrease the x coordinate by 'speed' (0.5px) so that it can move to left
        if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
            Player.player_x_change += Player.speed #will increase the x coordinate by 'speed' (0.5px) so that it can move to right
        #laser will fire when upper arrow is pressed
        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
            Laser.laser_x = Player.player_x
            if Laser.laser_state == 'rest': #checking if laser state is in rest state 
                #this condition above is important becase, without it if we accidentally clicked the up_arrow, the position of laser will reset to spaceship position
                #and it will refire from the spaceship position
                Laser.laser_state = 'fired' #so that it can be changes to fire state
                Laser.laser_fire(Laser.laser_x, Laser.laser_y) #and can be fired from the position of the spaceship (laser_x and laser_y are equals to spaceship position)

class Score:
    score = 0 #keeping the track of score which will increase upon collision
    #declaring the font used. 
    font = pygame.font.Font('C:\Projects\Space Invaders\space-invaders\Fonts\VCR_OSD_MONO_1.001.ttf', 16)

    def show_score(x, y): #to display the score count using blit()
        score_count = Score.font.render('Score : ' + str(Score.score), True, (255,255,255))
        screen.blit(score_count, (x,y))

    def show_title(x, y): #to show 'space invaders title' using (blit)
        score_count = Score.font.render('Space Invaders', True, (255,255,255))
        screen.blit(score_count, (x,y)) 

class StartScreen:
    start = True #variable to store the state of start window, if its true that means start window is displayed on screen. If false, then its not.
    font = pygame.font.Font(r'Fonts\upheavtt.ttf', 56) #declaring the font

    def start_screen():   
        #adding and displaying (blit function) the start image on screen.
        start_image = pygame.image.load("C:\Projects\Space Invaders\space-invaders\Elements\Space Invaders Start.png")
        start_image = pygame.transform.scale(start_image, (400,400)) #resizing the screen so that it fits the window

        screen.blit(start_image, (0,0))
    
    def show_start():
        while StartScreen.start: #while the start variable in StartScreen class is True (it becomes true when the function is called)
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN :#checks if SPACE key is pressed
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        StartScreen.start = False #sets the start variable to false, hence start screen is closed 
            
            StartScreen.start_screen() #calling the start_screen function to display the intro image
            pygame.display.update()

class Collision:
    def collision():
        laser_rect = Laser.laser.get_rect(center=(Laser.laser_x, Laser.laser_y)) #getting rectangle of size and width of laser image, and mapping it to position of laser
        enemy_rect = [] #making an empty list to store the rectangles we will get of the enemy images stored in enemy_rect list

        for i in range(Enemy.number_of_enemies):  #iterating over enemies
            Enemy.enemy_x[i] += Enemy.enemy_x_change[i] #this will constantly change the enemy's (at index 'i' in the enemy_rect list) x coordinate by enemy_x_change
            Enemy.enemy_y[i] = Enemy.enemy_y_change[i] #this will constantly change the enemy's (at index 'i' in the enemy_rect list) y coordinate by enemy_x_change
            
            #this is enemy boundary, if enemy at say index 'i' hits the wall ie goes outside the window it will be reset to a new coordinate as per the code
            if Enemy.enemy_x[i] < 0: #if enemy at index 'i' hits the left wall
                Enemy.enemy_x_change[i] = Enemy.enemy_fasten #change the speed of enemy and hence its coordinates by logic mentioned earlier
                Enemy.enemy_y_change[i] += 32 #to change the y position of alien, to make it come one row down if it touches walls
            if Enemy.enemy_x[i] >= 340: #if enemy at index 'i' hits the right wall
                Enemy.enemy_x_change[i] = -Enemy.enemy_fasten #change the speed of enemy and hence its coordinates by logic mentioned earlier
                Enemy.enemy_y_change[i] += 32 #to change the y position of alien, to make it come one row down if it touches walls
            
            if Enemy.enemy_y[i] >= 300 : #if player hits the y boundary that is 300  
                GameOver.show_game_over()  #game over screen will be displayed
                break
                    
            Enemy.enemy1(Enemy.enemy_x[i], Enemy.enemy_y[i], i) #showing the enemies on screen

            #now we will add the rectangles of enemy at index i to the enemy_rect list.
            enemy_rect.append(Enemy.enemy_red[i].get_rect(center=(Enemy.enemy_x[i], Enemy.enemy_y[i]))) 

            if laser_rect.colliderect(enemy_rect[i]): #colliderect is an inbuilt function which will return True if the two given rectangles collide each other
                print(Score.score)
                Enemy.enemy_x[i] = 10  #set the enemy's x coordinate to 10
                Enemy.enemy_y[i] = 60  #set the enemy's y coordinate to 60
                Enemy.enemy_y_change[i] = random.randint(32, 150) #set the enemy_y_change to any random int between 32 and 150 so that the y coordinate of that specific enemy is changed.
                Score.score += 1 #increase the score by 1 
                Laser.laser_state = 'rest' #change the state of laser to rest so that it can be fired again
                Laser.laser_y = Player.player_y #change the y coordinate of laser to player's y coordinate. 
            
                Laser.laser_fire(Player.player_x + 300, Player.player_y + 300) #make the laser dissapear once it hits the spaceship

class GameScreen :
    def gameplay():

        Player.player_movement() #adding the movement logic of player
        Player.player_boundary() #adding the boundary by calling the Boundary() function from Player Class

        Laser.laserstate() #checking the state of the laser by calling the laserstate() function from Laser Class
        Laser.laser_boundary() #adding the condition to check if laser is outside the window or not by calling laser_boundary() function from Laser Class
        
        Collision.collision() #checking for collision of enemy and bullet calling collision() function from Collision class

        Player.line() #displaying the end line by calling line function from Player class
        Player.player(Player.player_x, Player.player_y) #displaying spaceship by calling player function from Player class

        Score.show_score(10,10) #displaying the score by calling show_score function from Score class. (10,10) is the position.
        Score.show_title(260,10) #displaying the title by calling show_title func from Score Class. (260, 10) is the position.

class Paused :
    pause = True

    def paused():
        paused = GameOver.font.render('PAUSED', True, (255,255,255))
        paused_rect = paused.get_rect(center=(400/2, 400/2))
        end_score = Score.font.render('score : '+ str(Score.score), True, (255,255,255))
        rect1 = pygame.Rect((0 ,0 , 400, 400))
        pygame.draw.rect(screen, (40,40,40), rect1)
        screen.blit(paused, paused_rect)
        screen.blit(end_score, (150,230))
    
        while Paused.pause:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:  # whem key is pressed
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        Paused.pause = False
                        GameScreen.gameplay()

            pygame.display.update()

    def pause_control():

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                Paused.pause = True
                Paused.paused()

class GameOver:
    font = pygame.font.Font('C:\Projects\Space Invaders\space-invaders\Fonts\VCR_OSD_MONO_1.001.ttf', 40)
    stopped = True

    def gameover():
        game_over = GameOver.font.render('GAME OVER', True, (255,255,255))
        game_over_rect = game_over.get_rect(center=(400/2, 400/2))
        end_score = Score.font.render('score : '+ str(Score.score), True, (255,255,255))
        rect1 = pygame.Rect((0 ,0 , 400, 400))
        pygame.draw.rect(screen, (40,40,40), rect1)
        screen.blit(game_over,game_over_rect)
        screen.blit(end_score, (150,230))
    
    def show_game_over():
        while GameOver.stopped:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit() 
                        
            GameOver.gameover()
            pygame.display.update()

def small_text(text) :
    Score.font.render(text, True, (255,255,255))

def main():
    clock = pygame.time.Clock()
    while True:
        
        screen.fill((30, 30, 30))  # Set the Backgroud Color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
            if event.type == pygame.KEYDOWN:  # whem key is pressed
                Controls.player_control()
                Paused.pause_control()  
            if event.type == pygame.KEYUP:
                Player.player_x_change = 0

        
        StartScreen.show_start()
        GameScreen.gameplay()
        clock.tick(3000)
        pygame.display.update()

main()