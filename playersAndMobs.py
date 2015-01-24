import BasicSprite
import Character
import Player
import spriteManagement
from pygame import *

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
		redTallest, 1, 20, 5, 0, 0, 0, 0, 800, False, False, False, False, False, \
		False, "walking", "ground", "Red", 5, 0, redLeftIdle, 0, 3, clock, clock.tick()/100.0)

	player1 = Player.Player(redDownIdle, redLeftIdle, redUpIdle, \
		redRightIdle, redDownWalkList, redLeftWalkList, redUpWalkList, \
		redRightWalkList, redDefault, 10, 0, 0, 0, 0, "right", redWidest, \
		redTallest, 1, 20, 0, 0, 0, 0, 1048, 790, False, False, False, False, False, \
		False, "idle", "ground", "Red", 5, 0, redRightIdle, 0, 2.8, clock, clock.tick()/100.0,\
		False, False, False, False, False)

	characterList = []
	playerList = []
	characterList.append(character1)
	playerList.append(player1)

	returnLists = []
	returnLists.append(characterList)
	returnLists.append(playerList)

	return returnLists