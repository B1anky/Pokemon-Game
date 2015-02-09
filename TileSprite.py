#This will handle all tiles that will be animated and added to the sreen

class TileSprite:
	def __init__(self, idleTile = None, movingTile = [], tileCoords = (0, 0), drawCoords = (0,0), \
				defaultTile = None, animTimer = 5, currentTile = None,\
				isWalkableOn = False, tileType = "", pokemonObjects = [], items = [], \
				encounterRate = 0):

		self.__idleTile = idleTile
		self.__movingTile = movingTile
		self.__tileCoords = tileCoords
		self.__drawCoords = drawCoords
		self.__defaultTile = defaultTile
		self.__animTimer = animTimer
		self.__currentTile = currentTile
		self.__isWalkableOn = isWalkableOn
		self.__tileType = tileType
		self.__pokemonObjects = pokemonObjects
		self.__items = items
		self.__encounterRate = encounterRate

	def setIdleTile(self, idleTile):
		self.__idleTile = idleTile

	def returnIdleTile(self):
		return self.__idleTile

	def setMovingTile(self, movingTile):
		self.__movingTile = movingTile

	#Like water or grass rustling
	def returnMovingTile(self):
		return self.__movingTile

	def setTileCoords(self, tileCoords):
		self.__tileCoords = tileCoords

	def returnTileCoords(self):
		return self.__tileCoords

	def setDrawCoords(self, drawCoords):
		self.__drawCoords = drawCoords

	def returnDrawCoords(self):
		return self.__drawCoords

	def setDefaultTile(self, defaultTile):
		self.__defaultTile = defaultTile

	def returnDefaultTile(self):
		return self.__defaultTile

	def setAnimTimer(self, TileTimer):
		self.__TileTimer = TileTimer

	def returnAnimTimer(self):
		return self.__TileTimer

	def setCurrentTile(self, currentTile):
		self.__currentTile = currentTile

	def returnCurrentTile(self):
		return self.__currentTile

	def setIsWalkableOn(self, isWalkableOn):
		self.__isWalkableOn = isWalkableOn

	def returnIsWalkableOn(self):
		return self.__isWalkableOn

	def setTileType(self, tileType):
		self.__tileType = tileType

	def returnTileType(self):
		return self.__tileType

	def setPokemonObjects(self, pokemonObjects):
		self.__pokemonObjects = pokemonObjects

	def returnPokemonObjects(self):
		return self.__pokemonObjects

	def setItems(self, items):
		self.__items = items

	def returnItems(self):
		return self.__items

	def setEncounterRate(self, encounterRate):
		self.__encounterRate = encounterRate

	def returnEncounterRate(self):
		return self.__encounterRate

	def animation(self):
		if len(self.returnMovingTile()) == 0:
			self.setCurrentTile(self.returnDefaultTile())

	def draw(self, screen, cam):
		imgToDraw = self.returnCurrentTile().returnScaledPicture()
		fx = self.returnTileCoords()[0] * 5*16
		fy = self.returnTileCoords()[1] * 5*16

		from pygame import Rect
		screen.blit(imgToDraw, cam.apply(Rect(fx, fy, 5*16, 5*16) ) )
	
	def rect(self):
		fx = self.returnTileCoords()[0] * 5*16
		fy = self.returnTileCoords()[1] * 5*16
		return Rect(fx, fy, 5*16, 5*16) 
		
	def updateAll(self, screen, cam):
		self.animation()
		self.draw(screen, cam)

	def __str__(self):
		return  "Tile type: " + str(self.__tileType) + \
				"\nTile Coordinates: "  + str(self.__tileCoords) + \
				"\nPixel Coordinates: " + str(self.__drawCoords) + \
				"\nCurrent tile: " + str(self.__currentTile) + \
				"\nItems: " + str(self.__items) + \
				"\nEncounter rate: " + str(self.__encounterRate) + \
				"\nIs walkable on?: " + str(self.__isWalkableOn) + \
				"\nPokemon objects: " + str(self.__pokemonObjects)
