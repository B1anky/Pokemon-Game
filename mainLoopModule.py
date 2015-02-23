from pygame import *
import playersAndMobs
import mapManagement
import windowControl
from scale import *
from Camera import *
FPS = 60
TILE_DEBUG = 0


#Main window loop which will blit everything to screen
def run():
	init()
	keepGoing = True
	video_flags = RESIZABLE
	screen = display.set_mode(size, video_flags)

	#create camera object	
	camera_x = 0
	camera_y = 0
	cam = Camera(simple_camera, camera_x, camera_y)


	#Creates the player object
	objectLists = playersAndMobs.createRed()

	allTiles = []
	allTiles = mapManagement.createMaps()
	tileList1 = mapManagement.getDirtList()
	tileList2 = mapManagement.getGrassList()
	tileList3 = mapManagement.createTown1Trees()
	#allTiles.append(tileList2)
	#allTiles.append(tileList1)
	allTiles.append(tileList3)

	#Immediately maximizes the screen upon starting, calls method in windowControl module
	windowControl.SDL_Maximize()

	while keepGoing:
		screen.fill((0,0,0))
		
		if TILE_DEBUG:
			for tile in tileList3:
				print("Tile: " + str(tile.returnTileCoords()))
		for tileList in allTiles:
			for tiles in tileList:
				tiles.updateAll(screen, cam)

		#Draws/updates characters
		for character in objectLists[0]:
			character.updateAll(screen, cam)
			#NPCs can currently interact with notWalkableOn tiles correctly
			#character.moveLeft(allTiles)
		
		#Draws/updates players
		for player in objectLists[1]:
			player.updateAllPlayers(screen, cam, allTiles)
			if TILE_DEBUG:
				print("player: " + str(player.returnTileCoords()))
			cam.update(player)
			
		time.Clock().tick(FPS)

		display.flip()  

#comes from help at:
#http://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame

def simple_camera(camera, target_rect):
	l, t, _, _ = target_rect # l = left,  t = top
	_, _, w, h = camera      # w = width, h = height
	return Rect(-l+(size[0]//2), -t+(size[1]//2), w, h)
