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

def createTree1():
	treeList1 = []
	tree11 = BasicSprite("Little root tree quad. 1", MAIN_TILES1, 0, 16, 324, 340, SCALE)
	tree12 = BasicSprite("Little root tree quad. 2", MAIN_TILES1, 16, 32, 324, 340, SCALE)
	tree13 = BasicSprite("Little root tree quad. 3", MAIN_TILES1, 0, 16, 340, 378, SCALE)
	tree14 = BasicSprite("Little root tree quad. 4", MAIN_TILES1, 16, 32, 340, 378, SCALE)
	treeList1.append(tree11)
	treeList1.append(tree12)
	treeList1.append(tree13)
	treeList1.append(tree14)

	return treeList1
