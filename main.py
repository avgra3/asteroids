import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION, INITIAL_SCORE
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
from pathlib import Path

EXPLOSION_SOUND = Path("assets/explosion.mp3").resolve()
SPACE_BACKGROUND = Path("assets/space.jpg").resolve()

def play_explosion():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(EXPLOSION_SOUND)
        pygame.mixer.music.play()
    except pygame.error:
        print("Sound was unable to play: No such audio device!")


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

        # screen.fill("black")
        background = pygame.image.load(SPACE_BACKGROUND)
        screen.blit(background, (0, 0))

        if pygame.font:
            font = pygame.font.Font(None, 64)
            text = font.render(f"Current score: {score}", True, "red")
            text_position = text.get_rect(centerx=screen.get_width() / 2, y=10)
            screen.blit(text, text_position)
            # Show remaining player lives
        if pygame.font:
            font = pygame.font.Font(None, 32)
            lives_text = font.render(
                f"Lives left: {player.lives}", True, "red")
            lives_text_position = lives_text.get_rect(
                centerx=screen.get_width() / 2,
                y=SCREEN_HEIGHT - 40,
            )
            screen.blit(lives_text, lives_text_position)

        for drawn in drawable:
            drawn.draw(screen)

        for update in updateable:
            update.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
               # play_explosion()
                if player.lives <= 0:
                    sys.exit("Game over!")
                player.reset()
            for shot in shots:
                if asteroid.collisions(shot):
                   # play_explosion()
                    score += 1
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = pygame.time.Clock().tick(fps) / 1000


if __name__ == "__main__":
    main()
