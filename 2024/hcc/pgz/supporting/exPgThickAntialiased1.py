#https://stackoverflow.com/questions/30578068/pygame-draw-anti-aliased-thick-line

def drawLineWidth(surface, color, p1, p2, width):
    # delta vector
    d = (p2[0] - p1[0], p2[1] - p1[1])

    # distance between the points
    dis = math.hypot(*d)

    # normalized vector
    n = (d[0]/dis, d[1]/dis)

    # perpendicular vector
    p = (-n[1], n[0])

    # scaled perpendicular vector (vector from p1 & p2 to the polygon's points)
    sp = (p[0]*width/2, p[1]*width/2)

    # points
    p1_1 = (p1[0] - sp[0], p1[1] - sp[1])
    p1_2 = (p1[0] + sp[0], p1[1] + sp[1])
    p2_1 = (p2[0] - sp[0], p2[1] - sp[1])
    p2_2 = (p2[0] + sp[0], p2[1] + sp[1])

    # draw the polygon
    pygame.gfxdraw.aapolygon(surface, (p1_1, p1_2, p2_2, p2_1), color)
    pygame.gfxdraw.filled_polygon(surface, (p1_1, p1_2, p2_2, p2_1), color)

### end ###
