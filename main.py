import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # player - asteroid collision detection
        for a in asteroids:
            if a.is_colliding(player):
                print("Game over!")
                return

        # asteroid - bullet collision detection
        for s in shots:
            for a in asteroids:
                if a.is_colliding(s):
                    a.split()
                    s.kill()

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        player.draw(screen)
        pygame.display.flip()

        # limit to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
