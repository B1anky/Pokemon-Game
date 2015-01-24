import BasicSprite
import Character
import Player
import spriteManagement
from pygame import *
import mapManagement

def createPlayers():
	createRed()

#def createCharacter():
	#character1 = Character.Character()

def createRed():
	redDownIdle = spriteManagement.redDownIdleAnim()
	redLeftIdle = spriteManagement.redLeftIdleAnim()
	redUpIdle = spriteManagement.redUpIdleAnim()
	redRightIdle = spriteManagement.redRightIdleAnim()

	redDownWalkList = spriteManagement.redDownWalkAnim()
	redLeftWalkList = spriteManagement.redLeftWalkAnim()
	redUpWalkList = spriteManagement.redUpWalkAnim()
	redRightWalkList = spriteManagement.redRightWalkAnim()

	redTallest = spriteManagement.redWidestSprite()
	redWidest = spriteManagement.redTallestSprite()
	redDefault = spriteManagement.redDefault()

	clock = time.Clock()

	character1 = Character.Character(redDownIdle, redLeftIdle, redUpIdle, \
		redRightIdle, redDownWalkList, redLeftWalkList, redUpWalkList, \
		redRightWalkList, redDefault, 10, 0, 0, 0, 0, "left", redWidest, \
		redTallest, mapManagement.createTown1Grass()[0].returnDrawCoords()[0], mapManagement.createTown1Grass()[0].returnDrawCoords()[1], \
		False, False, False, False, False, \
		False, "walking", "ground", "Red", redLeftIdle, 0, 3, clock, clock.tick()/100.0, \
		(mapManagement.createTown1Grass()[0].returnTileCoords()[0], mapManagement.createTown1Grass()[0].returnDrawCoords()[1]))

	player1 = Player.Player(redDownIdle, redLeftIdle, redUpIdle, \
		redRightIdle, redDownWalkList, redLeftWalkList, redUpWalkList, \
		redRightWalkList, redDefault, 10, 0, 0, 0, 0, "right", redWidest, \
		redTallest, mapManagement.createTown1Grass()[0].returnDrawCoords()[0], mapManagement.createTown1Grass()[0].returnDrawCoords()[1],\
		False, False, False, False, False, \
		False, "idle", "ground", "Red", redRightIdle, 0, 3, clock, clock.tick()/100.0,\
		(mapManagement.createTown1Grass()[0].returnTileCoords()[0], mapManagement.createTown1Grass()[0].returnTileCoords()[1]), \
		False, False, False, False, False)

	characterList = []
	playerList = []
	characterList.append(character1)
	playerList.append(player1)

	returnLists = []
	returnLists.append(characterList)
	returnLists.append(playerList)

	return returnLists