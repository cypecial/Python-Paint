# pygameRev1.py
from pygame import *

init()
size = width, height = 800, 600
green = 0, 255, 0
red = 255, 0, 0
screen = display.set_mode(size)
cursorPic = image.load("ship1.png")
cw = cursorPic.get_width()
ch = cursorPic.get_height()

running = True
mx,my = 0,0
myClock = time.Clock()
mouse.set_visible(False)
screenBuff = screen.copy()
while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            sx,sy = evnt.pos
        if evnt.type == MOUSEBUTTONUP:
            screen.blit(screenBuff, (0,0))
            draw.line(screen, green, (sx,sy), (mx,my))
            screenBuff = screen.copy()

    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    
    screen.blit(screenBuff, (0,0))
    if mb[0]==1:
        draw.line(screen, green, (sx,sy), (mx,my))
    if mouse.get_pressed()[2]==1:
        screen.fill((0,0,0))

    screen.blit(cursorPic,(mx-cw/2,my-ch/2))   
    
    display.flip()
    myClock.tick(60)                        
    
quit()
