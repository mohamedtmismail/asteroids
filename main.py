import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.isColliding(player):
                print("Game over!")
                sys.exit()
                
        for obj in asteroids:
            for shot in shots:
                if obj.isColliding(shot):
                    shot.kill()
                    obj.split()
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
