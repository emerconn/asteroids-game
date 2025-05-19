import pygame
from constants import *
from player import Player


# groups
updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()

# sprites
Player.containers = (updatables, drawables)
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
player = Player(x, y)


def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    fps = 165
    fps_display_timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")  # fill entire screen black
        dt = clock.tick(fps) / 1000  # get delta time in float seconds

        # print fps every second
        fps_display_timer += dt
        if fps_display_timer >= 1.0:
            print(f"fps: {round(clock.get_fps())}")
            fps_display_timer = 0

        # draw all sprites
        for drawable in drawables:
            drawable.draw(screen)

        updatables.update(dt)  # update all sprits

        pygame.display.flip()  # update contents of entire screen


if __name__ == "__main__":
    main()
