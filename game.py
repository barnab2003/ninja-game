import pygame
import sys

class Game:
    def __init__(self):
        pygame.init() #initialise pygame

        pygame.display.set_caption('ninja game') #window title
        self.screen = pygame.display.set_mode((640, 480)) #makes the window and resolution

        self.clock = pygame.time.Clock() #initiate a clock

        self.img = pygame.image.load('platformer game/data/images/clouds/cloud_1.png') #load the image

    def run(self):
        while True:  #game runs a continouse infinite loop
                self.screen.blit(self.img,(100, 200)) #location of image
                                                      #top left is (0,0)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: #event for exit the application
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
                self.clock.tick(60)

Game().run()                

