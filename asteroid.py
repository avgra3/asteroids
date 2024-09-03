from circleshape import CircleShape
from pygame import draw


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        width = 2
        draw.circle(screen, color="white",
                    center=self.position, radius=self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
