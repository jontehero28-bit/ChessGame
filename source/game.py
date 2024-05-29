import pygame 

from const import *

class Game:
    
    def __init__(self):
        pass
    
    #show methods
    
    def show_background(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = [pygame.Color("dark green")]
                else:
                    color = [pygame.Color("beige")]
                    
                rect = (col * SQUARESIZE, row *SQUARESIZE, SQUARESIZE)
                
                #pygame.draw.rect()
                    