from circleshape import pygame
from circleshape import CircleShape
import pygame
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_LIVES,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from shot import Shot
from pathlib import Path

ROCKET_SHIP_IMAGE = Path("assets/rocket.png").resolve()


class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.lives = PLAYER_LIVES
        self.image = pygame.image.load(ROCKET_SHIP_IMAGE)
        self.image_rect = self.image.get_rect()

    def rocket(self):
        rock = pygame.transform.rotate(self.image, -1 * self.rotation)
        return rock

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        width = 1
        triangle = self.triangle()
        poly = pygame.draw.polygon(
            screen, "purple", triangle, width=width)
        poly_size = (poly.width, poly.height)
        rocket = pygame.transform.scale(self.rocket(), poly_size)

        screen.blit(rocket, poly)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.timer <= 0:
            shot = Shot(self.position[0], self.position[1])
            shot.velocity = pygame.Vector2(0, 1).rotate(
                self.rotation) * PLAYER_SHOOT_SPEED
            shot.update(dt)
            self.timer = PLAYER_SHOOT_COOLDOWN

    def reset(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.position = pygame.Vector2(self.x, self.y)
        self.velocity = pygame.Vector2(0, self.y)
        self.lives -= 1
