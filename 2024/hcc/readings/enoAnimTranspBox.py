# Enodia animated transparent box
# By Brygg Ullmer, Clemson University
# Begun 2024-09-06

import pygame  

#WIDTH, HEIGHT = 500, 500

############################ enodia animated transparent box ############################

class enoAnimTranspBox:

  lineThickness = 5
  alpha         = 128  #on 255 scale
  topLeft       = None #tuple
  bottomRight   = None #tuple

  ############# constructor #############

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

  ############################ build box ############################

  def buildBox(self):

# Create a temporary surface that supports alpha values
s1 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
s2 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

  ############################ draw ############################

  def draw(self, screen):
  screen.clear()
  color  = (255, 255, 255, 128) # or '#ffffffdd'

#https://stackoverflow.com/questions/18701453/how-to-draw-a-transparent-line-in-pygame
  # Draw the line on the temporary surface
  #pygame.draw.line(s1, color, start_pos, end_pos, width)
  pygame.draw.line(s1, color, (0, 250), (500, 250), 50)
  pygame.draw.line(s2, color, (250, 0), (250, 500), 50)

  # Draw the surface on the screen
  screen.blit(s1, (0,0))
  screen.blit(s2, (0,0))

### end ###
