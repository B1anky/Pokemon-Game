from pygame import *
from BasicSprite import BasicSprite
import os
from scale import SCALE

MAIN_SPRITES = None
MAIN_SPRITES1 = None


if os.name == 'nt':
	MAIN_SPRITES = image.load("spriteSheet.gif")
	MAIN_TILES1 = image.load("LittleRootSheet.png")
else:
	MAIN_SPRITES = image.load("spriteSheet.bmp")
	MAIN_TILES1 = image.load("LittleRootSheet.bmp")


def createDirt():
	dirt = BasicSprite("Dirt tile", MAIN_SPRITES, 1639, 1686, 0, 30, SCALE, 0, 0)
	return dirt

def createGrass1():
	grass1 = BasicSprite("Grass tile 1", MAIN_TILES1, 160, 176, 298, 314, SCALE, 0, 0)
	return grass1
