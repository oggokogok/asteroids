import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #initializing pygame, needed for following bits
    pygame.init()

    #creating the display area
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
                return
        #Call groups directly, not through player 
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            for bullet in shots:
                if obj.collision(bullet) == True:
                    obj.kill()
                    bullet.kill()
            if obj.collision(player) == True:
                print('Game over!')
                return

        screen.fill("black")

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
