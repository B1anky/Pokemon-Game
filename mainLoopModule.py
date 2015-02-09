from pygame import *
import playersAndMobs
import mapManagement
import windowControl
from scale import *
from Camera import *
FPS = 60

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
	tileList1 = mapManagement.createTown1Dirt()
	tileList2 = mapManagement.createTown1Grass()
	tileList3 = mapManagement.createTown1Trees()
	allTiles.append(tileList2)
	allTiles.append(tileList1)
	allTiles.append(tileList3)

	#Immediately maximizes the screen upon starting, calls method in windowControl module
	windowControl.SDL_Maximize()

	'''
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
		#@tile.updateAll(screen, cam)
		tx += 1
		'''

	while keepGoing:
		screen.fill((0,0,0))
		for tileList in allTiles:
			for tiles in tileList:
				tiles.updateAll(screen, cam)
		'''

		#Updates the display/objects by calling the objects' class update methods

		#Dirty tile optimizations, only updates necessary surrounding tile coords
		#Helps CPU when scale is very low
		#for dirtyObjectTilesList in allDirtyTilesList:
			#for dirtyTupleCoords in dirtyObjectTilesList:
				
				DTCx = dirtyTupleCoords[0]
				DTCy = dirtyTupleCoords[1]
				tile = masterTileList[DTCx][DTCy]
				if tile == None:
					continue
				tile.updateAll(screen, cam)
				coordsList = []
				allDirtyTilesList = []
				
				#for tiles in tileList2:
					#if tiles.returnTileCoords() == dirtyTupleCoords:
						#tiles.updateAll(screen, cam)
						#coordsList = []
						#allDirtyTilesList = []
						'''

		#Draws/updates characters
		for character in objectLists[0]:
			character.updateAll(screen, cam)
			#NPCs can currently interact with notWalkableOn tiles correctly
			#character.moveLeft(allTiles)
			#allDirtyTilesList.append(character.getDirty(coordsList, size[0]//TILEWIDTH, size[1]//TILEWIDTH))
		
		#Draws/updates players
		for player in objectLists[1]:
			#allDirtyTilesList.append(player.getDirty(coordsList, size[0]//TILEWIDTH, size[1]//TILEWIDTH))
			player.updateAllPlayers(screen, cam, allTiles)
			cam.update(player)
			
		time.Clock().tick(FPS)

		display.flip()  


#comes from help at:
#http://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame

def simple_camera(camera, target_rect):
	l, t, _, _ = target_rect # l = left,  t = top
	_, _, w, h = camera      # w = width, h = height
	return Rect(-l+(size[0]//2), -t+(size[1]//2), w, h)

'''
def complex_camera(camera, target_rect):
	l, t, _, _ = target_rect
	_, _, w, h = camera
	l, t, _, _ = -l+(size[0]//2), -t+(size[1]//2), w, h # center player

	l = min(0, l)
	l = max(-(w-(size[0]//4)), l)
	t = max(-(h-(size[1]//4)), t)
	t = min(0, t)

	return Rect(l, t, w, h)

def new_camera(camera, target_rect):
	l,t, _, _ = target_rect
	_, _, w, h = camera

	ret = None

	if l - (size[0]//2) <= 0:
		print(1)
		ret = Rect(-l, -t, w, h)
	elif t - (size[1]//2) <= 0:
		print(2)
		ret = Rect(-l, -t, w, h)
	elif l+(size[0]//2) >  size[0]:
		print(2)
		ret = Rect(-l, -t, w, h)
	elif t+(size[1]//2) >  size[1]:
		print(2)
		ret = Rect(-l, -t, w, h)
	else:
		ret = Rect(-l+(size[0]//2), -t+(size[1]//2), w, h)

	return ret
'''