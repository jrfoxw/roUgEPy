__author__ = 'PY-DEV'

from pygame import *

class(object):

    def __init__(self, fonttype, text2show, x_cor, y_cor, fontx_offset=0, fonty_offset=0, color=list ):


    def show_text(self, fonttype, text2show, x_cor, y_cor, fontx_offset=0, fonty_offset=0, color=list):
        text = fonttype.render(text2show, True,  color)
        self.gameDisplay.blit(text, [fontx_offset + x_cor, fonty_offset + y_cor])