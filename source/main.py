import pygame
import sys      #nice to use to quit the application

from const import *   #gives access to everything inside const file.
from game import Game

class Main:
    
    def __init__(self):  #__init__ method is always called first.
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption("Chess")
        self.game = Game()
    
    def mainLoop(self):
        
        while True:
            self.game.show_background(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
            pygame.display.update()
            
    
main = Main() #instance of the main class
game = Game()
main.mainLoop()