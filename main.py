import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH})")
    print(f"Screen height: {SCREEN_HEIGHT})")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    delta_time = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((2, 2, 2))
        pygame.display.flip()
        last_time = timer.tick(60)
        delta_time = last_time / 1000
        player.draw_player(screen)


if __name__ == "__main__":
    main()
