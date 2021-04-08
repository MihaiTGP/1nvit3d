import pygame, sys, os
pygame.init()

move_commands = ['up', 'down', 'left', 'right']
teleport_commands = ['up up', 'down down', 'left left', 'right right']

FONT = pygame.font.Font(os.path.join('Assets', 'Pixeboy.ttf'), 55)
BIG_FONT = pygame.font.Font(os.path.join('Assets', 'Pixeboy.ttf'), 80)

SMALL_RECT_WIDTH = 120
RECT_WIDTH = 220
RECT_HEIGHT = 40

WIDTH = 800
HEIGHT = 800
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Commands')

def draw_commands(move, tp):
    title_surface = BIG_FONT.render('Commands', True, BLACK)
    WIN.blit(title_surface, (220, 100))

    mox = 80
    moy = 200
    mex = 500
    mey = 200
    for command in move:
        command_surface = FONT.render(command, True, BLACK)
        WIN.blit(command_surface, (mox, moy))
        moy += 100

    for command in tp:
        command_surface = FONT.render(command, True, BLACK)
        WIN.blit(command_surface, (mex, mey))
        mey += 100




def draw_command(command):
    title_surface = BIG_FONT.render(command, True, BLACK)


    definitions = {'up': pygame.image.load(os.path.join('Assets', 'Def1.PNG')),
                   'down'  :pygame.image.load(os.path.join('Assets', 'Def2.PNG')),
                   'left': pygame.image.load(os.path.join('Assets', 'Def3.PNG')),
                   'right': pygame.image.load(os.path.join('Assets', 'Def4.PNG')),
                   'up up':pygame.image.load(os.path.join('Assets', 'Def5.PNG')),
                   'down down': pygame.image.load(os.path.join('Assets', 'Def6.PNG')),
                   'left left': pygame.image.load(os.path.join('Assets', 'Def7.PNG')),
                   'right right':pygame.image.load(os.path.join('Assets', 'Def8.PNG'))}

    definition = definitions[command]
    looking = True
    while looking:
        WIN.fill((255, 255, 255))
        WIN.blit(title_surface, (30, 250))
        WIN.blit(definition, (30, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # If the user pressed escape then return to the commands
                    looking = False
        pygame.display.update()


def commands():
    CLOCK = pygame.time.Clock()
    running = True
    while running:
        WIN.fill((240, 255, 255))

        B1 = pygame.Rect(80, 200, SMALL_RECT_WIDTH, RECT_HEIGHT)
        B2 = pygame.Rect(80, 300, RECT_WIDTH, RECT_HEIGHT)
        B3 = pygame.Rect(80, 400, SMALL_RECT_WIDTH, RECT_HEIGHT)
        B4 = pygame.Rect(80, 500, RECT_WIDTH, RECT_HEIGHT)
        B5 = pygame.Rect(500, 200, SMALL_RECT_WIDTH, RECT_HEIGHT)
        B6 = pygame.Rect(500, 300, SMALL_RECT_WIDTH, RECT_HEIGHT)
        B7 = pygame.Rect(500, 400, SMALL_RECT_WIDTH, RECT_HEIGHT)
        B8 = pygame.Rect(500, 500, SMALL_RECT_WIDTH, RECT_HEIGHT)

        mx, my = pygame.mouse.get_pos()
        if B1.collidepoint((mx, my)):
            if click:
                draw_command('up')


        if B2.collidepoint((mx, my)):
            if click:
                draw_command('down')

        if B3.collidepoint((mx, my)):
            if click:
                draw_command('left')

        if B4.collidepoint((mx, my)):
            if click:
                draw_command('right')

        if B5.collidepoint((mx, my)):
            if click:
                draw_command('up up')

        if B6.collidepoint((mx, my)):
            if click:
                draw_command('down down')

        if B7.collidepoint((mx, my)):
            if click:
                draw_command('left left')

        if B8.collidepoint((mx, my)):
            if click:
                draw_command('right right')

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # If the user pressed escape then close the program
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # If the user clicked set click to True
                if event.button == 1:
                    click = True


        draw_commands(move_commands, teleport_commands)
        CLOCK.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    commands()
