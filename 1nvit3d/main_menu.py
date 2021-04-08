import pygame, sys, os
from commands import commands
from game import game
from tutorial import tutorial
pygame.init()

FONT = pygame.font.Font(os.path.join('Assets', 'Pixeboy.ttf'), 80)


WIDTH = 800
HEIGHT = 800
BLACK = (0, 0, 0)
LIGHT_GREEN = (0, 120, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RECT_WIDTH = 400
RECT_HEIGHT = 70

BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'MatrixPhoto.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

WIN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('1nvit3d')
pygame.display.set_icon(pygame.image.load(os.path.join('Assets', 'robot.png')))

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def main():
    CLOCK = pygame.time.Clock()
    running = True
    while running:

        WIN.blit(BACKGROUND, (0, 0))
        placeholder_surface = FONT.render('1nvit3d', True, BLACK).convert_alpha()
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(100, 251, RECT_WIDTH, RECT_HEIGHT)
        button_2 = pygame.Rect(100, 322, RECT_WIDTH, RECT_HEIGHT)
        button_3 = pygame.Rect(100, 393, RECT_WIDTH, RECT_HEIGHT)
        button_4 = pygame.Rect(100, 464, RECT_WIDTH, RECT_HEIGHT)
        background_rect = pygame.Rect(50, 100, 700, 700)
        play_surface = FONT.render('Play', True, BLACK).convert_alpha()
        commands_surface = FONT.render('Commands', True, BLACK).convert_alpha()
        tutorial_surface = FONT.render('Tutorial', True, BLACK).convert_alpha()
        quit_surface = FONT.render('Quit', True, BLACK).convert_alpha()
        # Drawing the text
        draw_rect_alpha(WIN, (0, 0, 255, 170),(50, 50, 700, 700),)
        pygame.draw.rect(WIN, GREEN, button_1)
        pygame.draw.rect(WIN, GREEN, button_2)
        pygame.draw.rect(WIN, GREEN, button_3)
        pygame.draw.rect(WIN, GREEN, button_4)


        # If the cursor hovers over the button
        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(WIN, LIGHT_GREEN, button_1)  # Change the color of the rectangle
            if click:
                game()

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(WIN, LIGHT_GREEN, button_2) # Change the color of the rectangle
            if click:
                commands()

        if button_3.collidepoint((mx, my)):
            pygame.draw.rect(WIN, LIGHT_GREEN, button_3)  # Change the color of the rectangle
            if click:
                tutorial()

        if button_4.collidepoint((mx, my)):
            pygame.draw.rect(WIN, LIGHT_GREEN, button_4)  # Change the color of the rectangle
            if click:
                sys.exit()

        WIN.blit(play_surface, (156, 264))
        WIN.blit(commands_surface, (153, 330))
        WIN.blit(tutorial_surface, (153, 406))
        WIN.blit(quit_surface, (153, 475))
        WIN.blit(placeholder_surface, (110, 150))
        # Resetting the click variable
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # If the user pressed escape then close the program
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # If the user clicked set click to True
                if event.button == 1:
                    click = True
        # Updating the display
        pygame.display.update()
        CLOCK.tick(60)



if __name__ == '__main__':
    main()