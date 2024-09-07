#https://www.reddit.com/r/pygame/comments/4io49d/drawing_a_transparenthalftransparent_square/
#https://gamedevacademy.org/pygame-opacity-tutorial-complete-guide/

import sys
import pygame as pg


RED_HIGHLIGHT = (240, 50, 50, 100)

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((500,500))
screen_rect = screen.get_rect()

see_through = pg.Surface((100,100)).convert_alpha()
see_through.fill(RED_HIGHLIGHT)
see_through_rect = see_through.get_rect(bottomleft=screen_rect.center)


while pg.event.poll().type != pg.QUIT:
    pg.draw.circle(screen, pg.Color("cyan"), screen_rect.center, 50)
    screen.blit(see_through, see_through_rect)
    pg.display.update()
    clock.tick(60)

pg.quit()
sys.exit()

### end ###
