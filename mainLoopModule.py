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

	dirtytiles = []

	templ = [None] * (size[1]//TILEWIDTH)
	tiles = [templ] * (size[0]//TILEWIDTH)
	count = 0



	while keepGoing: 
		#Updates the display/objects by calling the objects' class update methods
		for tile in tileList2:
			templ.append(tile)
			if tile != None:
				tile.updateAll(screen)
			if count >= (size[1]//TILEWIDTH):
				tiles.append(templ)
				templ = []

		#Draw/updates the tiles to the screen
		for tile in dirtytiles:
			if tile != None:
				tile.updateAll(screen)

		#print(len(dirtytiles))
		dirtytiles = []

		#Draw/updates grass tile

		#Draws/updates characters
		for character in objectLists[0]:
			character.updateAll(screen)
			dirtytiles.extend(character.getDirty(tiles, size[0]//TILEWIDTH, len(tiles)))
		
		#Draws/updates players
		for player in objectLists[1]:
			player.updateAllPlayers(screen)
			dirtytiles.extend(player.getDirty(tiles, size[0]//TILEWIDTH, len(tiles)))

		time.Clock().tick(FPS)

		display.flip()  

