from pygame import *
import playersAndMobs
import mapManagement
import windowControl

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


	while keepGoing:
		#Updates the display/objects by calling the objects' class update methods
		
		#Draw/updates the tiles to the screen
		for tile in tileList2:
			tile.updateAll(screen)

		#Draw/updates grass tile


		#Draws/updates characters
		for character in objectLists[0]:
			character.updateAll(screen)
		
		#Draws/updates players
		for player in objectLists[1]:
			player.updateAllPlayers(screen)

		time.Clock().tick(FPS)

		display.flip()  

