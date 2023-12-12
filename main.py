#You can just copy the code below and paste it into your main.py file
#Its writen using python OOP 

#----------------------------------------------------------------
#        ||
#        ||
#        ||
#       \\//
#        {}
#----------------------------------------------------------------

import pygame,sys

class game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("In production")
        self.display = pygame.Surface((400, 300))
        self.clock = pygame.time.Clock()
    def run(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.display.fill((255, 255, 255))

            self.screen.blit(pygame.transform.scale2x(self.display), (0, 0))
            pygame.display.flip()
            pygame.display.update()

game().run()
