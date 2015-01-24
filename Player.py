#The class for what the player controls, extends Character
from Character import Character
from pygame import *
import windowControl
import sys
import mainLoopModule

#Credit for basic structure of class to Michael Melnik Jr. (Xvladin)

class Player(Character):
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
				allSpeeds = 0, currentSprite = None, walkCoolDown = 0, walkDelay = 5,  \
				tileClock = None, delta = 0, number = 0, pushingRight = False, \
				pushingLeft = False, pushingUp = False, pushingDown = False, isPushing = False):

		Character.__init__(self, downIdleAnim, leftIdleAnim, upIdleAnim, \
							rightIdleAnim,  downWalkAnimList, \
							leftWalkAnimList, upWalkAnimList, rightWalkAnimList, \
							defaultSprite, animTimer, walkAnimCtr, \
							walkAnimCount, idleAnimCtr, idleAnimCount, \
							face, widestSprite, tallestSprite,\
							speed, maxSpeed, rightSpeed, leftSpeed,\
							upSpeed, downSpeed, x, y, canLeaveScreen,\
							isOffBottom, isOffTop, isOffRight, isOffLeft,\
							isOffScreen, status, isOn, name, speedStat, \
							allSpeeds, currentSprite, walkCoolDown, walkDelay, tileClock, \
							delta)

		self.__number = number
		self.__pushingRight = pushingRight
		self.__pushingLeft = pushingLeft
		self.__pushingUp = pushingUp
		self.__pushingDown = pushingDown

	def setNumber(self, number):
		self.__number = number

	def returnNumber(self):
		return self.__number

	def setPushingRight(self, pushingRight):
		self.__pushingRight = pushingRight

	def returnPushingRight(self):
		return self.__pushingRight

	def setPushingLeft(self, pushingLeft):
		self.__pushingLeft = pushingLeft

	def returnPushingLeft(self):
		return self.__pushingLeft

	def setPushingUp(self, pushingUp):
		self.__pushingUp = pushingUp

	def returnPushingUp(self):
		return self.__pushingUp

	def setPushingDown(self, pushingDown):
		self.__pushingDown = pushingDown

	def returnPushingDown(self):
		return self.__pushingDown

	#Below is what allows the user to interact with the sprite and window
	def playerControl(self, screen):
		event.pump()
		keyPressed = key.get_pressed()
		for Event in event.get():
			#Allows you to quit by either pressing escape or the window bar exit button
			if Event.type == QUIT:
				quit()
				sys.exit()

			#This calls the functions in windowControl module to resize window
			elif Event.type == KEYDOWN:
				if Event.type == KEYDOWN: 
					if Event.key == K_m:
						if windowControl.SDL_IsMaximized():
							windowControl.SDL_Restore()
						else:
							windowControl.SDL_Maximize()

					if Event.key == K_ESCAPE:
						quit()
						sys.exit()

				elif Event.type == VIDEORESIZE:
					size = Event.size
					mainLoopModule.screen = display.set_mode(size, windowControl.video_flags)
			
		#A key is pressed
		if keyPressed[K_a] and self.returnPushingRight() == False and \
				self.returnPushingUp() == False and \
				self.returnPushingDown() == False and self.returnWalkCoolDown() <= 0:
			self.setPushingLeft(True)
			self.setFace("left")
			self.setWalkCoolDown(self.returnWalkDelay())

		#D key is pressed
		if keyPressed[K_d] and self.returnPushingLeft() == False and \
				self.returnPushingUp() == False and \
				self.returnPushingDown() == False and self.returnWalkCoolDown() <= 0:
			self.setPushingRight(True)
			self.setFace("right")
			self.setWalkCoolDown(self.returnWalkDelay())

		#W key is pressed
		if keyPressed[K_w] and self.returnPushingRight() == False and \
				self.returnPushingLeft() == False and \
				self.returnPushingDown() == False and self.returnWalkCoolDown() <= 0:
			self.setPushingUp(True)
			self.setFace("up")
			self.setWalkCoolDown(self.returnWalkDelay())

		#S key is pressed
		if keyPressed[K_s] and self.returnPushingRight() == False and \
				self.returnPushingUp() == False and \
				self.returnPushingLeft() == False and self.returnWalkCoolDown() <= 0:
			self.setPushingDown(True)
			self.setFace("down")
			self.setWalkCoolDown(self.returnWalkDelay())

		#Checkes to see when animations and walk cycles should end
		if keyPressed[K_a] == False and self.returnWalkCoolDown() <= 0:
			self.setPushingLeft(False)

		if keyPressed[K_d] == False and self.returnWalkCoolDown() <= 0:
			self.setPushingRight(False)

		if keyPressed[K_w] == False and self.returnWalkCoolDown() <= 0:
			self.setPushingUp(False)

		if keyPressed[K_s] == False and self.returnWalkCoolDown() <= 0:
			self.setPushingDown(False)

		#Moves for walk cool down time
		if self.returnWalkCoolDown() > 0:
			self.setStatus("walking")

			if self.returnFace() == "left":
				self.moveLeft()

			if self.returnFace() == "right":
				self.moveRight()

			if self.returnFace() == "up":
				self.moveUp()

			if self.returnFace() == "down":
				self.moveDown()
						
		#Checks to see if walk cool down is over
		if self.returnWalkCoolDown() <= 0:
			self.setStatus("idle")

			if self.returnFace() == "left":
				self.setLeftSpeed(0)

			if self.returnFace() == "right":
				self.setRightSpeed(0)

			if self.returnFace() == "up":
				self.setUpSpeed(0)

			if self.returnFace() == "down":
				self.setDownSpeed(0)

	#Calls all methods that manipulate character which need to constantly update
	def updateAllPlayers(self, screen):
		self.animation()
		self.updateTileClock()
		self.updateStatus()
		self.updateCoords()
		self.playerControl(screen)
		self.draw(screen)

	def __str__(self):
		return  Character.__str__(self) + \
				"\nNumber: " + str(self.__number) + \
				"\nIs pushing right: " + str(self.__pushingRight) + \
				"\nIs pushing left: " + str(self.__pushingLeft) + \
				"\nIs pushing up: " + str(self.__pushingUp) + \
				"\nIs pushing down: " + str(self.__pushingDown)