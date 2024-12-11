import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # initialize pygame and set screen size
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # prints in the terminal when the file is executed
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock() # create a clock object
    dt = 0 # Delta time (time between frames)

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable) # Adds all instances of the Player class to both groups
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # instantiate a Player object
    AsteroidField()

    # Game loop
    running = True
    while running:
        # checks if the user tries to exit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw game objects
        screen.fill("black", rect=None) # fills the screen black (game background)
        for object in updatable:
            object.update(dt) # updates game objects
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
            
        for object in drawable:
            object.draw(screen) # draws game objects

        dt = clock.tick(60)/1000 # Limit FPS to 60 and calculate delta time
        pygame.display.flip() # refreshes the screen

    pygame.quit()
        

if __name__ == "__main__":
    main()