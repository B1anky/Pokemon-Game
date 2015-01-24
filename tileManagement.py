from pygame import *
from BasicSprite import BasicSprite

MAIN_SPRITES = image.load("spriteSheet.gif")
MAIN_TILES1 = image.load("LittleRootSheet.png")


def createDirt():
	dirt = BasicSprite("Dirt tile", MAIN_SPRITES, 1639, 1686, 0, 30, 5, 0, 0)
	return dirt

def createGrass1():
	grass1 = BasicSprite("Grass tile 1", MAIN_TILES1, 160, 176, 298, 314, 5, 0, 0)
	return grass1
