import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
 #Adding a line to change the file
 #    
    def draw(self,screen):
        #self.position was needed as the x and y don't exist by themselves, position is created in circleshape
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if  self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            split1 = pygame.Vector2(self.velocity).rotate(angle)
            split2 = pygame.Vector2(self.velocity).rotate(-angle)
            new_radii = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position[0],self.position[1],new_radii)
            ast1.velocity = split1*1.2
            ast2 = Asteroid(self.position[0],self.position[1],new_radii)
            ast2.velocity = split2*1.2