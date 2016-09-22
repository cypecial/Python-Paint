#Python paint program made by Yiping Che
from pygame import *
from random import *
from math import *
screen = display.set_mode((1024,768))
drawtool="pencil" #default drawing tool
start=0,0
size=2
#colours
blue = 0,0,255
red = 255,0,0
white = 255,255,255
black = 0,0,0
clr = black      #default drawing colour
#music
init()
##mixer.music.load("op11.mp3")
##mixer.music.play(-1)
#----load images
bkgrd = image.load("luffy zoro.png")
screen.blit(bkgrd,(0,0))
bkgrd1 = image.load("bkgrd1.png")
bkgrd2 = image.load("bkgrd2.png")
bkgrd3 = image.load("bkgrd3.png")
bkgrd4 = image.load("bkgrd4.png")
bkgrd5 = image.load("bkgrd5.png")
bkgrd6 = image.load("bkgrd6.png")
#-----------------------------------------
wheel = image.load("color.png")
screen.blit(wheel,(750,485))
#-----------------------------------------
pencil = image.load("pencil.png")
screen.blit(pencil,(15,155))
#-----------------------------------------
eraser = image.load("eraser.png")
screen.blit(eraser,(70,155))
#-----------------------------------------
brush = image.load("brush.png")
screen.blit(brush,(15,205))
#-----------------------------------------
line = image.load("line.jpg")
screen.blit(line,(70,205))
#-----------------------------------------
rect = image.load("rect.png")
screen.blit(rect,(70,255))
#-----------------------------------------
circle = image.load("circle.png")
screen.blit(circle,(15,255))
#-----------------------------------------
eyedropper = image.load("eyedropper.png")
screen.blit(eyedropper,(15,305))
#-----------------------------------------
airbrush = image.load("airbrush.png")
screen.blit(airbrush,(70,305))
#-----------------------------------------
pause = image.load("pause.png")
screen.blit(pause,(70,355))
#-----------------------------------------
play = image.load("play.png")
screen.blit(play,(15,355))
#-----------------------------------------
undo = image.load("undo.png")
screen.blit(undo,(610,20))
#-----------------------------------------
redo = image.load("redo.png")
screen.blit(redo,(685,20))
#-----------------------------------------
save = image.load("save.png")
screen.blit(save,(15,105))
#-----------------------------------------
load = image.load("open.png")
screen.blit(load,(70,105))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
luffyicon = image.load("luffy icon.png")
screen.blit(luffyicon,(125,660))
#-----------------------------------------
zoroicon = image.load("zoro icon.png")
screen.blit(zoroicon,(195,660))
#-----------------------------------------
namiicon = image.load("nami icon.png")
screen.blit(namiicon,(265,660))
#-----------------------------------------
ussopicon = image.load("ussop icon.png")
screen.blit(ussopicon,(335,660))
#-----------------------------------------
sanjiicon = image.load("sanji icon.png")
screen.blit(sanjiicon,(405,660))
#-----------------------------------------
robinicon = image.load("robin icon.png")
screen.blit(robinicon,(475,660))
#-----------------------------------------
choppericon = image.load("chopper icon.png")
screen.blit(choppericon,(545,660))
#-----------------------------------------
frankyicon = image.load("franky icon.png")
screen.blit(frankyicon,(615,660))
#-----------------------------------------
brookicon = image.load("brook icon.png")
screen.blit(brookicon,(685,660))
#-----------------------------------------
""" to add icons: icon = image.load("icon.png")
    to blit icon: screen.blit(icon,(x,y))
"""
oplogo = image.load("op logo.png")
logo = image.load("logo.png")
textPic = image.load("textPic.png") #text picture when saving/loading

pencilRect = Rect(15,155,40,40)
eraserRect = Rect(70,155,40,40)
brushRect = Rect(15,205,40,40)
lineRect = Rect(70,205,40,40)
circleRect = Rect(15,255,40,40)
rectRect = Rect(70,255,40,40)
eyedropRect = Rect(15,305,40,40)
playRect = Rect(15,355,40,40)
airbrushRect = Rect(70,305,40,40)
pauseRect = Rect(70,355,40,40)
wheelRect = Rect(750,480,285,276)
canvasRect = Rect(125,105,620,550)
randclrRect = Rect(762,492,35,35)
titleRect = Rect(0,0,281,98)
undoRect = Rect(610,20,60,60)
redoRect = Rect(685,20,60,60)
saveRect = Rect(15,105,40,40)
loadRect = Rect(70,105,40,40)
logoRect = Rect(857,0,167,107)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
luffyRect = Rect(125,660,60,60)
zoroRect = Rect(195,660,60,60)
namiRect = Rect(265,660,60,60)
ussopRect = Rect(335,660,60,60)
sanjiRect = Rect(405,660,60,60)
robinRect = Rect(475,660,60,60)
chopperRect = Rect(545,660,60,60)
frankyRect = Rect(615,660,60,60)
brookRect = Rect(685,660,60,60)
#-----------------------------------------
""" to add rect: rect = Rect(x,y,w,h,)"""

draw.rect(screen,white,canvasRect,0)
draw.rect(screen,black,(124,104,622,552),1)
running =True

draw.rect(screen,red,pencilRect,2)

undo = [screen.copy()]
redo = []
drawn = False
def getName(): #function to get file name when saving/loading
    ans = ""                    
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(150,140,200,25) # make changes here.
    screen.blit(textPic,(125,105))
    screen.set_clip(textArea)
    
    
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = arialFont.render(ans, True, (0,0,0))   
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,black,textArea,2)              
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        
        display.flip()
    screen.set_clip(canvasRect)        
    screen.blit(back,(0,0))
    return ans

while running:
    mx,my = mouse.get_pos()
    keys=key.get_pressed()

    #----blitting backgrounds in canvas
    if keys[K_F1]: 
        screen.blit(bkgrd1,canvasRect)
        drawn = True
    if keys[K_F2]:
        screen.blit(bkgrd2,canvasRect)
        drawn = True
    if keys[K_F3]:
        screen.blit(bkgrd3,canvasRect)
        drawn = True
    if keys[K_F4]:
        screen.blit(bkgrd4,canvasRect)
        drawn = True
    if keys[K_F5]:
        screen.blit(bkgrd5,canvasRect)
        drawn = True
    if keys[K_F6]:
        screen.blit(bkgrd6,canvasRect)
        drawn = True
        
    for e in event.get():
        if e.type == QUIT:
            running = False
        #----drawing red over selected tool/ defining tool
        if pencilRect.collidepoint(mx,my): 
            draw.rect(screen,red,pencilRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="pencil"
        if eraserRect.collidepoint(mx,my):
            draw.rect(screen,red,eraserRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="eraser"
        if brushRect.collidepoint(mx,my):
            draw.rect(screen,red,brushRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="brush"
        if lineRect.collidepoint(mx,my):
            draw.rect(screen,red,lineRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="line"
        if rectRect.collidepoint(mx,my):      
            draw.rect(screen,red,rectRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="rect"
        if eyedropRect.collidepoint(mx,my):
            draw.rect(screen,red,eyedropRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="eyedrop"
        if circleRect.collidepoint(mx,my):
            draw.rect(screen,red,circleRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="circle"
        if airbrushRect.collidepoint(mx,my):
            draw.rect(screen,red,airbrushRect,2)
            if e.type ==MOUSEBUTTONDOWN and e.button ==1:
                drawtool="airbrush"
        if undoRect.collidepoint(mx,my):
            draw.rect(screen,red,undoRect,2)
            if e.type ==MOUSEBUTTONDOWN and e.button ==1:
                drawtool="undo"
        if redoRect.collidepoint(mx,my):
            draw.rect(screen,red,redoRect,2)
            if e.type ==MOUSEBUTTONDOWN and e.button ==1:
                drawtool="redo"
        if saveRect.collidepoint(mx,my):
            draw.rect(screen,red,saveRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button ==1:
                drawtool="save"
        if loadRect.collidepoint(mx,my):
            draw.rect(screen,red,loadRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button ==1:
                drawtool="load"
        #----music play / pause
        if playRect.collidepoint(mx,my):
            draw.rect(screen,red,playRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="play"
        if pauseRect.collidepoint(mx,my):
            draw.rect(screen,red,pauseRect,2)
            if e.type ==MOUSEBUTTONDOWN and e.button ==1:
                drawtool="pause"
        if titleRect.collidepoint(mx,my):
            if e.type ==MOUSEBUTTONDOWN and e.button ==1: #left click on title to clear screen
                screen.set_clip(canvasRect)
                screen.fill(white)
                screen.set_clip(None)
            if e.type == MOUSEBUTTONDOWN and e.button ==3: #right click on title for Onepiece logo
                drawtool="oplogo"
        if wheelRect.collidepoint(mx,my):
            if (750+158-mx)**2+(485+156-my)**2 < 138**2 and e.type ==MOUSEBUTTONDOWN and e.button ==1:
                clr = screen.get_at((mx,my))
        if randclrRect.collidepoint(mx,my) and e.type ==MOUSEBUTTONDOWN and e.button ==1:
            clr=(randint(0,255),randint(0,255),randint(0,255))  #gives random colour
        draw.rect(screen,clr,logoRect)
        if clr==black:
            draw.rect(screen,white,logoRect)
        screen.blit(logo,(857,0))
        #---- stamps
        if zoroRect.collidepoint(mx,my):
            draw.rect(screen,red,zoroRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="zoro"
        if luffyRect.collidepoint(mx,my):
            draw.rect(screen,red,luffyRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="luffy"
        if namiRect.collidepoint(mx,my):
            draw.rect(screen,red,namiRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="nami"
        if namiRect.collidepoint(mx,my):
            draw.rect(screen,red,namiRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="nami"
        if ussopRect.collidepoint(mx,my):
            draw.rect(screen,red,ussopRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="ussop"
        if sanjiRect.collidepoint(mx,my):
            draw.rect(screen,red,sanjiRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="sanji"
        if robinRect.collidepoint(mx,my):
            draw.rect(screen,red,robinRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="robin"
        if chopperRect.collidepoint(mx,my):
            draw.rect(screen,red,chopperRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="chopper"
        if frankyRect.collidepoint(mx,my):
            draw.rect(screen,red,frankyRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="franky"
        if brookRect.collidepoint(mx,my):
            draw.rect(screen,red, brookRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="brook"
        #----music play / pause
        if playRect.collidepoint(mx,my):
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                mixer.music.unpause()
        if pauseRect.collidepoint(mx,my):
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                mixer.music.pause()

        """ when adding tools:
            if tool.collidepoint(mx,my):
                draw.rect(screen,red,toolRect,2)
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                drawtool="tool"
        """
        #----start undo redo
        if redoRect.collidepoint(mx,my):
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and redo:
                screen.set_clip(canvasRect)
                undo.append(redo.pop(-1))
                screen.blit(undo[-1],(0,0))
                screen.set_clip(None)
        if undoRect.collidepoint(mx,my):
            if e.type == MOUSEBUTTONDOWN and e.button == 1 and len(undo) > 1:
                redo.append(undo.pop(-1))
                screen.set_clip(canvasRect)
                screen.blit(undo[-1],(0,0))
                screen.set_clip(None)

        #----continue the evt loop
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1 or e.button == 3:
                back=screen.copy()
                start = e.pos
            if e.button == 4 and size < 70:
               size += 1
            if e.button == 5 and size > 1:
               size -= 1
            if drawtool == "circle":
                if e.button == 1:
                    back=screen.copy()
                    start = e.pos
                elif e.button == 4 and size < min(abs(mx-start[0]),abs(my-start[1]))/2:
                    size +=1
                elif e.button == 5 and size > 1:
                    size -=1
            #----save and load
            if drawtool == "save":
                txt = getName()
                if "." in txt:
                    image.save(screen.subsurface(canvasRect),txt)
                else:   #if user forgets to enter extention, set to .png automatically
                    image.save(screen.subsurface(canvasRect),txt+".png")
                drawtool = "pencil"

            if drawtool == "load": 
                txt = getName()
                screen.set_clip(canvasRect)
                if "." in txt:
                    loadimage = image.load(txt)
                else:   #if user forgets to enter extention, set to .png automatically
                    loadimage = image.load(txt+".png")
                screen.blit(loadimage,canvasRect)
                drawtool = "pencil"

        if e.type == MOUSEBUTTONUP:
            if e.button == 1 and drawn: 
                redo = []
                undo.append(screen.copy())
                drawn = False
        display.flip()
    
    mb = mouse.get_pressed()
    
    #----draw blue over unselected tools
    if drawtool != "pencil":
        draw.rect(screen,blue,pencilRect,2)
    if drawtool != "eraser":
        draw.rect(screen,blue,eraserRect,2)
    if drawtool != "brush":
        draw.rect(screen,blue,brushRect,2) 
    if drawtool != "line":
        draw.rect(screen,blue,lineRect,2)  
    if drawtool != "play":
        draw.rect(screen,blue,playRect,2) 
    if drawtool != "rect":
        draw.rect(screen,blue,rectRect,2)
    if drawtool != "eyedrop":
        draw.rect(screen,blue,eyedropRect,2)
    if drawtool != "circle":
        draw.rect(screen,blue,circleRect,2)
    if drawtool != "airbrush":
        draw.rect(screen,blue,airbrushRect,2)
    if drawtool != "pause":
        draw.rect(screen,blue,pauseRect,2)
    if drawtool != "undo":
        draw.rect(screen,blue,undoRect,2)
    if drawtool != "redo":
        draw.rect(screen,blue,redoRect,2)
    if drawtool != "save":
        draw.rect(screen,blue,saveRect,2)
    if drawtool != "load":
        draw.rect(screen,blue,loadRect,2)
    #~~~~stamps Rect
    if drawtool != "luffy":
        draw.rect(screen,blue,luffyRect,2)    
    if drawtool != "zoro":
        draw.rect(screen,blue,zoroRect,2)      
    if drawtool != "nami":
        draw.rect(screen,blue,namiRect,2)     
    if drawtool != "ussop":
        draw.rect(screen,blue,ussopRect,2)    
    if drawtool != "sanji":
        draw.rect(screen,blue,sanjiRect,2)    
    if drawtool != "robin":
        draw.rect(screen,blue,robinRect,2)    
    if drawtool != "chopper":
        draw.rect(screen,blue,chopperRect,2)   
    if drawtool != "franky":
        draw.rect(screen,blue,frankyRect,2)    
    if drawtool != "brook":
        draw.rect(screen,blue,brookRect,2)

    """ when adding tools:
    if drawtool != "tool":
        draw.rect(screen,blue,toolRect,2)
    """
#----------------------------------------------------
    
    if canvasRect.collidepoint(mx,my): #while mouse inside canvas
        nmx,nmy = mouse.get_pos()
        delx = nmx-mx
        dely = nmy-my
        dist = hypot(delx,dely)
        if dist==0:
            dist=1
        screen.set_clip(canvasRect)
        if size<=2:
            size==2    #size won't go negative
        if size>=100:  #and does not exceed 100
            size==100
        #----pencil
        if mb[0]==1 and drawtool=="pencil":
            draw.line(screen,clr,(mx,my),(nmx,nmy),1)
            drawn = True            
        #----brush
        if mb[0]==1 and drawtool=="brush":
            for i in range(int(dist)+1):
                draw.circle(screen,clr,(mx+int(delx/dist*i),my+int(dely/dist*i)),size)
            drawn = True
        #----line
        if mb[0]==1 and drawtool=="line":
            screen.blit(back,(0,0))
            draw.line(screen,clr,start,(nmx,nmy), size)
            drawn = True
        #----circle
        if mb[0]==1 and drawtool=="circle":
            if size < min(abs(mx-start[0]),abs(my-start[1]))/2:
                screen.blit(back,(0,0))
                draw.ellipse(screen,clr,(min(mx,start[0]),min(my,start[1]),abs(mx-start[0]),abs(my-start[1])),size)
            drawn = True
        if mb[2]==1 and drawtool=="circle": #right click for filled ellipse
            if size < min(abs(mx-start[0]),abs(my-start[1]))/2:
                screen.blit(back,(0,0))
                draw.ellipse(screen,clr,(min(mx,start[0]),min(my,start[1]),abs(mx-start[0]),abs(my-start[1])))
            drawn = True
        #----eraser
        if mb[0]==1 and drawtool=="eraser":
            if size<5:
                size=5
            for i in range(int(dist)+1):
                draw.rect(screen,white,(mx+int(delx/dist*i)-size,my+int(dely/dist*i)-size,size*2,size*2),0)
            drawn = True
        if mb[2]==1 and drawtool =="eraser": #right click for coloured eraser
            if size<5:
                size=5
            for i in range(int(dist)+1):
                draw.rect(screen,clr,(mx+int(delx/dist*i)-size,my+int(dely/dist*i)-size,size*2,size*2),0)
            drawn = True              
            
        #----rect
        if drawtool=="rect":
            if mb[0]==1:
                screen.blit(back,(0,0))
                draw.rect(screen,clr,(start[0],start[1],mx-start[0],my-start[1]),size)
                drawn = True
            if mb[2]==1:    #right click for filled rect
                screen.blit(back,(0,0))
                draw.rect(screen,clr,(start[0],start[1],mx-start[0],my-start[1]))
                drawn = True
        #----eyedrop
        if mb[0]==1 and drawtool=="eyedrop":
            clr = screen.get_at((mx,my))                        
        #----airbrush
        if mb[0]==1 and drawtool=="airbrush":
            if size<10:
                size=10
            for i in range(20):
                x = randint(-size,size)
                y = randint(-size,size)
                if (x)**2+(y)**2 < size**2:
                    draw.line(screen,clr,(x+mx,y+my),(x+mx,y+my),1)
            drawn = True
            display.flip()

        """when adding tools:
           if mb[0]==1 and drawtool=="tool":
               #set tool function
               #if tool makes changes to canvas, add:
               drawn = True
        """

        #------stamps
        if mb[0]==1:
            if drawtool=="zoro":
                screen.blit(back,(0,0))
                screen.blit(zoroicon, (mx-30,my-30))
                drawn = True
            if drawtool=="luffy":
                screen.blit(back,(0,0))
                screen.blit(luffyicon,(mx-30,my-30))
                drawn = True
            if drawtool=="nami":
                screen.blit(back,(0,0))
                screen.blit(namiicon,(mx-30,my-30))
                drawn = True
            if drawtool=="ussop":
                screen.blit(back,(0,0))
                screen.blit(ussopicon,(mx-30,my-30))
                drawn = True
            if drawtool=="sanji":
                screen.blit(back,(0,0))
                screen.blit(sanjiicon,(mx-30,my-30))
                drawn = True
            if drawtool=="robin":
                screen.blit(back,(0,0))
                screen.blit(robinicon,(mx-30,my-30))
                drawn = True
            if drawtool=="chopper":
                screen.blit(back,(0,0))
                screen.blit(choppericon,(mx-30,my-30))
                drawn = True
            if drawtool=="franky":
                screen.blit(back,(0,0))
                screen.blit(frankyicon,(mx-30,my-30))
                drawn = True
            if drawtool=="brook":
                screen.blit(back,(0,0))
                screen.blit(brookicon,(mx-30,my-30))
                drawn = True
            if drawtool=="oplogo":
                screen.blit(back,(0,0))
                screen.blit(oplogo,(mx-126,my-45))
                drawn = True
        if mb[2]==1:
            if drawtool=="zoro":
                screen.blit(zoroicon, (mx-30,my-30))
                drawn = True
            if drawtool=="luffy":
                screen.blit(luffyicon,(mx-30,my-30))
                drawn = True
            if drawtool=="nami":
                screen.blit(namiicon,(mx-30,my-30))
                drawn = True
            if drawtool=="ussop":
                screen.blit(ussopicon,(mx-30,my-30))
                drawn = True
            if drawtool=="sanji":
                screen.blit(sanjiicon,(mx-30,my-30))
                drawn = True
            if drawtool=="robin":
                screen.blit(robinicon,(mx-30,my-30))
                drawn = True
            if drawtool=="chopper":
                screen.blit(choppericon,(mx-30,my-30))
                drawn = True
            if drawtool=="franky":
                screen.blit(frankyicon,(mx-30,my-30))
                drawn = True
            if drawtool=="brook":
                screen.blit(brookicon,(mx-30,my-30))
                drawn = True
        screen.set_clip(None)


quit()
