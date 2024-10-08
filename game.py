import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()  # initialize pygame

        pygame.display.set_caption('ninja game')  # window title
        self.screen = pygame.display.set_mode((640, 480))  # make the window with a set resolution

        self.clock = pygame.time.Clock()  # initiate a clock

        self.img = pygame.image.load('platformer game/data/images/clouds/cloud_1.png')  # load the image
        self.img.set_colorkey((0, 0, 0))  # set the transparent color key

        self.img_pos = [160, 260]  # initial image position
        self.movement = [False, False]  # movement flags for up/down

        self.collision_area = pygame.Rect(50, 50, 300, 50)  # rectangle for collision area

    def run(self):
        while True:  # game runs in a continuous infinite loop
            self.screen.fill((14, 219, 248))  # fill the screen with a background color

            # Move the image based on key inputs
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5

            # Draw the image at its new position
            self.screen.blit(self.img, self.img_pos)

            # Create a rect for the image to detect collisions
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())

            # Check for collision with the predefined area
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 155), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # event for exiting the application
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()  # update the display
            self.clock.tick(60)  # maintain a framerate of 60 FPS


Game().run()  # start the game
