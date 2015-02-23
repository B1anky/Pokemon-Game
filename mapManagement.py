import tileManagement
from TileSprite import TileSprite
from pygame import *
from scale import *

MASTER_DIRT = []
MASTER_GRASS = []

def readMapFromFile(filename):
	array2d = []
	with open(filename) as file:
		array2d = [[int(digit) for digit in line.strip()] for line in file]
	print(array2d)
	return array2d

def createMaps():
	twoDee = readMapFromFile('map.pkm')
	return createTown1(twoDee)

def createTown1(twoDee):
	List = []
	MASTER_GRASS = []
	MASTER_DIRT = []	

	for i in range(0, len(twoDee)):
		for j in range(0, len(twoDee[i])):
			key = switchStmt(twoDee[i][j])
			if key == 'grass':
				MASTER_GRASS.append(createSingleGrass(i,j))
			if key == 'dirt':
				MASTER_DIRT.append(createSingleDirt(i,j))
			if key == 'tree':
				print("adding tree")

	List.append(MASTER_GRASS)
	List.append(MASTER_DIRT)
	return List

def switchStmt(code):
	return
	{
		0 : 'grass',
		1 : 'dirt',
		2 : 'tree',
	}.get(x, 0)

def getDirtList():
	return MASTER_DIRT
def getGrassList():
	return MASTER_GRASS

def createTown1Dirt():
	dirtImage = tileManagement.createDirt()
	dirtList = []

	dirtList.append(TileSprite(dirtImage, [], (15 ,15), ((15 * TILEWIDTH),(15 * TILEWIDTH)),\
				dirtImage, 0, None, True, "Dirt", [], [], 0))
	dirtList.append(TileSprite(dirtImage, [], (18 ,15), ((18 * TILEWIDTH),(15 * TILEWIDTH)),\
				dirtImage, 0, None, True, "Dirt", [], [], 0))
	return dirtList

def createTown1Grass():
	grassTileImage1 = tileManagement.createGrass1()
	grassList = []
	#for i in range(10):
	#	for j in range(10):
	
	for x in range(10, 20):
		for y in range(10, 20):
			grassList.append(TileSprite(grassTileImage1, [], (x, y), (x * TILEWIDTH, y * TILEWIDTH), grassTileImage1, \
				0, None, True, "Grass", [], [], 0))

	return grassList

def createTown1Trees():
	treeTileImage1 = tileManagement.createTree1()
	treeList = []
	finalTreeList = []

	n = levelsize[0]
	n2 = levelsize[1]

	for x in range(0, 10, 2):
		for y in range(0, 10, 2):
				treeList.append(TileSprite(treeTileImage1[0], [], (x, y), (x * TILEWIDTH, y * TILEWIDTH), treeTileImage1[0], \
					0, None, False, "Tree", [], [], 0))
				treeList.append(TileSprite(treeTileImage1[1], [], (x + 1, y), (x  * TILEWIDTH, y * TILEWIDTH), treeTileImage1[1], \
					0, None, False, "Tree", [], [], 0))
				treeList.append(TileSprite(treeTileImage1[2], [], (x, y + 1), (x * TILEWIDTH, y  * TILEWIDTH), treeTileImage1[2], \
					0, None, False, "Tree", [], [], 0))
				treeList.append(TileSprite(treeTileImage1[3], [], (x + 1, y + 1), (x  * TILEWIDTH, y  * TILEWIDTH), treeTileImage1[3], \
					0, None, False, "Tree", [], [], 0))

	for tree in treeList:
		if 0 <= tree.returnTileCoords()[0] <= (55//SCALE) \
		or 0 <= tree.returnTileCoords()[1] <= (50//SCALE) \
		or n - (65//SCALE) <= tree.returnTileCoords()[0] <= n\
		or n - (47//SCALE) <= tree.returnTileCoords()[1] <= n:
			finalTreeList.append(tree)
	
	return finalTreeList


def createSingleGrass(x, y):
	grassTileImage1 = tileManagement.createGrass1()
	return (TileSprite(grassTileImage1, [], (x, y), (x * TILEWIDTH, y * TILEWIDTH), grassTileImage1, \
				0, None, True, "Grass", [], [], 0))
def createSingleDirt(x,y):
	dirtImage = tileManagement.createDirt()
	dirtList = []

	dirtList.append(TileSprite(dirtImage, [], (15 ,15), ((15 * TILEWIDTH),(15 * TILEWIDTH)),\
				dirtImage, 0, None, True, "Dirt", [], [], 0))
	dirtList.append(TileSprite(dirtImage, [], (18 ,15), ((18 * TILEWIDTH),(15 * TILEWIDTH)),\
				dirtImage, 0, None, True, "Dirt", [], [], 0))
	return dirtList