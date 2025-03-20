#deck.py

import os
import pygame
import numpy as np
from tile import Tile

#Deck class that will allow for the shuffling, drawing, and storing of tiles
class Deck:
    
    tiles_left = 0
    
    #Shuffles the Deck
    def shuffle(self):
        np.random.shuffle(self.game_deck)

    #constructor that loads the tiles into an array
    def __init__(self):
        self.game_deck = []

        for i in (os.listdir('TileAssets')):
            i = "TileAssets/{}".format(i)
            for j in range(int(i[-1])):
                self.game_deck.append(Tile(500,400, i))
        self.shuffle()
        #Add the starting tile to the top of the deck
        self.game_deck.insert(0, Tile(500, 400, 'TileAssets/Tile8_3'))
        Deck.tiles_left = len(self.game_deck)

    #pops the tile on the bottom of the array out, shifting everything over, and returns it.
    def drawTile(self):
        if len(self.game_deck) > 0:
            Deck.tiles_left -= 1
            drawn_tile = self.game_deck.pop(0)
            return drawn_tile
        else:
            return None



