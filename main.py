import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from player import Player
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    #Initiate the game and screen size
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #CH2 L4 Initialize clock and delta time (dt) before loop
    clock = pygame.time.Clock()
    dt = 0.0
    #CH3 L2 Instantiate a player object in center of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        #CH2 L2
        log_state()
        for event in pygame.event.get():
            #CH2 L3 allowing the "x" to close the window
            # #Otherwise you have to CTRL + C to quit
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #CH 3 L2 draw player after filling screen
        player.draw(screen)
        pygame.display.flip()
        #CH2 L4 Limits FPS to 60 and calculate delta time in seconds
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
