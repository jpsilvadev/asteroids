import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # if small asteroid -> don't spawn new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # used for splitting new asteroids in different directions
        random_angle = random.uniform(20, 50)
        new_direction_pos = self.velocity.rotate(random_angle)
        new_direction_neg = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        pos_asteroid = Asteroid(*self.position, new_radius)
        neg_asteroid = Asteroid(*self.position, new_radius)
        pos_asteroid.velocity = new_direction_pos * 1.2
        neg_asteroid.velocity = new_direction_neg * 1.2
