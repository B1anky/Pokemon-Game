from pygame import Rect

class Camera(object):
	def __init__(self, camera_handler, width, height):
		self.state = Rect(0,0, width, height)
		self.cam_handle = camera_handler

	def apply(self, target):
		return target.move(self.state.topleft)

	def update(self, target):
		self.state = self.cam_handle(self.state, target.rect())