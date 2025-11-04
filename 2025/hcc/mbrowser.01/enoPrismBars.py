import pygame

# Create a transparent surface
poly1 = pygame.Surface((400, 400), pygame.SRCALPHA)
poly2 = pygame.Surface((400, 400), pygame.SRCALPHA)

# Define polygon points
points1 = [(100, 100), (300, 100), (350, 300), (150, 350)]
points2 = [(200,   0), (400, 400), (  0, 400)]

# Define a color with alpha (RGBA)
colRed = (255, 0, 0, 128)  # Semi-transparent red

# Draw the polygon on the transparent surface
pygame.draw.polygon(poly1, colRed, points1)
pygame.draw.polygon(poly2, colRed, points2)

def draw():
  screen.clear()
  screen.blit(poly1, (0, 0))
  screen.blit(poly2, (0, 0))

### end ###
