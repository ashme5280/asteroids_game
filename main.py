import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_SPEED
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    #Initiate the game and screen size
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #CH2 L4 Initialize clock and delta time (dt) before loop
    clock = pygame.time.Clock()
    dt = 0.0

    #CH3 L5 groups & containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    #CH3 L2 Instantiate a player object in center of screen; CH4 L1 Create Asteroid Field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        #CH2 L2
        log_state()
        for event in pygame.event.get():
            #CH2 L3 allowing the "x" to close the window; Otherwise you have to CTRL + C to quit
            if event.type == pygame.QUIT:
                return

        #CH3 L3 move player left and right using a & d keys; CH3 L5 use the player groups
        updatable.update(dt)

        #CH4 L2 Collisions
        for ast_obj in asteroids:
            if player.collides_with(ast_obj) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")

        #CH 3 L2 draw player after filling screen
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        #CH2 L4 Limits FPS to 60 and calculate delta time in seconds
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
