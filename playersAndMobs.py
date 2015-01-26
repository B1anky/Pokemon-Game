import BasicSprite
import Character
import Player
import spriteManagement
from pygame import *
import mapManagement
from scale import *

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

	#x and y draw coords must be TILEWIDTH * coords

	character1 = Character.Character(redDownIdle, redLeftIdle, redUpIdle, \
		redRightIdle, redDownWalkList, redLeftWalkList, redUpWalkList, \
		redRightWalkList, redDefault, 10, 0, 0, 0, 0, "right", redWidest, \
		redTallest, TILEWIDTH * 3, TILEWIDTH * 5, False, False, False, False, False, \
		False, "idle", "ground", "Red", redLeftIdle, 0, 3, clock, clock.tick()/100.0, \
		(3, 5))

	player1 = Player.Player(redDownIdle, redLeftIdle, redUpIdle, \
		redRightIdle, redDownWalkList, redLeftWalkList, redUpWalkList, \
		redRightWalkList, redDefault, 10, 0, 0, 0, 0, "right", redWidest, \
		redTallest, TILEWIDTH * 5, TILEWIDTH * 5, False, False, False, False, False, \
		False, "idle", "ground", "Red", redRightIdle, 0, 3, clock, clock.tick()/100.0,\
		(5,5), False, False, False, False, False, 0, 0, [0][0])

	characterList = []
	playerList = []
	characterList.append(character1)
	playerList.append(player1)

	returnLists = []
	returnLists.append(characterList)
	returnLists.append(playerList)

	return returnLists