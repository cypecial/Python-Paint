from pygame import *
screen=display.set_mode((800,600))
background=screen.copy()
running=True
size = 0
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                size = 0
                background=screen.copy()
                pos=evt.pos
            elif evt.button == 4 and size < min(abs(mx-pos[0]),abs(my-pos[1]))/2:
                size +=1
            elif evt.button == 5 and size > 1:
                size -=1
    mx,my=mouse.get_pos()       
    mb=mouse.get_pressed()
    keys = key.get_pressed()
    if mb[0]==1:
        if size < min(abs(mx-pos[0]),abs(my-pos[1]))/2:
            screen.blit(background,(0,0))
            draw.ellipse(screen,(0,255,0),(min(mx,pos[0]),min(my,pos[1]),abs(mx-pos[0]),abs(my-pos[1])),size)
    display.flip()
quit()
