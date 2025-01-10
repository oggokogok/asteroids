import pygame
import shelve
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import shelve

def main():

    #initializing pygame, needed for following bits
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Arial',30)

    #creating the display area
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #creating score variable
    score = 0

    #creating highscore variable
    highscore = 0

    #Reading the file
    d = shelve.open('score.txt')
    highscore = d['score']
    d.close()

    #Creating groups which will be iterated on directly
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Adding items to the groups to be able to act upon them direction
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots,updatable,drawable)
    clock = pygame.time.Clock()
    player = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
    ast_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f'you scored {score} points')
                d = shelve.open('score.txt')
                d['score'] = highscore
                d.close()
                return
        #Call groups directly, not through player 
        for obj in updatable:
            obj.update(dt,score)
        
        for obj in asteroids:
            for bullet in shots:
                if obj.collision(bullet) == True:
                    score += 1
                    if score >= highscore:
                        highscore = score
                    obj.split()
                    bullet.kill()
            if obj.collision(player) == True:
                print('Game over!')
                print(f'you scored {score} points')
                d = shelve.open('score.txt')
                d['score'] = highscore
                d.close()
                return

        screen.fill("black")
        text_surface = my_font.render(f'SCORE: {score}', False, (255,255,255))
        screen.blit(text_surface,(0,0))
        high_surface = my_font.render(f'HIGH SCORE: {highscore}',False,'white')
        screen.blit(high_surface,(0,40))
        for obj in drawable:
            obj.draw(screen)
        #Remove the upper fill and turn this on to make an etch a sketch
        #screen.fill("black")

        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        #print(dt)
        
        
        
             


if __name__ == "__main__":
    main()
