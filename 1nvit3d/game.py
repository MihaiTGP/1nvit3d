import math
import os
import pygame
import sys
import time
from copy import deepcopy
from levels import levels, levels_unchanged


pygame.init()

FONT = pygame.font.Font(os.path.join('Assets', 'Pixeboy.ttf'), 32)
TIME_FONT = pygame.font.Font(os.path.join('Assets', 'Pixeboy.ttf'), 50)
COIN_FONT = pygame.font.Font(os.path.join('Assets', 'Pixeboy.ttf'), 40)
LEVEL_FONT = pygame.font.Font(os.path.join('Assets', 'Pixeboy.ttf'), 65)
KEYS = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e,
        pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j,
        pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o,
        pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t,
        pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_SPACE]

WIDTH = 800
HEIGHT = 800
GAME_WIDTH = 600
GAME_HEIGHT = 600
CHAT_WIDTH = 700
CHAT_HEIGHT = 100
TILE_SIZE = 30

FPS = 60

WHITE = (255, 255, 255)
WHITELESS = (240, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

GAME_RECT = pygame.Rect(100, 50, GAME_WIDTH, GAME_HEIGHT)
CHAT_RECT = pygame.Rect(50, 680, CHAT_WIDTH, CHAT_HEIGHT)

WIN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('W0rdB0t')


class World():
    def __init__(self, data):
        self.tile_list = []
        self.data = data

    def render_terrain(self):
        x = 100
        y = 50
        TILE_IMG = pygame.image.load(os.path.join('Assets', 'Tile.PNG'))
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(TILE_IMG, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = x + col_count * TILE_SIZE
                    img_rect.y = y + row_count * TILE_SIZE
                    tile = (img, img_rect, 1)
                    self.tile_list.append(tile)

                if tile == 2:
                    img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'exit.png')), (30, 60))
                    img_rect = img.get_rect()
                    img_rect.x = x + col_count * TILE_SIZE
                    img_rect.y = y + row_count * TILE_SIZE
                    tile = (img, img_rect, 2)
                    self.tile_list.append(tile)

                if tile == 4:
                    img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spike.png')), (30, 30))
                    img_rect = img.get_rect()
                    img_rect.x = x + col_count * TILE_SIZE
                    img_rect.y = y + row_count * TILE_SIZE
                    tile = (img, img_rect, 4)
                    self.tile_list.append(tile)

                if tile == 5:
                    img = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spike.png')), (30, 30)), False, True)
                    img_rect = img.get_rect()
                    img_rect.x = x + col_count * TILE_SIZE
                    img_rect.y = y + row_count * TILE_SIZE
                    tile = (img, img_rect, 5)
                    self.tile_list.append(tile)


                if tile == 6:
                    img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spike.png')), (30, 30)), 90)
                    img_rect = img.get_rect()
                    img_rect.x = x + col_count * TILE_SIZE
                    img_rect.y = y + row_count * TILE_SIZE
                    tile = (img, img_rect, 6)
                    self.tile_list.append(tile)

                if tile == 7:
                    img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spike.png')), (30, 30)), 270)
                    img_rect = img.get_rect()
                    img_rect.x = x + col_count * TILE_SIZE
                    img_rect.y = y + row_count * TILE_SIZE
                    tile = (img, img_rect, 7)
                    self.tile_list.append(tile)

                if tile == 8:
                    img = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Coin.PNG')), (30, 30))
                    img_rect = img.get_rect()
                    img_rect.x = x + col_count * TILE_SIZE
                    img_rect.y = y + row_count * TILE_SIZE
                    tile = (img, img_rect, 8)
                    self.tile_list.append(tile)


                if tile == 9:
                    self.player = Player(row_count, col_count)
                    tile = (self.player.image, self.player.rect, 9)
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1

    def update_world(self, data):
        self.data = data

    def draw(self):
        for tile in self.tile_list:
            WIN.blit(tile[0], tile[1])


class Player():
    def __init__(self, row, col):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'robot.png')), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = col * 30 + 100
        self.rect.y = row * 30 + 50
        self.row = row
        self.col = col


    def move(self, dir):
        global level, coins, collected_coins

        if dir == 'up':
            # Death
            if world.data[self.row - 1][self.col] == 5:
                coins = 0
                levels[level] = deepcopy(levels_unchanged[level])
                world.update_world(levels[level])

            # Coin
            elif world.data[self.row - 1][self.col] == 8:
                world.data[self.row][self.col] = 0
                world.data[self.row - 1][self.col] = 9
                coins += 1


            # Empty
            elif world.data[self.row - 1][self.col] == 0:
                world.data[self.row][self.col] = 0
                world.data[self.row - 1][self.col] = 9

            # Exit
            elif world.data[self.row - 1][self.col] == 3:
                level += 1
                if level == 10:
                    pass
                else:
                    world.update_world(levels[level])

            
        if dir == 'right':
            if world.data[self.row][self.col + 1] == 6:
                coins = 0
                levels[level] = deepcopy(levels_unchanged[level])
                world.update_world(levels[level])

            elif world.data[self.row][self.col + 1] == 8:
                world.data[self.row][self.col] = 0
                world.data[self.row][self.col + 1] = 9
                coins += 1


            elif world.data[self.row][self.col + 1] == 0:
                world.data[self.row][self.col] = 0
                world.data[self.row][self.col + 1] = 9

            elif world.data[self.row][self.col + 1] == 3 or world.data[self.row][self.col + 1] == 2:
                level += 1
                if level == 10:
                    pass
                else:
                    world.update_world(levels[level])

        if dir == 'left':
            if world.data[self.row][self.col - 1] == 7:
                coins = 0
                levels[level] = deepcopy(levels_unchanged[level])
                world.update_world(levels[level])

            elif world.data[self.row][self.col - 1] == 8:
                world.data[self.row][self.col] = 0
                world.data[self.row][self.col - 1] = 9
                coins += 1

            elif world.data[self.row][self.col - 1] == 0:
                world.data[self.row][self.col] = 0
                world.data[self.row][self.col - 1] = 9

            elif world.data[self.row][self.col - 1] == 3 or world.data[self.row][self.col - 1] == 2:
                level += 1
                if level == 10:
                    pass
                else:
                    world.update_world(levels[level])


        if dir == 'down':
            if world.data[self.row + 1][self.col] == 4:
                levels[level] = deepcopy(levels_unchanged[level])
                world.update_world(levels[level])

            elif world.data[self.row + 1][self.col] == 8:
                world.data[self.row][self.col] = 0
                world.data[self.row + 1][self.col] = 9
                coins += 1

            elif world.data[self.row + 1][self.col] == 0:
                world.data[self.row][self.col] = 0
                world.data[self.row + 1][self.col] = 9

            elif world.data[self.row + 1][self.col] == 2:
                level += 1
                if level == 10:
                    pass
                else:
                    world.update_world(levels[level])


        if dir == 'up up':
            for i in range(19):
                if world.data[self.row - i][self.col] == 5:
                    coins = 0
                    levels[level] = deepcopy(levels_unchanged[level])
                    world.update_world(levels[level])
                    for tile in world.tile_list:
                        if tile[2] == 9:
                            world.tile_list.remove(tile)
                            break
                    break

                if world.data[self.row - i][self.col] == 8:
                    coins += 1
                    world.data[self.row - i][self.col] = 0


                elif world.data[self.row - i][self.col] == 1 or world.data[self.row - i][self.col] == 4 or world.data[self.row - i][self.col] == 6 or world.data[self.row - i][self.col] == 7:
                    world.data[self.row][self.col] = 0
                    world.data[self.row - i + 1][self.col] = 9
                    for tile in world.tile_list:
                        if tile[2] == 9:
                            world.tile_list.remove(tile)
                            break
                    break

                elif world.data[self.row - i][self.col] == 3:
                    level += 1
                    if level == 10:
                        pass
                    else:
                        world.render_terrain()
                        world.update_world(levels[level])
                        for tile in world.tile_list:
                            if tile[2] == 9:
                                world.tile_list.remove(tile)
                                break
                        break


        if dir == 'right right':
            for i in range(19):
                if world.data[self.row][self.col + i] == 6:
                    coins = 0
                    levels[level] = deepcopy(levels_unchanged[level])
                    world.update_world(levels[level])
                    for tile in world.tile_list:
                        if tile[2] == 9:
                            world.tile_list.remove(tile)
                            break
                    break

                elif world.data[self.row][self.col + i] == 8:
                    coins += 1
                    world.data[self.row][self.col + i] = 0

                elif world.data[self.row][self.col + i] == 1 or world.data[self.row][self.col + i] == 4 or world.data[self.row][self.col + i] == 5 or world.data[self.row][self.col + i] == 7:
                    world.data[self.row][self.col] = 0
                    world.data[self.row][self.col + i - 1] = 9
                    for tile in world.tile_list:
                        if tile[2] == 9:
                            world.tile_list.remove(tile)
                            break
                    break

                elif world.data[self.row][self.col + i] == 2 or world.data[self.row][self.col + i] == 3:
                    level += 1
                    if level == 10:
                        pass
                    else:
                        world.render_terrain()
                        world.update_world(levels[level])
                        for tile in world.tile_list:
                            if tile[2] == 9:
                                world.tile_list.remove(tile)
                                break
                        break


        if dir == 'left left':
            for i in range(19):
                if world.data[self.row][self.col - i] == 7:
                    coins = 0
                    levels[level] = deepcopy(levels_unchanged[level])
                    world.update_world(levels[level])
                    for tile in world.tile_list:
                        if tile[2] == 9:
                            world.tile_list.remove(tile)
                            break
                    break

                elif world.data[self.row][self.col - i] == 8:
                    coins += 1
                    world.data[self.row][self.col - i] = 0

                elif world.data[self.row][self.col - i] == 1 or world.data[self.row][self.col - i] == 4 or world.data[self.row][self.col - i] == 5 or world.data[self.row][self.col - i] == 6:
                    world.data[self.row][self.col] = 0
                    world.data[self.row][self.col - i + 1] = 9
                    for tile in world.tile_list:
                        if tile[2] == 9:
                            world.tile_list.remove(tile)
                            break
                    break

                elif world.data[self.row][self.col - i] == 2 or world.data[self.row][self.col - i] == 3:
                    level += 1
                    if level == 10:
                        pass
                    else:
                        world.update_world(levels[level])
                        for tile in world.tile_list:
                            if tile[2] == 9:
                                world.tile_list.remove(tile)
                                break
                        break


        if dir == 'down down':
            for i in range(19):
                if world.data[self.row + i][self.col] == 4:
                    coins = 0
                    levels[level] = deepcopy(levels_unchanged[level])
                    world.update_world(levels[level])
                    for tile in world.tile_list:
                        if tile[2] == 9:
                            world.tile_list.remove(tile)
                            break
                    break

                elif world.data[self.row + i][self.col] == 8:
                    coins += 1
                    world.data[self.row + i][self.col] = 0

                elif world.data[self.row + i][self.col] == 1 or world.data[self.row + i][self.col] == 5 or world.data[self.row + i][self.col] == 6 or world.data[self.row + i][self.col] == 7:
                    world.data[self.row][self.col] = 0
                    world.data[self.row + i - 1][self.col] = 9
                    for tile in world.tile_list:
                        if tile[2] == 9:
                            world.tile_list.remove(tile)
                            break
                    break

                elif world.data[self.row + i][self.col] == 3:
                    level += 1
                    if level == 10:
                        pass
                    else:
                        world.render_terrain()
                        world.update_world(levels[level])
                        for tile in world.tile_list:
                            if tile[2] == 9:
                                world.tile_list.remove(tile)
                                break
                        break

        if level != 10:
            world.tile_list = []
            world.render_terrain()

coins = 0
level = 0
command_count = 0

world = World(levels[level])
world.render_terrain()


def draw_game():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, GAME_RECT, 3)
    pygame.draw.rect(WIN, BLACK, CHAT_RECT, 3)

    BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'Background.jpg'))
    BACKGROUND = pygame.transform.scale(BACKGROUND_IMG, (600, 600))
    WIN.blit(BACKGROUND, (100, 50))


def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    hour = minute // 60

    mat = " " + str(minute) + ":" + str(sec)
    return mat, minute, sec


def draw_time(time):
    time_surface = TIME_FONT.render(format_time(time)[0], True, BLACK).convert_alpha()
    WIN.blit(time_surface, (0, 100))

def draw_coins(coins):
    coin_surface = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Coin.png')), (40, 40))
    coin_points = COIN_FONT.render('x' + str(coins), True,BLACK)
    WIN.blit(coin_surface, (700, 100))
    WIN.blit(coin_points, (740, 110))

def draw_level(level):
    level_surface = LEVEL_FONT.render('Level ' + str(level + 1), True, BLACK)
    WIN.blit(level_surface, (305, 10))

def draw_final(time, coins, commands):
    WIN.fill(WHITELESS)
    cong_text = ''

    if (int(format_time(time)[1]) == 10 and int(format_time(time)[2]) < 1) or (int(format_time(time)[1] <= 9) and int(format_time(time)[2]) < 60) and coins >= 20:
        cong_text = 'Congratulations, you made it!'
        text_surface = COIN_FONT.render(cong_text, True, BLUE)


    elif int(format_time(time)[1] < 10) and int(format_time(time)[2]) < 60 and coins <= 19:
        cong_text = 'You don\'t have enough coins!'
        text_surface = COIN_FONT.render(cong_text, True, RED)

    elif int(format_time(time)[1]) >= 10 and int(format_time(time)[2]) > 00:
        cong_text = 'You didn\'t get there in time! ;('
        text_surface = COIN_FONT.render(cong_text, True, RED)

    coins_surface = FONT.render('You collected ' + str(coins) + ' coins!', True, BLACK)
    time_surface = FONT.render('You finished the game in ' + str(format_time(time)[1]) + ' minutes and ' + str(format_time(time)[2]) + ' seconds', True, BLACK)
    command_surface = FONT.render('You wrote ' + str(commands) + ' commands!', True, BLACK)
    esc_surface = COIN_FONT.render('Press ESC to return to the menu', True, BLACK)

    WIN.blit(text_surface, (20, 160))
    WIN.blit(coins_surface, (20, 230))
    WIN.blit(time_surface, (20, 260))
    WIN.blit(command_surface, (20, 290))
    WIN.blit(esc_surface, (20, 400))


def game():
    global level, coins, world, command_count
    level = 0
    coins = 0
    for lvl in range(0, len(levels)):
        levels[lvl] = deepcopy(levels_unchanged[lvl])
    world = World(levels[level])
    world.render_terrain()
    text = ''
    active = False
    CLOCK = pygame.time.Clock()
    running = True
    time_start = time.time()
    while running:

        if level != 10:
            play_time = round(time.time() - time_start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHAT_RECT.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[0:-1]

                    elif event.key == pygame.K_RETURN:
                        commands = ['up', 'right', 'left', 'down', 'up up', 'right right', 'left left', 'down down']
                        if text.lower() in commands:
                            world.player.move(text.lower())
                            command_count += 1

                        text = ''

                    elif text_surface.get_width() < CHAT_RECT.w - 20 and event.key in KEYS:
                        text += event.unicode

                if event.key == pygame.K_ESCAPE:
                    running = False

        if level != 10:
            draw_game()
            world.draw()
            draw_time(play_time)
            draw_level(level)
            draw_coins(coins)
            text_surface = FONT.render(text, True, BLACK)
            WIN.blit(text_surface, (CHAT_RECT.x + 5, CHAT_RECT.y + 5))
            CLOCK.tick(FPS)
        else:
            draw_final(play_time, coins, command_count)

        pygame.display.update()


if __name__ == '__main__':
    game()
