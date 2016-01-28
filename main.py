__author__ = 'PY-DEV'


import pygame
from random import randrange as rrange
#from creeps import *
#from xp import *
from rooms import *
from items import *

pygame.init()


# Colors Defined #

class Main(Rooms, Items):

    def __init__(self):

        # PYGAME INIT SETTINGS #
        self.gameDisplay = pygame.display.set_mode([1024, 768])
        self.fontsize_main = 20
        self.fontsize_sub = 15
        self.mainFont = pygame.font.SysFont("arial", self.fontsize_main)
        self.subFont = pygame.font.SysFont('monospace', self.fontsize_sub)
        self.playFont = pygame.font.SysFont('Times Roman', 20)

        # INITIALIZE COLORS #
        self.WHITE   =   [255,255,255]
        self.BLACK   =   [0,0,0]
        self.RED     =   [255,0,0]
        self.BLUE    =   [0,0, 255]
        self.GREEN   =   [0,255,0]
        self.YELLOW  =   [245, 241, 7]
        self.LIGHT_BLUE = [107, 201, 232]
        self.font_spacing = 10

        # INITIALIZE ROOM OBJECTS #
        self.mobs_list = [2, 3, 4, 52]
        self.items_list = [7]
        self.npc_list = [80]
        self.room_loc = [75, 110]
        self.player_pos = 0
        self.map_grid = []
        self.room_objs = {
                0: {'symbol': '#', 'color': self.RED},
                1: {'symbol': '.', 'color': self.WHITE},
                2: {'symbol': '@', 'color': self.LIGHT_BLUE},
                3: {'symbol': 'g', 'color': self.GREEN},
                4: {'symbol': 'r', 'color': self.RED},
                52: {'symbol': 'w', 'color': self.GREEN},
                7: {'symbol': '$', 'color': self.YELLOW},
                80: {'symbol': 'C', 'color': self.BLUE},

                          }
        self.spawn = {}
        self.check_pos = 0
        self.messages = []

    def create_random_map(self):
        # LAYOUT ROOM ##
        random_x = rrange(7,35)
        random_y = rrange(7,15)
        self.map_grid = [[0 for x in range(random_x)] for y in range(random_y)]
        for pos_x in range(1, len(self.map_grid)-1):
            for pos_y in range(1, len(self.map_grid[pos_x])-1):
                self.map_grid[pos_x][pos_y] = 1

        # DEFINE PLAYER START LOCATION ##
        self.player_pos = [rrange(2, random_y-2), rrange(2, random_x-2)]
        print('MAP:',random_x, random_y)
        print('PLAYER:',self.player_pos)
        self.map_grid[self.player_pos[0]][self.player_pos[1]] = 2

        # CREATE RANDOM ITEMS IN ROOM ##

        # Walls #
        for random_walls in range(rrange(1, 19)):
            wall_pos = [rrange(2, random_y-2), rrange(2, random_x-2)]
            if self.map_grid[wall_pos[0]][wall_pos[1]] != 2:
                self.map_grid[wall_pos[0]][wall_pos[1]] = 0

        return [random_x, random_y]


    # Generator for x, y cords for text #
    def gen_loc(self, start, end, offset):
        for x in range(start, end, offset):
            for y in range(start, end, offset):
                yield x, y

    def gen_letter(self, text):
        for letter in text:
            yield letter


    def info_area(self, text, color=list, offset=list):
        b = self.gen_loc(255, 775, 25)
        c = self.gen_loc(15, 75, 15)
        pygame.draw.rect(self.gameDisplay, self.RED, [25, 475, 750, 285], 2)
        pygame.draw.rect(self.gameDisplay, self.BLACK, [30, 480, 740, 275])
        print('\n')
        print('*'*50)
        print('>>>',text)
        for each in self.messages:
            next_text = next(b)
            print('x:{},y:{} {}'.format(35, next_text[1], each[0]))
            self.show_text(self.mainFont, each[0], 35, next_text[1], 0, next_text[0], each[1])
            check = each[0].split()
            v = self.mainFont.size(each[0])

            new_n = {}
            n = self.mainFont.metrics(each[0])
            z = self.gen_letter(each[0])
            for each in n:
                new_n[next(z)] = each

            print('V',v)
            for each in new_n.items():
                print('>> ',each)

            for items in check:
                if items.isdigit():
                    print('{}'.format(items))
                    print('\n-------------- DIGIT FOUND ------------------\n')
                    digit_index = each[0].index(items)
                    print('digit_index',digit_index)
                    self.show_text2(self.mainFont, items, int(digit_index)*15, next_text[1], 0, next_text[0], self.WHITE)
        print('*'*50)
        print('\n')

    def show_text(self, fonttype, text2show, x_cor, y_cor, fontx_offset=0, fonty_offset=0, color=list):
        text = fonttype.render(text2show, True,  color)
        self.gameDisplay.blit(text, [fontx_offset + x_cor, fonty_offset + y_cor])

    def show_text2(self, fonttype, text2show, x_cor, y_cor, fontx_offset=0, fonty_offset=0, color=list):
        text = fonttype.render(text2show, True, color)
        self.gameDisplay.blit(text, [fontx_offset+x_cor, fonty_offset+y_cor])

