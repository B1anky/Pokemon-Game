import tileManagement
from TileSprite import TileSprite
from pygame import *

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
	for i in range(10):
		#Height
		for j in range(10):
			dirtList.append(TileSprite(dirtImage, [], ((i * 235),(j * 150)),\
						dirtImage, 0, None, True, "Dirt", [], [], 0))

	return dirtList

def createTown1Grass():
	grassTileImage1 = tileManagement.createGrass1()
	grassList = []

	for i in range(30):
		for j in range(16):
			grassList.append(TileSprite(grassTileImage1, [], (i * 64, j * 64), grassTileImage1, \
				0, None, True, "Grass", [], [], 0))

	return grassList