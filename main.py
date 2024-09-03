import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHOOT_SPEED
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt = 0
    fps = 60
    pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for drawn in drawable:
            drawn.draw(screen)

        for update in updateable:
            update.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.kill()
                    shot.kill()

        pygame.display.flip()
        dt = pygame.time.Clock().tick(fps) / 1000


if __name__ == "__main__":
    main()
