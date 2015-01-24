#Creates all of the sprites and returns them in seperate, neat lists
from pygame import *
from BasicSprite import BasicSprite

MAIN_SPRITES = image.load("spriteSheet.gif")

def redDownIdleAnim():
	redDownIdle = BasicSprite("Red's down Idle anim.", MAIN_SPRITES, 481, 495, 387, 406, 5, 0, 0)
	return redDownIdle

def redDownWalkAnim():
	redWalkDown1 = BasicSprite("Red's down walk anim. 1", MAIN_SPRITES, 496, 511, 387, 406, 5, 0, 0)
	redWalkDown2 = BasicSprite("Red's down walk anim. 2", MAIN_SPRITES, 512, 527, 387, 406, 5, 0, 0)
	redWalkDownAnimList = [redWalkDown1, redWalkDown2]
	return redWalkDownAnimList

def redLeftIdleAnim():
	redLeftIdle = BasicSprite("Red's left Idle anim.", MAIN_SPRITES, 528, 542, 387, 406, 5, 0, 0)
	return redLeftIdle

def redLeftWalkAnim():
	redWalkLeft1 = BasicSprite("Red's left walk anim. 1", MAIN_SPRITES, 544, 558, 387, 406, 5, 0, 0)
	redWalkLeft2 = BasicSprite("Red's left walk anim. 2", MAIN_SPRITES, 560, 574, 387, 406, 5, 0, 0)
	redWalkLeftAnimList = [redWalkLeft1, redWalkLeft2]
	return redWalkLeftAnimList

def redUpIdleAnim():
	redUpIdle = BasicSprite("Red's up Idle anim.", MAIN_SPRITES, 578, 592, 387, 406, 5, 0, 0)
	return redUpIdle

def redUpWalkAnim():
	redWalkUp1 = BasicSprite("Red's up walk anim. 1", MAIN_SPRITES, 594, 608, 387, 406, 5, 0, 0)
	redWalkUp2 = BasicSprite("Red's up walk anim. 2", MAIN_SPRITES, 609, 623, 387, 406, 5, 0, 0)
	redWalkUpAnimList = [redWalkUp1, redWalkUp2]
	return redWalkUpAnimList

def redRightIdleAnim():
	redRightIdle = BasicSprite("Red's right Idle anim.", MAIN_SPRITES, 625, 639, 387, 406, 5, 0, 0)
	return redRightIdle

def redRightWalkAnim():
	redWalkRight1 = BasicSprite("Red's right walk anim. 1", MAIN_SPRITES, 641, 655, 388, 406, 5, 0, 0)
	redWalkRight2 = BasicSprite("Red's right walk anim. 2", MAIN_SPRITES, 657, 671, 388, 406, 5, 0, 0)
	redWalkRightAnimList = [redWalkRight1, redWalkRight2]
	return redWalkRightAnimList

def redWidestSprite():
	redWalkDown1 = BasicSprite("Red's down walk anim. 1", MAIN_SPRITES, 496, 511, 387, 406, 5, 0, 0)
	return redWalkDown1

def redTallestSprite():
	redDownIdle = BasicSprite("Red's down Idle anim.", MAIN_SPRITES, 481, 495, 387, 406, 5, 0, 0)
	return redDownIdle

def redDefault():
	redDownIdle = BasicSprite("Red's down Idle anim.", MAIN_SPRITES, 481, 495, 387, 406, 5, 0, 0)
	return redDownIdle