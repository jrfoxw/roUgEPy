__author__ = 'PY-DEV'

from random import randrange as rrange
#from main import *
#from player import *


class Items:
    # def __init__(self):


    def place_treasure(self, random_y, random_x):
        # TREASURE CHESTS #
        for random_walls in range(rrange(1, 3)):
            mob_pos = [rrange(2, random_y-2), rrange(2, random_x-2)]
            if self.map_grid[mob_pos[0]][mob_pos[1]] < 2 > 0:
                self.map_grid[mob_pos[0]][mob_pos[1]] = 7

    def random_treasure(self):
        gold = rrange(10, 50)
        self.messages.append([('You found {} pieces of gold!'.format(gold)), self.YELLOW])
        print('>>',self.messages[0][0],self.messages[0][1])
        self.player_gold = gold+self.player_gold
        self.player_info_area()
        self.info_area(self.messages[0][0], self.messages[0][1])

    def random_item(self):
        pass




