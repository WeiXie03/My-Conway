from fltk import *
import time

sqside = 9
bgrid = []
oldgrid = []
gridside = 100
state = 0
delay = 0.4

def trigged(widg):
    if widg.color() != FL_BLACK:
        if Fl.event_button() == FL_LEFT_MOUSE:
            widg.color(FL_BLUE)
        else:
            widg.color(FL_WHITE)

def simu(widg):
    global state
    global delay
    delay = 0.4
    state = 1
    while state == 1:
        for x in range(1,len(bgrid)-1):
            for y in range(1,len(bgrid[x])-1):
                if bgrid[x][y].color() == FL_BLUE:
                    oldgrid[x][y] = 1
                else:
                    oldgrid[x][y] = 0

        for x in range(1,len(bgrid)-1):
            for y in range(1,len(bgrid[x])-1):
                pop = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i != 0 or j != 0:
                            pop += oldgrid[x+i][y+j]
                if pop < 2:
                    bgrid[x][y].color(FL_WHITE)
                elif pop == 3 and oldgrid[x][y] == 0:
                    bgrid[x][y].color(FL_BLUE)
                elif pop > 3:
                    bgrid[x][y].color(FL_WHITE)
                bgrid[x][y].redraw()
        time.sleep(delay)
        Fl.check()

win = Fl_Window(Fl_w()-40, Fl_h()-40, 'Wei\'s Game of Life')

def halt(widg):
    global state
    state = 0

def fast(widg):
    global delay
    delay *= 0.5

win.begin()
for row in range(gridside):
    bgrid.append([])
    oldgrid.append([])
    for column in range(gridside):
        bgrid[row].append(Fl_Button(sqside*column,sqside*row,sqside,sqside))
        bgrid[row][-1].color(FL_WHITE)
        bgrid[row][-1].box(FL_FLAT_BOX)
        bgrid[row][-1].callback(trigged)
        oldgrid[row].append(0)

offset = 100
stop = Fl_Button(Fl_w()-offset*sqside//2,Fl_h()-(offset*sqside)//4,60,40,'stop')
stop.color(FL_WHITE)
stop.callback(halt)
start = Fl_Button(Fl_w()-offset*sqside//2-20,offset*sqside//4,60,40,'start')
start.color(FL_WHITE)
start.callback(simu)
fastfor = Fl_Button(Fl_w()-offset*sqside//2-30,Fl_h()//2-20,60,40,'faster')
fastfor.callback(fast)

for x in [0, len(bgrid)-1]:
    for y in range(len(bgrid[x])):
        bgrid[x][y].color(FL_BLACK)
        bgrid[x][y].deactivate()

for x in range(len(bgrid)):
    for y in [0, len(bgrid[x])-1]:
        bgrid[x][y].color(FL_BLACK)
        bgrid[x][y].deactivate()

win.end()

win.show()
Fl.run()
