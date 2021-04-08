import pygame, sys, os
pygame.init()

WIDTH = 800
HEIGHT = 800

BLACK = (0, 0, 0)

FONT = pygame.font.Font(os.path.join('Assets', 'Pixeboy.ttf'), 80)
WIN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Tutorial')

text1 = FONT.render('Story', True, BLACK)
text2 = FONT.render('Objective', True, BLACK)
text3 = FONT.render('How to play?', True, BLACK)

tut1 = pygame.image.load(os.path.join('Assets', 'Tutorial1.PNG'))
tut2 = pygame.image.load(os.path.join('Assets', 'Tutorial2.PNG'))
tut3 = pygame.image.load(os.path.join('Assets', 'Tutorial3.PNG'))


def tutorial():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # If the user pressed escape then close the program
                    running = False

        WIN.fill((255, 255, 255))
        WIN.blit(text1, (10, 10))
        WIN.blit(tut1, (10, 60))
        WIN.blit(text2, (10, 250))
        WIN.blit(tut2, (10, 300))
        WIN.blit(text3, (10, 540))
        WIN.blit(tut3, (10, 600))
        pygame.display.update()

if __name__ == '__main__':
    tutorial()
