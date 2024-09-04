from circleshape import CircleShape
from pygame import draw, image, transform
from constants import ASTEROID_MIN_RADIUS
import random
from pathlib import Path

ASTEROID_IMAGE = Path("assets/asteroid.png")


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = image.load(ASTEROID_IMAGE)
        self.image_rect = self.image.get_rect()

    def asteroid(self):
        asteroid = self.image
        return asteroid

    def draw(self, screen):
        width = 1  # Was: 2
        circle = draw.circle(screen, color="white",
                             center=self.position, radius=self.radius, width=width)
        circle_size = (circle.width, circle.height)
        image = transform.scale(self.asteroid(), circle_size)
        screen.blit(image, circle)

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
