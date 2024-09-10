# Enodia window ~manager
#  Slight generalization and abstraction from earlier transparent + migratory window code 
#  evolved from below links, ++
# Brygg Ullmer, Clemson University
# Begun 2024-08-31

#https://stackoverflow.com/questions/550001/fully-transparent-windows-in-pygame
#https://stackoverflow.com/questions/1997710/pygame-error-display-surface-quit-why
#https://stackoverflow.com/questions/44520491/can-i-move-the-pygame-game-window-around-the-screen

import pygame
import os
import win32api
import win32con
import win32gui
from pygame._sdl2 import Window

###################### Enodia Window Manager (first steps) ###################### 

class enoWinMgr:

  name2window            = None
  moveWindowLastCoords   = None
  moveWindowIdLastCoords = None
  borderless             = True

  ############# constructor #############

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.name2window            = {}
    self.moveWindowLastCoords   = {} #unsure because of pygame_sdl2 deepcopy issue about aspects here
    self.moveWindowIdLastCoords = {}

  ##################### new window ##################### 
   
  def newWindow(self, name, w,h):
    pWindow           = Window(name, size=(w,h))
    if self.borderless: pWindow.borderless = True
    self.name2window[name] = pWindow
    return pWindow
  
  ##################### get window ##################### 
  
  def getWindow(self, name=None):
    if name=='firstWin' or name is None: return Window.from_display_module()
    if name in self.name2window:         result = self.name2window[name]; return result
  
  ##################### move window ##################### 
  
  def moveWindow(self, pWindow, x, y):
    if pWindow in self.moveWindowLastCoords:
      lastX, lastY = self.moveWindowLastCoords[pWindow]
      if x == lastX and y == lastY: return #no movement
  
    else: self.moveWindowLastCoords[pWindow] = (x,y)
  
    if pWindow is None: pWindow=getWindow()
    pWindow.position = (x,y) #titlebar slightly off-screen
  
  ##################### move window by id ##################### 
  
  def moveWindowById(self, windowId, x, y, pWindows):
    if windowId in self.moveWindowIdLastCoords:
      lastX, lastY = self.moveWindowIdLastCoords[windowId]
      if x == lastX and y == lastY: return #no movement
  
    else: self.moveWindowIdLastCoords[windowId] = (x,y)
  
    if windowId not in pWindows:
      print("moveWindowById error: id index not found:", windowId); return
  
    pWindow = pWindows[windowId]
    pWindow.position = (x,y)
  
  ##################### transparent window setup ##################### 
  
  def transpWinSetup(self, screen, keyColor, winWidth, winHeight, pWindow=None):
    imgIcon = pygame.image.load("images/animist01e.png")
    pygame.display.set_icon(imgIcon)
    pygame.display.set_caption("animist alpha")
  
    if pWindow is None: pWindow = self.getWindow()
    self.moveWindow(pWindow, 0, 0)
  
    # Create layered window
    #print("transpWinSetup hwnd:" + str(pygame.display.get_wm_info()))
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    # Set window transparency color
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*keyColor), 0, win32con.LWA_COLORKEY)

### end ###
