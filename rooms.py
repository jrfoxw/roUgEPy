__author__ = 'PY-DEV'
#from main import *
import pygame

class Rooms():


    def render_room(self):
        #print(update_grid)
        for x_grid in range(len(self.map_grid)):
            print('')
            for y_grid in range(len(self.map_grid[x_grid])):
                print('{}'.format(self.map_grid[x_grid][y_grid]), end='')

        # for each in update_grid:
        #     final_render.append(''.join(each))
        #print('>>',final_render)


    def render_room_screen(self):

        # b = gen_loc(200, 800, 15)
        # c = gen_loc(200, 800, 55)
        #global player_pos
        pygame.draw.rect(self.gameDisplay, self.BLACK, [self.room_loc[0], self.room_loc[1], 850, 350])
        for x in range(len(self.map_grid)):
            for y in range(len(self.map_grid[x])):
                for each in self.room_objs.keys():
                    if self.map_grid[x][y] == each:
                        self.show_text(self.playFont, self.room_objs[each]['symbol'], self.room_loc[0]+y*25, self.room_loc[1]+x*25, 0, 0, self.room_objs[each]['color'])
                        if self.map_grid[x][y] == 2 and each == 2:
                            player_pos = [x, y]



