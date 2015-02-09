import tileManagement
from TileSprite import TileSprite
from pygame import *
from scale import *

def createMaps():
	createTown1()

def createTown1():
	createTown1Ground()

def createTown1Ground():
	createTown1Dirt()

def createTown1Dirt():
	dirtImage = tileManagement.createDirt()
	dirtList = []

	#Width
	#for i in range(10):
		#Height
	#	for j in range(10):
#	for i in range(1920 // TILEWIDTH):
#		for j in range(1080 // TILEWIDTH):
	dirtList.append(TileSprite(dirtImage, [], (15 ,15), ((15 * TILEWIDTH),(15 * TILEWIDTH)),\
				dirtImage, 0, None, True, "Dirt", [], [], 0))

	return dirtList

def createTown1Grass():
	grassTileImage1 = tileManagement.createGrass1()
	grassList = []
	#for i in range(10):
	#	for j in range(10):
	
	for i in range(10, levelsize[0]):
		for j in range(10, levelsize[0]):
			grassList.append(TileSprite(grassTileImage1, [], (i, j), (i * TILEWIDTH, j * TILEWIDTH), grassTileImage1, \
				0, None, True, "Grass", [], [], 0))

	return grassList

def createTown1Trees():
	treeTileImage1 = tileManagement.createTree1()
	treeList = []
	finalTreeList = []

	n = levelsize[0]
	n2 = levelsize[1]

	for x in range(0, n, 2):
		for y in range(0, n2, 2):
				treeList.append(TileSprite(treeTileImage1[0], [], (x, y), (x * TILEWIDTH, y * TILEWIDTH), treeTileImage1[0], \
					0, None, False, "Tree", [], [], 0))
				treeList.append(TileSprite(treeTileImage1[1], [], (x + 1, y), (x * TILEWIDTH, y * TILEWIDTH), treeTileImage1[1], \
					0, None, False, "Tree", [], [], 0))
				treeList.append(TileSprite(treeTileImage1[2], [], (x, y + 1), (x * TILEWIDTH, y * TILEWIDTH), treeTileImage1[2], \
					0, None, False, "Tree", [], [], 0))
				treeList.append(TileSprite(treeTileImage1[3], [], (x + 1, y + 1), (x * TILEWIDTH, y * TILEWIDTH), treeTileImage1[3], \
					0, None, False, "Tree", [], [], 0))

	for tree in treeList:
		if 0 <= tree.returnTileCoords()[0] <= (55/SCALE) \
		or 0 <= tree.returnTileCoords()[1] <= (50/SCALE) \
		or n - (65/SCALE) <= tree.returnTileCoords()[0] <= n\
		or n - (47/SCALE) <= tree.returnTileCoords()[1] <= n:
			finalTreeList.append(tree)
	
	return finalTreeList