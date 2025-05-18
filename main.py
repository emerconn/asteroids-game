import pygame
from constants import *

def main():
	print(f"Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	fps = 60
	counter = 0
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")  # fill entire screen black
		pygame.display.flip()  # update contents of entire screen

		clock.tick(fps)
		dt /= 1000
		counter += 1
		if counter == fps:
			print(f"fps: {clock.get_fps()}")
			counter = 0


if __name__ == "__main__":
	main()
