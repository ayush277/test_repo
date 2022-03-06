import pygame  # importing pygame library
import random
from sys import exit  # Importing 'sys' important for various functions


pygame.init()  
screen = pygame.display.set_mode((400, 400))
started = False

class Player:
    player_x = 170
    player_y = 350
    player_x_change = 0

    spaceship = pygame.image.load(
            'C:\Projects\Space Invaders\space-invaders\Elements\player.png')
    
    def player(x, y):
        screen.blit(Player.spaceship, (x, y))

    def line():
        rect1 = pygame.Rect((0 ,330 , 400, 200))
        pygame.draw.rect(screen, (40,40,40), rect1)

class Enemy:

    enemy_red = []
    enemy_x = []
    enemy_y = []
    enemy_x_change = []
    enemy_y_change = []
    number_of_enemies = 4

    for enemies in range(number_of_enemies):
        enemy_red.append(pygame.image.load(
            'C:\Projects\Space Invaders\space-invaders\Elements\enemy_red.png'))
        # locates the enemy on a random point between 60, 360
        enemy_x.append(random.randint(60, 360))
        # locates the enemy on a random point between 0, 200
        enemy_y.append(random.randint(32, 100))
        enemy_x_change.append(0.2)
        enemy_y_change.append(32)

    def enemy1(x, y, i):
        screen.blit(Enemy.enemy_red[i], (x, y))

class Laser:
    # locates the enemy on a random point between 60, 360
    laser_x = Player.player_x + 30
    laser_y = Player.player_y + 5  # locates the enemy on a random point between 0, 200
    laser_x_change = 0
    laser_y_change = 3
    laser_state = 'rest'
    laser = pygame.image.load(
        'C:\Projects\Space Invaders\space-invaders\Elements\laser_bullet.jpg')
    laser = pygame.transform.scale(laser, (4, 20))

    def laser_fire(x, y):
        global laser_state
        laser_state = 'fired'
        screen.blit(Laser.laser, (x, y))

class Score:
    score = 0
    font = pygame.font.Font('C:\Projects\Space Invaders\space-invaders\Fonts\VCR_OSD_MONO_1.001.ttf', 16)

    def show_score(x, y):
        score_count = Score.font.render('Score : ' + str(Score.score), True, (255,255,255))
        screen.blit(score_count, (x,y))

    def show_title(x, y):
        score_count = Score.font.render('Space Invaders', True, (255,255,255))
        screen.blit(score_count, (x,y))

class StartScreen:
    start = True
    font = pygame.font.Font(r'Fonts\upheavtt.ttf', 56)

    def show_start():   
        rect1 = pygame.Rect((0 ,0 , 400, 400))

        start_image = pygame.image.load("C:\Projects\Space Invaders\space-invaders\Elements\Space Invaders Start.png")
        start_image = pygame.transform.scale(start_image, (400,400))

        screen.blit(start_image, (0,0))
        
        while StartScreen.start:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        StartScreen.start = False
                        GameScreen.gameplay()

            pygame.display.update()

class GameScreen :
    def player_control():
        if event.type == pygame.KEYDOWN:  # whem key is pressed
            if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
                Player.player_x_change -= 0.5
            if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
                Player.player_x_change += 0.5
            if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
                Laser.laser_x = Player.player_x
                if Laser.laser_state == 'rest':
                    Laser.laser_state = 'fired'
                    Laser.laser_fire(Laser.laser_x, Laser.laser_y)

        if event.type == pygame.KEYUP:
            Player.player_x_change = 0

    def gameplay() :
        game_started = True
        rect1 = pygame.Rect((0 ,0 , 400, 400))
        pygame.draw.rect(screen, (30, 30, 30), rect1)

        Player.player_x += Player.player_x_change

        if Player.player_x < 0:  # adding boundary to the game
            Player.player_x = 0  # adding boundary to the game
        elif Player.player_x >= 340:  # adding boundary to the game
            Player.player_x = 340  # adding boundary to the game

        if Laser.laser_state == 'fired' :
            Laser.laser_fire(Laser.laser_x + 26, Laser.laser_y)
            Laser.laser_y -= Laser.laser_y_change

        if Laser.laser_y <= 0 :
            Laser.laser_y = Player.player_y
            Laser.laser_state = 'rest'

        laser_rect = Laser.laser.get_rect(center=(Laser.laser_x, Laser.laser_y))
        enemy_rect = []

        for i in range(Enemy.number_of_enemies): 
            Enemy.enemy_x[i] += Enemy.enemy_x_change[i]
            Enemy.enemy_y[i] = Enemy.enemy_y_change[i]
            
            if Enemy.enemy_x[i] < 0:
                Enemy.enemy_x_change[i] = 1
                Enemy.enemy_y_change[i] += 32 #to change the y position of alien, to make it come one row down if it touches walls
            if Enemy.enemy_x[i] >= 340:
                Enemy.enemy_x_change[i] = -1 
                Enemy.enemy_y_change[i] += 32 #to change the y position of alien, to make it come one row down if it touches walls
            
            if Enemy.enemy_y[i] >= 300 : #y boundary    
                GameOver.show_game_over()
                break
                    
            

            Enemy.enemy1(Enemy.enemy_x[i], Enemy.enemy_y[i], i) 
            enemy_rect.append(Enemy.enemy_red[i].get_rect(center=(Enemy.enemy_x[i], Enemy.enemy_y[i])))#implementing enemy function

            if laser_rect.colliderect(enemy_rect[i]):
                print(Score.score)
                Enemy.enemy_x[i] = 10 
                Enemy.enemy_y[i] = 60
                Enemy.enemy_y_change[i] = random.randint(32, 150)
                Score.score += 1
                Laser.laser_state = 'rest'
                Laser.laser_y = Player.player_y
            
                Laser.laser_fire(Player.player_x + 300, Player.player_y + 300)
        

        Player.line()
        Player.player(Player.player_x, Player.player_y)
        Score.show_score(10,10)
        Score.show_title(260,10)


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

        if event.type == pygame.KEYDOWN:  # whem key is pressed
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                Paused.pause = True
                Paused.paused()

class GameOver:
    font = pygame.font.Font('C:\Projects\Space Invaders\space-invaders\Fonts\VCR_OSD_MONO_1.001.ttf', 40)
    stopped = True

    def show_game_over():
        game_over = GameOver.font.render('GAME OVER', True, (255,255,255))
        game_over_rect = game_over.get_rect(center=(400/2, 400/2))
        end_score = Score.font.render('score : '+ str(Score.score), True, (255,255,255))
        rect1 = pygame.Rect((0 ,0 , 400, 400))
        pygame.draw.rect(screen, (40,40,40), rect1)
        screen.blit(game_over,game_over_rect)
        screen.blit(end_score, (150,230))
    
        while GameOver.stopped:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit() 
                        

            pygame.display.update()

def small_text(text) :
    Score.font.render(text, True, (255,255,255))

class Game:
    def game():
        StartScreen.show_start()
        GameScreen.gameplay()


clock = pygame.time.Clock()
while True:
    
    screen.fill((30, 30, 30))  # Set the Backgroud Color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        GameScreen.player_control()
        Paused.pause_control()  

    Game.game()
    clock.tick(3000)
    pygame.display.update()
