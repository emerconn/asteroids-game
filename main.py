import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


# sprite groups
updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

# player sprite
Player.containers = (updatables, drawables)
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
player = Player(x, y)

# asteroid sprites
Asteroid.containers = (asteroids, updatables, drawables)
AsteroidField.containers = updatables
asteroid_field = AsteroidField()

# shot sprites
Shot.containers = (shots, updatables, drawables)


def fps_print(fps_display_timer, dt, clock):
    if fps_display_timer >= 1.0:
        print(f"fps: {round(clock.get_fps())}")
        fps_display_timer = 0
        return fps_display_timer
    else:
        fps_display_timer += dt
        return fps_display_timer


def main():
    fps = SCREEN_FPS
    fps_display_timer = 0
    dt = 0
    game_over = False

    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")  # fill entire screen black
        dt = clock.tick(fps) / 1000  # get delta time in float seconds

        # print fps every second
        fps_display_timer = fps_print(fps_display_timer, dt, clock)

        # draw all sprites
        for drawable in drawables:
            drawable.draw(screen)

        updatables.update(dt)  # update all sprits

        # check for asteroid collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                player.kill()

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        player.shoot_timer(dt)  # constantly reduce shoot timer

        pygame.display.flip()  # update contents of entire screen


if __name__ == "__main__":
    main()
