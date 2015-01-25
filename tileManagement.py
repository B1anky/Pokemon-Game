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
	dirt = BasicSprite("Dirt tile", MAIN_SPRITES, 1639, 1686, 0, 30, SCALE)
	return dirt

def createGrass1():
	grass1 = BasicSprite("Grass tile 1", MAIN_TILES1, 177, 193, 298, 314, SCALE)
	return grass1
