from pygame import *

#The most basic sprite class for basic attributes that all sprites have in common
class BasicSprite:
	def __init__(self, name, spriteSheet, spriteLeft, spriteRight, spriteTop, spriteBottom,\
				 scale, adjustX, adjustY):
		self.__name = name
		self.__spriteSheet = spriteSheet
		self.__spriteLeft = spriteLeft
		self.__spriteRight = spriteRight
		self.__spriteTop = spriteTop
		self.__spriteBottom = spriteBottom
		self.__scale = scale
		self.__spriteWidth = self.__spriteRight - self.__spriteLeft
		self.__spriteHeight = self.__spriteBottom - self.__spriteTop
		self.__spriteSheet.set_clip(Rect(self.__spriteLeft, self.__spriteTop, self.__spriteWidth, self.__spriteHeight))
		self.__spritePicture = self.__spriteSheet.subsurface(self.__spriteSheet.get_clip())
		self.__scaledSpriteWidth = self.__spriteWidth * self.__scale
		self.__scaledSpriteHeight = self.__spriteHeight * self.__scale
		self.__scaledPicture = transform.scale(self.__spritePicture, (self.__scaledSpriteWidth, self.__scaledSpriteHeight))
		self.__adjustX = adjustX
		self.__adjustY = adjustY

	def setName(self, name):
		self.__name = name

	def returnName(self):
		return self.__name

	def setSpriteSheet(self, spriteSheet):
		self.__spriteSheet = spriteSheet

	def returnSpriteSheet(self):
		return self.__spriteSheet

	def setLeft(self, spriteLeft):
		self.__spriteLeft = spriteLeft
		self.__spriteWidth = self.__spriteRight - self.__spriteLeft

	def returnSpriteLeft(self):
		return self.__spriteLeft

	def setRight(self, spriteRight):
		self.__spriteRight = spriteRight
		self.__spriteWidth = self.__spriteRight - self.__spriteLeft

	def returnSpriteRight(self):
		return self.__spriteRight

	def returnSpriteWidth(self):
		return self.__spriteWidth

	def setTop(self, spriteTop):
		self.__spriteTop = spriteTop
		self.__spriteHeight = self.__spriteBottom - self.__spriteTop

	def returnSpriteTop(self):
		return self.__spriteTop

	def setBottom(self, spriteBottom):
		self.__spriteBottom = spriteBottom
		self.__spriteHeight = self.__spriteBottom - self.__spriteTop

	def returnSpriteBottom(self):
		return self.__spriteBottom

	def returnSpriteHeight(self):
		return self.__spriteHeight

	def setScale(self, scale):
		self.__scale = scale
		self.__scaledWidth = self.__width * self.__scale
		self.__scaledHeight = self.__height * self.__scale
		self.__scaledPicture = transform.scale(self.__Picture, (self.__scaledWidth, self.__scaledHeight))

	def returnScale(self):
		return self.__scale

	def returnScaledWidth(self):
		return self.__scaledWidth

	def returnScaledHeight(self):
		return self.__scaledHeight

	def returnScaledPicture(self):
		return self.__scaledPicture

	def setAdjustX(self, adjustX):
		self.__adjustX = adjustX

	def returnAdjustX(self):
		return self.__adjustX

	def setAdjustY(self, adjustY):
		self.__adjustY = adjustY

	def returnAdjustY(self):
		return self.__adjustY

	def __str__(self):
		return  "\nName: " + str(self.__name)   + \
				"\nScale: " + str(self.__scale) + \
				"\nLeft Coord: " + str(self.__spriteLeft) + \
				"\nRight Coord: " + str(self.__spriteRight) + \
				"\nTop Coord: " + str(self.__spriteTop) + \
				"\nBottom Coord: " + str(self.__spriteBottom) + \
				"\nHorizontal Adjustment: " + str(self.__adjustX) + \
				"\nVertical Adjustment: " + str(self.__adjustY)