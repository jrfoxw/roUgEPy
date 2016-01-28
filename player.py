__author__ = 'PY-DEV'

from main import *
from xp import *
import pygame
#from npcs import *


class Player(Main, Xp):

    def __init__(self):
        Main.__init__(self)
        Xp.__init__(self)
        self.player_gold = 0
        self.player_level = 0
        self.player_HP = 20
        self.player_MP = 0
        self.player_XP = 0
        self.player_XP_SET = 10
        self.player_name = 'Test Player'
        self.player_ATT = 7
        self.player_DEF = 1
        self.player_ARCH = 'Adventurer'
        self.info_x = 30
        self.info_y = 16
        self.info_offset = 15

    # PLAYER INFO DISPLAY #
    def player_info_area(self):
        pygame.draw.rect(self.gameDisplay, self.WHITE, [25, 15, 750, 85], 2)
        pygame.draw.rect(self.gameDisplay, self.BLACK, [30, 20, 745, 80])
        offset1 = self.info_y+self.info_offset

        self.show_text(self.subFont, 'NAME: {}'.format(self.player_name), self.info_x, self.info_y, 0, 0, self.WHITE)
        self.show_text(self.subFont, 'CLASS: {}'.format(self.player_ARCH), self.info_x, offset1, 0, 0, self.WHITE)
        self.show_text(self.subFont, 'GOLD: {}'.format(self.player_gold), self.info_x, offset1+15, 0, 0, self.YELLOW)
        self.show_text(self.subFont, 'HP: {}'.format(self.player_HP), self.info_x, offset1+30, 0, 0, self.YELLOW)
        self.show_text(self.subFont, 'LEVEL: {}'.format(self.player_level), self.info_x+190, self.info_y, 0, 0,
                       self.YELLOW)
        self.show_text(self.subFont, 'XP: {}/{}'.format(self.player_XP, self.player_XP_SET), self.info_x+285,
                       self.info_y, 0, 0, self.YELLOW)
        # self.show_text(self.subFont, 'GOLD: {}'.format(self.player_gold), 30, 480, 0, 0, self.YELLOW)
        # self.show_text(self.subFont, 'GOLD: {}'.format(self.player_gold), 30, 480, 0, 0, self.YELLOW)

    # PLAYER ATTACK (May be moved to it's own class) #
    def player_attack(self, creature, creature_hp, creature_def=0):
        self.info_area(['You attack the {}...'.format(creature)], self.RED)
        print('Player attacks the {}'.format(creature))
        print('Creature HP:',creature_hp)
        attack = rrange(1, self.player_ATT)
        print('Attack Damage', attack)
        if attack > creature_def:
            new_hp = creature_hp - attack
            creature_hp = new_hp

            if new_hp <= 0:
                # Creature Dead Run XP function #
                print('Creature Dead..')
                self.messages.append([('The {} has died!'.format(creature)), self.RED])

                # remove creature from board #
                self.remove_creep(self.check_pos)

                # Run XP co-routine #
                self.add_xp(self.creeps_dict[creature]['XP'])
                self.messages.append([('You gain {} XP!'.format(self.creeps_dict[creature]['XP'])), self.WHITE])
                xp_left = abs(self.player_XP - self.player_XP_SET)

                self.messages.append([('{} XP remaining till next level.'.format(xp_left)), self.WHITE])
                self.info_area(self.messages[0], self.messages[1])

                return new_hp
            else:
                self.messages.append([('You Attack the {}!'.format(creature)),self.RED])
                self.messages.append([('You wound the {}, doing {} points of damage!'.format(creature, attack)), self.RED])
                print(self.messages)
                self.info_area(self.messages[0], self.messages[1])
                print('You wounded the {}, doing {} points of damage!'.format(creature, attack))
                return new_hp
        else:
            self.messages.append([('Your attack misses the mark..'.format(creature, attack)),self.YELLOW])
            print(self.messages)
            self.info_area(self.messages[0], self.messages[1])
            print('Your attack misses the mark...')
            return creature_hp

    # PROCESS XP #
    def add_xp(self, xp):
        pre_level = self.player_level
        b = self.level_gen()
        self.player_XP = self.xp_add(xp)
        ret = next(b)

        self.player_XP_SET = ret[1]
        self.player_level = ret[0]
        if self.player_level > pre_level:
            self.messages.append(['You are now level {}'.format(self.player_level), self.WHITE])
        self.player_info_area()





