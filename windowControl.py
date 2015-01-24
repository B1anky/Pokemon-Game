import sys
import os
from pygame import *
from pygame.locals import *

if os.name == 'nt': #sys.platform == 'win32':

	from ctypes import windll

	#The following uses system information in order to get info
	#that allows python/pygame to receive window info from the system
	#for maximizing or minimizing. Did not write. Credit below.
	#http://archives.seul.org/pygame/users/Oct-2007/msg00127.html

	SW_MAXIMIZE =   3
	SW_RESTORE  =   9
	user32      = windll.user32
	ShowWindow  = user32.ShowWindow
	IsZoomed    = user32.IsZoomed
	video_flags = RESIZABLE

	def getSDLWindow():
		return display.get_wm_info()['window']

	def SDL_Maximize():
		return ShowWindow(getSDLWindow(), SW_MAXIMIZE)

	def SDL_Restore():
		return ShowWindow(getSDLWindow(), SW_RESTORE)

	def SDL_IsMaximized():
		return IsZoomed(getSDLWindow())
else:
	SW_MAXIMIZE =   3
	SW_RESTORE  =   9
	user32      = None
	ShowWindow  = None
	IsZoomed    = None
	video_flags = RESIZABLE

	def getSDLWindow():
		return None

	def SDL_Maximize():
		return None

	def SDL_Restore():
		return None

	def SDL_IsMaximized():
		return None