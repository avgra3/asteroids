from circleshape import CircleShape
from pygame import draw
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        width = 2
        draw.circle(screen, color="white",
                    center=self.position, radius=self.radius, width=width)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Spawn new asteroids
        rand_angle = random.uniform(20, 50)

        new_asteroid_velocity_1 = self.velocity.rotate(rand_angle)
        new_asteroid_velocity_2 = self.velocity.rotate(rand_angle * -1)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)

        asteroid_1.velocity = new_asteroid_velocity_1 * 1.2
        asteroid_2.velocity = new_asteroid_velocity_2 * 1.2
