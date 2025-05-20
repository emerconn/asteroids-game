import pygame
from constants import *
from sprites.player import Player
from sprites.asteroid import Asteroid
from sprites.asteroidfield import AsteroidField
from sprites.shot import Shot


def create_sprite_groups():
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    return updatables, drawables, asteroids, shots


def create_sprites(updatables, drawables, asteroids, shots):
    # player
    Player.containers = (updatables, drawables)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # asteroids
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()  # must be declared

    # shots
    Shot.containers = (shots, updatables, drawables)

    return player


def fps_print(fps_print_timer, dt, clock):
    if fps_print_timer >= 1.0:
        print(f"fps: {round(clock.get_fps())}")
        fps_print_timer = 0
        return fps_print_timer
    else:
        fps_print_timer += dt
        return fps_print_timer


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    fps = SCREEN_FPS
    fps_print_timer = 0

    updatables, drawables, asteroids, shots = create_sprite_groups()
    player = create_sprites(updatables, drawables, asteroids, shots)

    running = True
    while running:
        running = handle_events()

        screen.fill("black")
        dt = clock.tick(fps) / 1000  # delta time in float seconds

        fps_print_timer = fps_print(fps_print_timer, dt, clock)

        for drawable in drawables:
            drawable.draw(screen)

        updatables.update(dt)

        # asteroid collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                player.kill()

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        player.shoot_timer(dt)  # constantly reduce shoot timer
        pygame.display.flip()  # update screen contents


if __name__ == "__main__":
    main()
