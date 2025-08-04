import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import Shot
import sys

def main():
    pygame.init()
    print('Starting Asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField() 
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    dt = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for sprite in drawable:
            sprite.draw(screen)
        
        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            if player_ship.collision(asteroid):
                print("Game Over!")
                sys.exit()
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
