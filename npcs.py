__author__ = 'PY-DEV'

from random import randrange as rrange

from player import *


class Npcs(Player):

    def __init__(self):
        Main.__init__(self)
        Player.__init__(self)

        self.npc_dict = {
                    'cleric': {
                        'name': 'Acolyte',
                        'number': 80,
                        'mana': 5,
                        'prayers': 'cure light wounds',
                        'rarity': 50,
                        'symbol': 'C',
                        'color': self.LIGHT_BLUE,

                              }
                    }
        self.npc = ['cleric',  'shopkeeper', 'princess']

        # Npc appearance is based off of rarity, a 30 rarity means that there is a 30% chance of NPC showing up.

    def npc_rarity_check(self, random_x, random_y):
        rarity = rrange(1, 100)
        if self.npc_dict['cleric']['rarity'] <= rarity:
            print('Cleric appears..')
            self.place_npc(random_x, random_y)

    def place_npc(self, random_y, random_x):
        # PLACE NPC #
        for random_walls in range(rrange(1, 2)):
            mob_pos = [rrange(2, random_y-2), rrange(2, random_x-2)]
            if self.map_grid[mob_pos[0]][mob_pos[1]] < 2 > 0:
                self.map_grid[mob_pos[0]][mob_pos[1]] = 80

    def cleric_heal(self):
        healer = self.npc_dict['cleric']
        self.info_area(['the {} heals all your wounds.. and suddenly vanishes.'.format(healer['name'])], self.BLUE)
        self.player_HP += 5
        self.player_info_area()

