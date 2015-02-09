#The class for what the player controls, extends Character
from Character import Character
from pygame import *
from scale import *
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
				x = 200, y = 200, canLeaveScreen = True,\
				isOffBottom = False, isOffTop = False, isOffRight = False, isOffLeft = False,\
				isOffScreen = False, status = "idle", isOn = "nothing", name = None, \
				currentSprite = None, walkCoolDown = 0, walkDelay = 5,  \
				tileClock = None, delta = 0, tileCoords = (0,0), number = 0, pushingRight = False, \
				pushingLeft = False, pushingUp = False, pushingDown = False, isPushing = False, \
				cameraX = 0, cameraY = 0, mapData = [0][0]):

		Character.__init__(self, downIdleAnim, leftIdleAnim, upIdleAnim, \
							rightIdleAnim,  downWalkAnimList, \
							leftWalkAnimList, upWalkAnimList, rightWalkAnimList, \
							defaultSprite, animTimer, walkAnimCtr, \
							walkAnimCount, idleAnimCtr, idleAnimCount, \
							face, widestSprite, tallestSprite,\
							x, y, canLeaveScreen,\
							isOffBottom, isOffTop, isOffRight, isOffLeft,\
							isOffScreen, status, isOn, name, \
							currentSprite, walkCoolDown, walkDelay, tileClock, \
							delta, tileCoords)

		self.__number = number
		self.__pushingRight = pushingRight
		self.__pushingLeft = pushingLeft
		self.__pushingUp = pushingUp
		self.__pushingDown = pushingDown
		self.__cameraX = cameraX
		self.__cameraY = cameraY
		self.__mapData = mapData
		self.__count = 0

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

	def setCameraX(self, cameraX):
		self.__cameraX = cameraX

	def returnCameraX(self):
		return self.__cameraX

	def setCameraY(self, cameraY):
		self.__cameraY = cameraY

	def returnCameraY(self):
		return self.__cameraY

	def setAllPush(self, boo):
		self.setPushingLeft(boo)
		self.setPushingRight(boo)
		self.setPushingUp(boo)
		self.setPushingDown(boo)

	#Below is what allows the user to interact with the sprite and window
	def playerControl(self, screen, nonOccludedtilesList, allTiles):
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


		if not self.checkMoving("idle"):
			self.setStatus("idle")

		if self.returnTargetX() == self.returnX() and self.returnTargetY() == self.returnY():
			self.setAllPush(False) 

			#A key is pressed
			if keyPressed[K_a] and not self.checkMoving("left"):
				self.setPushingLeft(True)
				self.setFace("left")
				self.moveLeft(allTiles)
				self.setStatus("walking")

			#D key is pressed
			if keyPressed[K_d] and not self.checkMoving("right"):
				self.setPushingRight(True)
				self.setFace("right")
				self.moveRight(allTiles)
				self.setStatus("walking")

			#W key is pressed
			if keyPressed[K_w] and not self.checkMoving("up"):
				self.setPushingUp(True)
				self.setFace("up")
				self.moveUp(allTiles)
				self.setStatus("walking")
				
			#S key is pressed
			if keyPressed[K_s] and not self.checkMoving("down"):
				self.setPushingDown(True)
				self.setFace("down")
				self.moveDown(allTiles)
				self.setStatus("walking")
	
	def UpdateMapAccordingToMvt(self, screen, nonOccludedtilesList):
		#check if player has reached bounds of screen view
		return
		#If off left
		if self.returnTileCoords()[0] < 0:
			self.setIsOffLeft(True)
			
		#If off right
		if self.returnTileCoords()[0] > (size[0]//TILEWIDTH):
			self.setIsOffRight(True)

		#If off top
		if self.returnTileCoords()[1] < 0:
			self.setIsOffTop(True)

		#If off bottom
		if self.returnTileCoords()[1] > size[1]//TILEWIDTH:
			self.setIsOffBottom(True)

			#if they have, shift all tiles in the opposite direction of the movement
		'''
		for tileList in nonOccludedtilesList:
			if tileList != None:
				for tile in tileList:
					if(tile != None):
						#if (self.checkTileOnScreen(tile.returnDrawCoords()[0], tile.returnDrawCoords()[1])):
						if self.returnIsOffLeft():
							tile.setDrawCoords((tile.returnDrawCoords()[0] + TILEWIDTH, tile.returnDrawCoords()[1]))
							tile.updateAll(screen)
							self.setIsOffLeft(False)

						elif self.returnIsOffRight():
							tile.setTileCoords((tile.returnTileCoords()[0] + 1, tile.returnTileCoords()[1]))
							#tile.setDrawCoords((tile.returnDrawCoords()[0] - TILEWIDTH, tile.returnDrawCoords()[1]))
							tile.updateAll(screen)
							self.__count+=1
							self.setIsOffRight(False)

						elif self.returnIsOffTop():
							tile.setDrawCoords((80, 240))
							tile.updateAll(screen)
							self.setIsOffTop(False)

						elif self.returnIsOffBottom():
							tile.setDrawCoords((tile.returnDrawCoords()[0], tile.returnDrawCoords()[1] - TILEWIDTH))
							tile.updateAll(screen)
							self.setIsOffBottom(False)
		'''
		if self.returnIsOffLeft():
			self.handleIsOffLeft(screen, nonOccludedtilesList)
			self.setIsOffLeft(False)
		elif self.returnIsOffRight():
			self.handleIsOffRight(screen, nonOccludedtilesList)
			self.setIsOffRight(False)
		elif self.returnIsOffTop():
			self.handleIsOffTop(screen, nonOccludedtilesList)
			self.setIsOffTop(False)
		elif self.returnIsOffBottom():
			self.handleIsOffBottom(screen, nonOccludedtilesList)
			self.setIsOffBottom(False)

	def handleIsOffLeft(self, screen, nonOccludedtilesList):
		for tileList in nonOccludedtilesList:
			if tileList != None:
				for tile in tileList:
					if(tile != None):
						#if (self.checkTileOnScreen(tile.returnDrawCoords()[0], tile.returnDrawCoords()[1])):
						if self.returnIsOffLeft():
							tile.setDrawCoords((tile.returnDrawCoords()[0] + TILEWIDTH, tile.returnDrawCoords()[1]))
							tile.updateAll(screen)
							self.setIsOffLeft(False)

						elif self.returnIsOffTop():
							tile.setDrawCoords((80, 240))
							tile.updateAll(screen)
							self.setIsOffTop(False)

						elif self.returnIsOffBottom():
							tile.setDrawCoords((tile.returnDrawCoords()[0], tile.returnDrawCoords()[1] - TILEWIDTH))
							tile.updateAll(screen)
							self.setIsOffBottom(False)

	def handleIsOffRight(self, screen, nonOccludedtilesList):
		for tileList in nonOccludedtilesList:
			for tile in tileList:
				if willBeOffScreen(tile, 1):
					print("off")
					tile.setTileCoords((tile.returnTileCoords()[0] + (size[0]//TILEWIDTH), tile.returnTileCoords()[1]))
					tile.updateAll(screen)
					self.__count+=1

	def handleIsOffTop(self, screen, nonOccludedtilesList):
		return
	def handleIsOffBottom(self, screen, nonOccludedtilesList):
		return

	def willBeOffScreen(self, tile, dir):
		if dir == 0:
			print(0)
		elif dir == 1: #right
			if tile.returnDrawCoords()[0] < TILEWIDTH:
				return True
		elif dir == 2: #top
			print(0)
		elif dir == 3:
			print(0)

	def checkTileOnScreen(self, tilePosX, tilePosY):
		return (tilePosX < TILEWIDTH//TILEWIDTH or tilePosX > 1920//TILEWIDTH \
			or tilePosY < 1920//TILEWIDTH \
			or tilePosY > 1080//TILEWIDTH)
	
	def draw(self, screen, cam):
		imgToDraw = self.returnCurrentSprite().returnScaledPicture()
		fx = self.returnX()
		fy = self.returnY()

		from pygame import Rect
		screen.blit(imgToDraw, cam.apply(Rect(fx, fy, SCALE*16, SCALE*16) ) )

	def rect(self):
		fx = self.returnX()
		fy = self.returnY()
		return Rect(fx, fy, SCALE * 16, SCALE * 16) 
		
	#Calls all methods that manipulate character which need to constantly update
	def updateAllPlayers(self, screen, nonOccludedtilesList, cam, allTiles):
		self.animation()
		self.updateTileClock()
		self.playerControl(screen, nonOccludedtilesList, allTiles)
		self.UpdateMapAccordingToMvt(screen, nonOccludedtilesList)
		self.draw(screen, cam)
		

	def __str__(self):
		return  Character.__str__(self) + \
				"\nNumber: " + str(self.__number) + \
				"\nIs pushing right: " + str(self.__pushingRight) + \
				"\nIs pushing left: " + str(self.__pushingLeft) + \
				"\nIs pushing up: " + str(self.__pushingUp) + \
				"\nIs pushing down: " + str(self.__pushingDown)