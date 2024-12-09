import pygame
from constants import *
from player import *
from circleshape import *

def main():
    # initialize pygame and set screen size
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # prints in the terminal when the file is executed
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # instantiate a Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # create a clock object and set it to "clock" variable
    clock = pygame.time.Clock()
    # initialize a value "delta time", which stores the value the .tick() method returns
    dt = 0
    # infinite game loop
    running = True
    while running:
        # checks if the user tries to exit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fills the screen black (game background)
        screen.fill("black", rect=None)
        # renders the player object to the screen
        player.draw(screen)
        # limits the FPS for the game and updates the dt variable
        dt = clock.tick(60)/1000
        # calls the player method to update player position
        player.update(dt)
        # refreshes the screen
        pygame.display.flip()
        

if __name__ == "__main__":
    main()