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
	size = (1920, 1080)
	screen = display.set_mode(size, video_flags)

	#Creates the player object
	objectLists = playersAndMobs.createRed()

	tileList1 = mapManagement.createTown1Dirt()
	tileList2 = mapManagement.createTown1Grass()

	#Immediately maximizes the screen upon starting, calls method in windowControl module
	windowControl.SDL_Maximize()

	#Initializes the lists for blitting optimizations
	dirtyTilesList = []
	coordsList = []

	#Initial blit of every grass tile 
	for tile in tileList2:
		if tile != None:
			tile.updateAll(screen)

	while keepGoing: 

		#Updates the display/objects by calling the objects' class update methods

		#Dirty tile optimizations, only updates necessary surrounding tile coords
		#Helps CPU when scale is very low
		for dirtySurroundingTiles in dirtyTilesList:
			for dirtyCoords in dirtySurroundingTiles:
				for tiles in tileList2:
					if tiles.returnTileCoords() == dirtyCoords:
						tiles.updateAll(screen)
						coordsList = []
						dirtyTilesList = []

		#Draws/updates characters
		#for character in objectLists[0]:
		#	character.updateAll(screen)
		#	dirtyTilesList.append(character.getDirty(coordsList, size[0]//TILEWIDTH, size[1]//TILEWIDTH))
		
		#Draws/updates players
		for player in objectLists[1]:
			player.updateAllPlayers(screen)
			dirtyTilesList.append(player.getDirty(coordsList, size[0]//TILEWIDTH, size[1]//TILEWIDTH))

		time.Clock().tick(FPS)

		display.flip()  

