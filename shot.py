from circleshape import CircleShape
from constants import SHOT_RADIUS
from pygame import draw


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        draw.circle(screen, color="white",
                    center=self.position, radius=self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
