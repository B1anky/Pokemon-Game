class Level():
	def __init__(self, playerObjects):
		self.__playerObjects = playerObjects
		self.__worldShiftX = 0

		self.__leftViewBox = windowWidth