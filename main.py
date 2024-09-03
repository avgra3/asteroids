import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION, INITIAL_SCORE
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
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

    score = INITIAL_SCORE

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        if pygame.font:
            font = pygame.font.Font(None, 64)
            text = font.render(f"Current score: {score}", True, "red")
            text_position = text.get_rect(centerx=screen.get_width() / 2, y=10)
            screen.blit(text, text_position)

        for drawn in drawable:
            drawn.draw(screen)

        for update in updateable:
            update.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.collisions(shot):
                    score += 1
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = pygame.time.Clock().tick(fps) / 1000


if __name__ == "__main__":
    main()
