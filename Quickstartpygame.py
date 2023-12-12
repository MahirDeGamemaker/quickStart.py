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
        pygame.display.set_caption("quickStart.py")
        self.display = pygame.Surface((400, 300))

        #rectangle
        self.rect_pos = pygame.Rect(50, 50, 50, 50)
        self.rect_spd = 5

        self.clock = pygame.time.Clock()
    def run(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #exit event code
                if event.type == pygame.KEYDOWN: 
                       if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            #getting the input
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]or key[pygame.K_a]:
                self.rect_pos.x -= self.rect_spd
            if key[pygame.K_RIGHT]or key[pygame.K_d]:
                self.rect_pos.x += self.rect_spd
            if key[pygame.K_UP]or key[pygame.K_w]:
                self.rect_pos.y -= self.rect_spd
            if key[pygame.K_DOWN]or key[pygame.K_s]:
                self.rect_pos.y += self.rect_spd
            
            #drawing stuff to the screen
            self.display.fill((255, 255, 255))
            pygame.draw.rect(self.display, 'red', self.rect_pos)

            self.screen.blit(pygame.transform.scale2x(self.display), (0, 0))
            pygame.display.flip()
            pygame.display.update()

game().run()
