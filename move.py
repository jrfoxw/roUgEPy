#from rooms import *
from creeps import *
#from items import *

__author__ = 'PY-DEV'


class Move(Creeps):

    #def __init__(self):
        # Main.__init__(self)

    # def __init__(self):
    #
    #     Npcs.__init__(self)
    #     Player.__init__(self)
    #     Creeps.__init__(self)
    #     Items.__init__(self)
    #     Rooms.__init__(self)

    def mov_dir(self, x, y):
        self.check_pos = self.map_grid[self.player_pos[0]+x][self.player_pos[1]+y]
        self.grid_pos = [self.player_pos[0]+x, self.player_pos[1]+y]
        self.info_area([])

        def redraw():
            print('Before Redraw: ', self.player_pos)
            pygame.draw.rect(self.gameDisplay, self.BLACK, [self.room_loc[0], self.room_loc[1], 350, 350])
            self.map_grid[self.player_pos[0]][self.player_pos[1]] = 1
            self.player_pos[0] += x
            self.player_pos[1] += y
            self.map_grid[self.player_pos[0]][self.player_pos[1]] = 2
            self.render_room_screen()
            print('After Redraw: ',self.player_pos)
            #self.info_area([])

        if self.check_pos != 0 and self.check_pos not in self.mobs_list:
            redraw()
            self.messages = []

        if self.check_pos in self.mobs_list:
            self.creeps_attack(self.grid_pos)

        if self.check_pos in self.items_list:
            self.random_treasure()
            #redraw()

        if self.check_pos in self.npc_list:
            self.cleric_heal()

        elif self.check_pos == 0:
            self.messages.append([('A slime covered wall blocks your path..'),self.WHITE])
            self.info_area(['A slime covered wall blocks your path..'], self.WHITE)


if __name__ == '__main__':

    new_game = Move()
    new_game.info_area([])
    new_game.player_info_area()

    start = new_game.create_random_map()
    print('START: ', start)
    new_game.place_creeps(start[1], start[0])
    new_game.place_treasure(start[1], start[0])
    new_game.npc_rarity_check(start[1], start[0])

    #new_game.render_room()
    new_game.render_room_screen()
    print(new_game.get_creeps())


    # MAIN GAME LOOP #
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                print('Key pressed')
                if event.key == pygame.K_w:
                    new_game.mov_dir(-1, 0)
                if event.key == pygame.K_s:
                    new_game.mov_dir(+1, 0)
                if event.key == pygame.K_d:
                    new_game.mov_dir(0, +1)
                if event.key == pygame.K_a:
                    new_game.mov_dir(0, -1)

        pygame.display.update()
