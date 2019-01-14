import pygame, sys

class mainApp():

    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244, 236, 203))
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def __on_render(self):
        pygame.display.flip()
    
    def maincycle(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()
            self.__on_render()
            
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.maincycle()


        
        