__author__ = 'PY-DEV'

from random import randrange as rrange
from random import choice
from npcs import *


class Creeps(Npcs):
    def __init__(self):
        Main.__init__(self)
        Player.__init__(self)
        Npcs.__init__(self)
        self.check_pos = 0
        self.amount = 0
        self.hp = 0
        self.creeps_dict = {

                        'goblin':   {
                            'name': 'goblin',
                            'color': self.GREEN,
                            'symbol': 'g',
                            'number': 3,
                            'DMG': 4,
                            'HP': 10,
                            'DEF': 2,
                            'weapon': 'club',
                            'XP': 12,
                                  },

                        'rat':  {
                            'name': 'rat',
                            'color': self.BLUE,
                            'symbol': 'r',
                            'number': 4,
                            'DMG': 3,
                            'HP': 4,
                            'DEF': 1,
                            'weapon': 'teeth',
                            'XP': 11,
                                },

                        'wolf':  {
                            'name': 'wolf',
                            'color': self.GREEN,
                            'symbol': 'w',
                            'number': 52,
                            'DMG': 5,
                            'HP': 15,
                            'DEF': 3,
                            'weapon': 'teeth',
                            'XP': 14,
                                }
                            }

        self.creeps_list = ['goblin', 'rat', 'wolf']
        self.creeps_alive = {}


    def get_creeps(self):
        # choose a creep randomly #
        creep = choice(self.creeps_list)
        print('')

        return self.creeps_dict[creep]

    def place_creeps(self, random_y, random_x):
        # Mobs #
        for random_walls in range(rrange(2, 8)):
            mob_pos = [rrange(2, random_y-2), rrange(2, random_x-2)]
            if self.map_grid[mob_pos[0]][mob_pos[1]] not in self.mobs_list:

                spawn = self.get_creeps()
                self.map_grid[mob_pos[0]][mob_pos[1]] = spawn['number']
                self.amount += 1
                self.creeps_alive[self.amount] = {'name': spawn['name'],
                                                  'pos': mob_pos,
                                                  'hp': spawn['HP']}
        print(self.creeps_alive)

    def creeps_attack(self, check_pos):
        self.check_pos = check_pos

        print('check pos(Creeps Attack)', check_pos)
        for each in self.creeps_alive:
            if check_pos[0] == self.creeps_alive[each]['pos'][0] and \
               check_pos[1] == self.creeps_alive[each]['pos'][1]:
                    self.stats = self.creeps_dict[self.creeps_alive[each]['name']]
                    self.spawn = self.creeps_alive[each]
                    spawn_dmg = rrange(1, self.stats['DMG'])
                    if rrange(self.stats['DMG']) != 0:
                        self.messages = []
                        self.messages.append([('A {} attacks you.. with its {}'.format(self.stats['name'], self.stats['weapon'])),self.RED])
                        self.messages.append([('Doing {} points of damage'.format(spawn_dmg)),self.YELLOW])

                        # self.info_area(['A {} attacks you.. with its {}'.format(self.stats['name'], self.stats['weapon']),
                        #                 ('Doing {} points of damage'.format(spawn_dmg))], self.RED)

                        print('A {} attacks you.. with its {}'.format(self.stats['name'], self.stats['weapon']))
                        print('Doing {} points of damage'.format(spawn_dmg))

                        self.player_HP = self.player_HP - spawn_dmg
                        self.player_info_area()
                        self.hp = self.player_attack(self.spawn['name'], self.spawn['hp'], self.stats['DEF'])
                        self.spawn['hp'] = self.hp
                        print('Creeps_attack Function HP', self.hp)
                        return self.hp
                    else:
                        self.messages = []
                        self.messages.append(['A {} attacks you.. with its {}'.format(self.spawn['name'], self.stats['weapon']),self.RED])
                        self.messages.append([('But fails to do any damage!'),self.YELLOW])
                        # self.info_area(['A {} attacks you.. with its {}'.format(self.spawn['name'], self.stats['weapon']),
                        #                 'But fails to do any damage!'], self.WHITE)
                        print('Creature fails in attack!!')
                        self.player_info_area()
                        self.hp = self.player_attack(self.spawn['name'], self.spawn['hp'], self.stats['DEF'])
                        self.spawn['hp'] = self.hp
                        print('Creeps_attack Function HP', self.hp)
                        return self.hp



    def remove_creep(self, check_pos):

        print('Check Pos..', check_pos)
        print('Class Check Pos...', self.check_pos)
        self.map_grid[check_pos[0]][check_pos[1]] = 1
        self.random_treasure()
        self.render_room_screen()
        for each in self.creeps_alive.keys():
            if self.creeps_alive[each]['pos'] == self.check_pos:
                self.creeps_alive[each] = {'name': '', 'pos': [-1, -1], 'hp': 0}

        print('Creeps remaining..', self.creeps_alive)

