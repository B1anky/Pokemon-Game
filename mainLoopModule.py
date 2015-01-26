from pygame import *
import playersAndMobs
import mapManagement
import windowControl
from scale import *
FPS = 60

#Main window loop which will blit everything to screen
def run():
	init()
	keepGoing = True
	video_flags = RESIZABLE
	screen = display.set_mode(size, video_flags)

	#Creates the player object
	objectLists = playersAndMobs.createRed()

	tileList1 = mapManagement.createTown1Dirt()
	tileList2 = mapManagement.createTown1Grass()

	#Immediately maximizes the screen upon starting, calls method in windowControl module
	windowControl.SDL_Maximize()

	#Initializes the lists for blitting optimizations
	allDirtyTilesList = []
	coordsList = []

	templ = [tileList2[0]] * (size[1]//TILEWIDTH)
	masterTileList = [templ] * (size[0]//TILEWIDTH)

	tx = 0
	ty = 0

	#Initial blit of every grass tile 	
	for tile in tileList2:
		if tile == None:
			continue
		if tx >= (size[1]//TILEWIDTH):
			ty += 1
			tx = 0
		try:
			masterTileList[tx][ty] = tile
		except:
			pass
		tile.updateAll(screen)
		tx += 1

	while keepGoing: 

		#Updates the display/objects by calling the objects' class update methods

		#Dirty tile optimizations, only updates necessary surrounding tile coords
		#Helps CPU when scale is very low
		for dirtyObjectTilesList in allDirtyTilesList:
			for dirtyTupleCoords in dirtyObjectTilesList:
				'''
				DTCx = dirtyTupleCoords[0]
				DTCy = dirtyTupleCoords[1]
				tile = masterTileList[DTCx][DTCy]
				if tile == None:
					continue
				tile.updateAll(screen)
				coordsList = []
				allDirtyTilesList = []

				'''
				for tiles in tileList2:
					if tiles.returnTileCoords() == dirtyTupleCoords:
						tiles.updateAll(screen)
						coordsList = []
						allDirtyTilesList = []
				

		#Draws/updates characters
		for character in objectLists[0]:
			character.updateAll(screen)
			allDirtyTilesList.append(character.getDirty(coordsList, size[0]//TILEWIDTH, size[1]//TILEWIDTH))
		
		#Draws/updates players
		for player in objectLists[1]:
			allDirtyTilesList.append(player.getDirty(coordsList, size[0]//TILEWIDTH, size[1]//TILEWIDTH))
			player.updateAllPlayers(screen, masterTileList)
			
		time.Clock().tick(FPS)

		display.flip()  

