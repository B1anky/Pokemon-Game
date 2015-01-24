#Character class which utilizes certain aspects of 
#Basic Sprite class objects, but does not extend

from pygame import *
from scale import *
import mainLoopModule

#Credit for basic structure to Michael Melnik Jr. (Xvladin)
class Character:
	def __init__(self, downIdleAnim = None, leftIdleAnim = None, upIdleAnim = None, \
		rightIdleAnim = None,  downWalkAnimList = [], \
		leftWalkAnimList = [], upWalkAnimList = [], rightWalkAnimList = [], \
		defaultSprite = None, animTimer = 5, walkAnimCtr = 0, \
		walkAnimCount = 0, idleAnimCtr = 0, idleAnimCount = 0, \
		face = "down", widestSprite = None, tallestSprite = None,\
		speed = 1, maxSpeed = 20, rightSpeed = 0, leftSpeed = 0,\
		upSpeed = 0, downSpeed = 0, x = 200, y = 200, canLeaveScreen = True,\
		isOffBottom = False, isOffTop = False, isOffRight = False, isOffLeft = False,\
		isOffScreen = False, status = "idle", isOn = "nothing", name = None, speedStat = 1, \
		allSpeeds = 0, currentSprite = None, walkCoolDown = 0, walkDelay = 5, \
		tileClock = time.Clock(), delta = 0):

		#Sprite List initializers
		self.__downIdleAnim = downIdleAnim
		self.__leftIdleAnim = leftIdleAnim
		self.__upIdleAnim = upIdleAnim
		self.__rightIdleAnim = rightIdleAnim

		self.__downWalkAnimList = downWalkAnimList
		self.__leftWalkAnimList = leftWalkAnimList
		self.__upWalkAnimList = upWalkAnimList
		self.__rightWalkAnimList = rightWalkAnimList

		#Temporary current sprite for animating
		self.__currentSprite = currentSprite

		#General animation attributes initializers
		self.__animTimer = animTimer
		self.__walkAnimCtr = walkAnimCtr
		self.__walkAnimCount = walkAnimCount
		self.__idleAnimCtr = idleAnimCtr
		self.__idleAnimCount = idleAnimCount

		#Movement initializers
		self.__face = face
		self.__widestSprite = widestSprite
		self.__tallestSprite = tallestSprite
		self.__speed = speed
		self.__maxSpeed = maxSpeed
		self.__rightSpeed = rightSpeed
		self.__leftSpeed = leftSpeed
		self.__upSpeed = upSpeed
		self.__downSpeed = downSpeed

		#**Special movement differential attributes not attached to object
		self.__dx = self.__leftSpeed - self.__rightSpeed
		self.__dy = self.__upSpeed - self.__downSpeed

		#Rest of normal movement initializers
		self.__x = x
		self.__y = y
		self.__targetX = x 
		self.__targetY = y
		self.__spacing = TILEWIDTH/SCALE/4

		#Movement limiting attribute initializers
		self.__canLeaveScreen = canLeaveScreen
		self.__isOffBottom = isOffBottom
		self.__isOffTop = isOffTop
		self.__isOffRight = isOffRight
		self.__isOffLeft = isOffLeft
		self.__isOffScreen = isOffScreen
		
		#Miscellaneous attribute(s)
		self.__status = status
		self.__isOn = isOn

		#Stats
		self.__name = name
		self.__speedStat = speedStat
		self.__allSpeeds = rightSpeed + leftSpeed + upSpeed + downSpeed

		#tile stuff
		self.__walkCoolDown = walkCoolDown
		self.__walkDelay = walkDelay
		self.__tileClock = tileClock
		self.__delta = delta

	#Now for the basic attribute mutators/accessors... *sigh* FOR SAFETY
	
	def setDownIdleAnim(self, downIdleAnim):
		self.__downIdleAnim = downIdleAnim

	def returnDownIdleAnim(self):
		return self.__downIdleAnim

	def setLeftIdleAnim(self, leftIdleAnim):
		self.__leftIdleAnim = leftIdleAnim

	def returnLeftIdleAnim(self):
		return self.__leftIdleAnim

	def setUpIdleAnim(self, upIdleAnim):
		self.__upIdleAnim = upIdleAnim

	def returnUpIdleAnim(self):
		return self.__upIdleAnim

	def setRightIdleAnim(self, rightIdleAnim):
		self.__rightIdleAnim = rightIdleAnim

	def returnRightIdleAnim(self):
		return self.__rightIdleAnim

	def setDownWalkAnimList(self, downWalkAnimList):
		self.__downWalkAnimList = downWalkAnimList

	def returnDownWalkAnimList(self):
		return self.__downWalkAnimList

	def setLeftWalkAnimList(self, leftWalkAnimList):
		self.__leftWalkAnimList = leftWalkAnimList

	def returnLeftWalkAnimList(self):
		return self.__leftWalkAnimList

	def setUpWalkAnimList(self, upWalkAnimList):
		self.__upWalkAnimList = upWalkAnimList

	def returnUpWalkAnimList(self):
		return self.__upWalkAnimList

	def setRightWalkAnimList(self, rightWalkAnimList):
		self.__rightWalkAnimList = rightWalkAnimList

	def returnRightWalkAnimList(self):
		return self.__rightWalkAnimList

	def setDefaultSprite(self, defaultSprite):
		self.__defaultSprite = defaultSprite

	def returnDefaultSprite(self):
		return self.__defaultSprite

	def setAnimTimer(self, animTimer):
		self.__animTimer = animTimer

	def returnAnimTimer(self):
		return self.__animTimer

	def setWalkAnimCtr(self, walkAnimCtr):
		self.__walkAnimCtr = walkAnimCtr

	def returnWalkAnimCtr(self):
		return self.__walkAnimCtr

	def setWalkAnimCount(self, walkAnimCount):
		self.__walkAnimCount = walkAnimCount

	def returnWalkAnimCount(self):
		return self.__walkAnimCount

	def setIdleAnimCtr(self, idleAnimCtr):
		self.__idleAnimCtr = idleAnimCtr

	def returnIdleAnimCtr(self):
		return self.__idleAnimCtr

	def setIdleAnimCount(self, idleAnimCount):
		self.__idleAnimCount = idleAnimCount

	def returnIdleAnimCount(self):
		return self.__idleAnimCount

	def setFace(self, face):
		self.__face = face

	def returnFace(self):
		return self.__face

	def setWidestSprite(self, widestSprite):
		self.__widestSprite = widestSprite

	def returnWidestSprite(self):
		return self.__widestSprite

	def setTallestSprite(self, tallestSprite):
		self.__tallestSprite = tallestSprite

	def returnTallestSprite(self):
		return self.__tallestSprite

	def setSpeed(self, speed):
		self.__speed = speed

	def returnSpeed(self):
		return self.__speed

	def setMaxSped(self, maxSpeed):
		self.__maxSpeed = maxSpeed

	def returnMaxSpeed(self):
		return self.__maxSpeed

	#Dx is the differntial in speed for the next tick for horizontal
	def setRightSpeed(self, rightSpeed):
		self.__rightSpeed = rightSpeed
		self.__dx = self.__leftSpeed - self.__rightSpeed
		self.__allSpeeds = self.__rightSpeed + self.__leftSpeed + self.__upSpeed + self.__downSpeed

	def returnRightSpeed(self):
		return self.__rightSpeed

	#Dx is the differntial in speed for the next tick for horizontal
	def setLeftSpeed(self, leftSpeed):
		self.__leftSpeed = leftSpeed
		self.__dx = self.__leftSpeed - self.__rightSpeed
		self.__allSpeeds = self.__rightSpeed + self.__leftSpeed + self.__upSpeed + self.__downSpeed

	def returnLeftSpeed(self):
		return self.__leftSpeed

	#Doesn't get its own mutator, relies on left/right speed mutators
	def returnDx(self):
		return self.__dx

	#Dy is the differntial in speed for the next tick for vertical
	def setUpSpeed(self, upSpeed):
		self.__upSpeed = upSpeed
		self.__dy = self.__upSpeed - self.__downSpeed
		self.__allSpeeds = self.__rightSpeed + self.__leftSpeed + self.__upSpeed + self.__downSpeed

	def returnUpSpeed(self):
		return self.__upSpeed

	#Dy is the differntial in speed for the next tick for vertical
	def setDownSpeed(self, downSpeed):
		self.__downSpeed = downSpeed
		self.__dy = self.__upSpeed - self.__downSpeed
		self.__allSpeeds = self.__rightSpeed + self.__leftSpeed + self.__upSpeed + self.__downSpeed

	def returnDownSpeed(self):
		return self.__downSpeed

	#Doesn't get its own mutator, relies on up/down speed mutators
	def returnDy(self):
		return self.__dy

	#Used for status indicator to check whether idle, walking, running, or on bike
	def returnAllSpeeds(self):
		return self.__allSpeeds

	def setX(self, x):
		self.__x = x

	def returnX(self):
		return self.__x

	def setTargetX(self, targetX):
		self.__targetX = targetX

	def returnTargetX(self):
		return self.__targetX

	def setY(self, y):
		self.__y = y

	def returnY(self):
		return self.__y

	def setTargetY(self, targetY):
		self.__targetY = targetY

	def returnTargetY(self):
		return self.__targetY

	def setCanLeaveScreen(self, canLeaveScreen):
		self.__canLeaveScreen = canLeaveScreen

	def returnCanLeaveScreen(self):
		return self.__canLeaveScreen

	def setIsOffBottom(self, isOffBottom):
		self.__isOffBottom = isOffBottom

	def returnIsOffBottom(self):
		return self.__isOffBottom

	def setIsOffTop(self, isOffTop):
		self.__isOffTop = isOffTop

	def returnIsOffTop(self):
		return self.__isOffTop

	def setIsOffRight(self, isOffRight):
		self.__isOffRight = isOffRight

	def returnIsOffRight(self):
		return self.__isOffRight

	def setIsOffLeft(self, isOffLeft):
		self.__isOffLeft = isOffLeft

	def returnIsOffLeft(self):
		return self.__isOffLeft

	def setIsOffScreen(self, isOffScreen):
		self.__isOffScreen = isOffScreen

	def returnIsOfScreen(self):
		return self.__isOffScreen

	def setStatus(self, status):
		self.__status = status

	def returnStatus(self):
		return self.__status

	def setIsOn(self, isOn):
		self.__isOn = isOn

	def returnIsOn(self):
		return self.__isOn

	def setName(self, name):
		self.__name = name

	def returnName(self):
		return self.__name

	def setSpeedStat(self, speedStat):
		self.__speedStat = speedStat

	def returnSpeedStat(self):
		return self.__speedStat

	def setAllSpeeds(self, allSpeedsl):
		self.__allSpeeds = self.__rightSpeed + self.__leftSpeed + self.__upSpeed + self.__downSpeed

	def returnAllSpeeds(self):
		return self.__allSpeeds

	def setCurrentSprite(self, currentSprite):
		self.__currentSprite = currentSprite

	def returnCurrentSprite(self):
		return self.__currentSprite

	def setWalkCoolDown(self, walkCoolDown):
		self.__walkCoolDown = walkCoolDown

	def returnWalkCoolDown(self):
		return self.__walkCoolDown

	def setWalkDelay(self, walkDelay):
		self.__walkDelay = walkDelay

	def returnWalkDelay(self):
		return self.__walkDelay

	def setTileClock(self, tileClock):
		self.__tileClock = tileClock.tick()

	def returnTileClock(self):
		return self.__tileClock

	def setDelta(self, delta):
		self.__delta = delta

	def returnDelta(self):
		return self.__delta

	def setSpacing(self):
		self.__spacing = TILEWIDTH//SCALE//4 #self.returnWalkDelay()

	def returnSpacing(self):
		return self.__spacing

	#Above is all initialization methods, below will be the rest of the methods
	#Most of this is credited to Michael Melnik Jr. (Xvladin)
	#I've privatized 100% of the methods and attributes, dx and dy aren't 
	#object atributes, therefore don't receive a separate mutator

	#Basic movement methods
	def moveRight(self):
		#if self.returnRightSpeed() < self.returnMaxSpeed():
		#	self.setRightSpeed(self.returnSpeedStat() * self.returnSpeed())
		self.setRightSpeed(self.returnSpeedStat() * self.returnSpeed())
		self.setTargetX(self.returnTargetX() + TILEWIDTH)
		self.setStatus("walking") 

	def moveLeft(self):
		self.setLeftSpeed(self.returnSpeedStat() * self.returnSpeed())
		self.setTargetX(self.returnTargetX() - TILEWIDTH)
		self.setStatus("walking") 

	def moveUp(self):
		self.setUpSpeed(self.returnSpeedStat() * self.returnSpeed())
		self.setTargetY(self.returnTargetY() - TILEWIDTH)
		self.setStatus("walking") 

	def moveDown(self):
		self.setDownSpeed(self.returnSpeedStat() * self.returnSpeed())
		self.setTargetY(self.returnTargetY() + TILEWIDTH)
		self.setStatus("walking") 

	def updateStatus(self):
		if self.returnAllSpeeds() == 0:
			self.setStatus("idle")
		else:
			self.setStatus("walking") 

	def animation(self):
		#Idle while facing down
		if self.returnStatus() == "idle" and self.returnFace() == "down":
			self.setCurrentSprite(self.returnDownIdleAnim())

		#Idle while facing left
		if self.returnStatus() == "idle" and self.returnFace() == "left":
			self.setCurrentSprite(self.returnLeftIdleAnim())

		#Idle while facing up
		if self.returnStatus() == "idle" and self.returnFace() == "up":
			self.setCurrentSprite(self.returnUpIdleAnim())

		#Idle while facing right
		if self.returnStatus() == "idle" and self.returnFace() == "right":
			self.setCurrentSprite(self.returnRightIdleAnim())

		#Walking while facing down
		if self.returnStatus() == "walking" and self.returnFace() == "down":
			self.setCurrentSprite(self.returnDownWalkAnimList()[self.returnWalkAnimCount()])
			self.setWalkAnimCtr(self.returnWalkAnimCtr() + 1)
			if self.returnWalkAnimCtr() == self.returnAnimTimer():
				self.setWalkAnimCount(self.returnWalkAnimCount() + 1)
				if self.returnWalkAnimCount() > (len(self.returnDownWalkAnimList()) - 1):
					self.setWalkAnimCount(0)
				self.setWalkAnimCtr(0)

		#Walking while facing left
		if self.returnStatus() == "walking" and self.returnFace() == "left":
			self.setCurrentSprite(self.returnLeftWalkAnimList()[self.returnWalkAnimCount()])
			self.setWalkAnimCtr(self.returnWalkAnimCtr() + 1)
			if self.returnWalkAnimCtr() == self.returnAnimTimer():
				self.setWalkAnimCount(self.returnWalkAnimCount() + 1)
				if self.returnWalkAnimCount() > (len(self.returnLeftWalkAnimList()) - 1):
					self.setWalkAnimCount(0)
				self.setWalkAnimCtr(0)

		#Walking while facing up
		if self.returnStatus() == "walking" and self.returnFace() == "up":
			self.setCurrentSprite(self.returnUpWalkAnimList()[self.returnWalkAnimCount()])
			self.setWalkAnimCtr(self.returnWalkAnimCtr() + 1)
			if self.returnWalkAnimCtr() == self.returnAnimTimer():
				self.setWalkAnimCount(self.returnWalkAnimCount() + 1)
				if self.returnWalkAnimCount() > (len(self.returnUpWalkAnimList()) - 1):
					self.setWalkAnimCount(0)
				self.setWalkAnimCtr(0)

		#Walking while facing right
		if self.returnStatus() == "walking" and self.returnFace() == "right":
			self.setCurrentSprite(self.returnRightWalkAnimList()[self.returnWalkAnimCount()])
			self.setWalkAnimCtr(self.returnWalkAnimCtr() + 1)
			if self.returnWalkAnimCtr() == self.returnAnimTimer():
				self.setWalkAnimCount(self.returnWalkAnimCount() + 1)
				if self.returnWalkAnimCount() > (len(self.returnRightWalkAnimList()) - 1):
					self.setWalkAnimCount(0)
				self.setWalkAnimCtr(0)			


		if self.returnTargetX() > self.returnX():
			self.setX(self.returnX() + self.returnSpacing())
		if self.returnTargetX() < self.returnX():
			self.setX(self.returnX() - self.returnSpacing())
		if self.returnTargetY() > self.returnY():
			self.setY(self.returnY() + self.returnSpacing())	
		if self.returnTargetY() < self.returnY():
			self.setY(self.returnY() - self.returnSpacing())	

	def checkMoving(self, dir):
		result = {
		  "up": (self.returnPushingDown() or self.returnPushingLeft() or self.returnPushingRight()),
		  "down": (self.returnPushingUp() or self.returnPushingLeft() or self.returnPushingRight()),
		  "left": (self.returnPushingUp() or self.returnPushingDown() or self.returnPushingRight()),
		  "right": (self.returnPushingUp() or self.returnPushingDown() or self.returnPushingLeft()),
		  "idle": (self.returnPushingUp() or self.returnPushingDown() or self.returnPushingLeft() or self.returnPushingRight())
		}[dir]
		return result
	
	#dx and dy are private but don't call a mutator to change since neither are object attributes
	#def updateCoords(self):
		#if self.returnWalkCoolDown() > 0:
			#self.__dx = (self.returnRightSpeed() - self.returnLeftSpeed())
			#self.__dy = (self.returnDownSpeed() - self.returnUpSpeed())

			#self.setAllSpeeds(self.returnRightSpeed() + self.returnLeftSpeed() + self.returnUpSpeed() + self.returnDownSpeed())

			#self.setX(self.returnX() + self.returnDx())
			#self.setY(self.returnY() + self.returnDy())

	def updateTileClock(self):
		#This is for changing from pixel based to time based movement for tiles
		self.setDelta(self.returnTileClock().tick()/100.0)		
		self.setWalkCoolDown(self.returnWalkCoolDown() - self.returnDelta())


	#Drawing method
	def draw(self, screen):
		screen.blit(self.returnCurrentSprite().returnScaledPicture(), \
			(self.returnX() + self.returnCurrentSprite().returnAdjustX(),\
			self.returnY() + self.returnCurrentSprite().returnAdjustY()))

	def updateAll(self, screen):
		self.updateTileClock()
		self.animation()
		#self.updateStatus()
		self.updateCoords()
		self.draw(screen)

	def __str__(self):
		return  "\nName: " + str(self.__name)   + \
				"\nDown idle sprite: " + str(self.__downIdleAnim) + \
				"\nLeft idle sprite: " + str(self.__leftIdleAnim) + \
				"\nUp idle sprite: " + str(self.__upIdleAnim) + \
				"\nRight idle sprite: " + str(self.__rightIdleAnim) + \
				"\nDown walking animation list: " + str(self.__downWalkAnimList) + \
				"\nLeft walking animation list: " + str(self.__leftWalkAnimList) + \
				"\nUp walking animation list: " + str(self.__upWalkAnimList) + \
				"\nRight walking animation list: " + str(self.__rightWalkAnimList) + \
				"\nAnimation Timer: " + str(self.__animTimer) + \
				"\nWalking animation counter: " + str(self.__walkAnimCtr) + \
				"\nWalking animation count: " + str(self.__walkAnimCount) + \
				"\nIdle animation counter: " + str(self.__idleAnimCtr) + \
				"\nIdle animation count: " + str(self.__idleAnimCount) + \
				"\nFacing: " + str(self.__face) + \
				"\nWidest sprite: " + str(self.__widestSprite) + \
				"\nTallest sprite: "  + str(self.__tallestSprite) + \
				"\nSpeed: " + str(self.__speed) + \
				"\nMax speed: " + str(self.__maxSpeed) + \
				"\nRight speed: " + str(self.__rightSpeed) + \
				"\nLeft speed: " + str(self.__leftSpeed) + \
				"\nUp speed: " + str(self.__upSpeed) + \
				"\nDown speed: " + str(self.__downSpeed) + \
				"\nDx: " + str(self.__dx) + \
				"\nDy: " + str(self.__dy) + \
				"\nX Coordinate: " + str(self.__x) + \
				"\nY Coordinate: " + str(self.__y) + \
				"\nCan Leave Screen: " + str(self.__canLeaveScreen) + \
				"\nIs off bottom of screen: " + str(self.__isOffBottom) + \
				"\nIs off top of screen: " + str(self.__isOffTop) + \
				"\nIs off right of screen: " + str(self.__isOffRight) + \
				"\nIs off left of screen: " + str(self.__isOffLeft) + \
				"\nIs off screen: " + str(self.__isOffScreen) + \
				"\nStatus: " + str(self.__status) + \
				"\nIs on: " + str(self.__isOn) + \
				"\nSpeed stat: " + str(self.__speedStat) +\
				"\nAll speeds together: " + str(self.__allSpeeds)