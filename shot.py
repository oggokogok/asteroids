import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self,screen):
        #self.position was needed as the x and y don't exist by themselves, position is created in circleshape
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += (self.velocity * dt)
        if self.position[0] <= 0:
            self.position = [SCREEN_WIDTH,self.position[1]]
        elif self.position[0] >= SCREEN_WIDTH:
            self.position = [0,self.position[1]]
        elif self.position[1] <= 0:
            self.position = [self.position[0],SCREEN_HEIGHT]
        elif self.position[1] >= SCREEN_HEIGHT:
            self.position = [self.position[0],0]