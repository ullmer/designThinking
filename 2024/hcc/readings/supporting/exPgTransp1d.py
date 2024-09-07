#https://stackoverflow.com/questions/18701453/how-to-draw-a-transparent-line-in-pygame

import pygame  

WIDTH, HEIGHT = 500, 500

# Create a temporary surface that supports alpha values
s1 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
s2 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

def draw():
  screen.clear()
  color  = (255, 255, 255, 128) # or '#ffffffdd'

  # Draw the line on the temporary surface
  #pygame.draw.line(s1, color, start_pos, end_pos, width)
  pygame.draw.line(s1, color, (0, 250), (500, 250), 50)
  pygame.draw.line(s2, color, (250, 0), (250, 500), 50)

  # Draw the surface on the screen
  screen.blit(s1, (0,0))
  screen.blit(s2, (0,0))

### end ###
