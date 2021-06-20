import turtle
import math

# Zoomables Koordinatensystem
# arrow-up für mehr Zoom
# arrow-down für weniger

ps = {}
lins = {}

stuff = [5, 1000, 1000]
ct = turtle.Turtle()
dt = turtle.Turtle()
data = [80, 40, 80, 1]

ct.speed(0)
turtle.delay(0)

turtle.screensize(1000, 1000)


def redrawplus():
    global data
    dt.clear()
    ct.clear()
    data[0] *= 1.1
    
    drawGrid()

def redrawminus():
    global data
    dt.clear()
    ct.clear()
    data[0] *= 0.9
    
    drawGrid()
    


def drawGrid():
    global data

    ct.forward(2)
    ct.write("0", align="left", font=("Arial", 8, "normal"))
    ct.goto(0, 0)
    turtle.tracer(0)
    ct.color(0.75, 0.75, 0.75)
    stufl = stuff[0]
    for i in range(int((stuff[1])/data[0])):
        

        if data[0] < data[1]:
            data[2] = data[1]
            data[1] = data[0] / 2
            
            data[3] = data[3] * 2
        elif data[0] > data[2]:
            data[1] = data[2]
            data[2] = data[0] * 2
            
            data[3] = data[3] / 2

        if not i % data[3] == 0:
            
            continue
        ct.penup()
        ct.setx(0 + data[0]*i)
        ct.sety(stuff[1])
        ct.pendown()
        ct.sety(stufl)
        ct.color(0, 0, 0)
        ct.sety(0)
        ct.write(float(i), align="left")
        ct.sety(-stufl)
        ct.color(0.75, 0.75, 0.75)
        ct.sety(-stuff[1])

    for i in range(int((stuff[1])/data[0])):
        if (i) % 5 == 0:
            stufl = stufl+4
        else:
            stufl = stuff[0]
        
        if not i % data[3] == 0:
            continue
        ct.penup()
        ct.setx(0 - data[0]*i)
        ct.sety(stuff[1])
        ct.pendown()
        ct.sety(stufl)
        ct.color(0, 0, 0)
        ct.sety(0)
        ct.write(float(i), align="left")
        ct.sety(-stufl)
        ct.color(0.75, 0.75, 0.75)
        ct.sety(-stuff[1])
    turtle.pensize(1)
    for i in range(int((stuff[1])/data[0])):
        if (i) % 5 == 0:
            stufl = stufl+4
        else:
            stufl = stuff[0]
        
        if not i % data[3] == 0:
            continue
        ct.penup()
        ct.sety(0 + data[0]*i)
        ct.setx(stuff[1])
        ct.pendown()
        ct.setx(stufl)
        ct.color(0, 0, 0)
        ct.setx(0)
        ct.write(float(i), align="left")
        ct.setx(-stufl)
        ct.color(0.75, 0.75, 0.75)
        ct.setx(-stuff[1])
    for i in range(int((stuff[1])/data[0])):
        if (i) % 5 == 0:
            stufl = stufl+4
        else:
            stufl = stuff[0]
        
        if not i % data[3] == 0:
            continue
        ct.penup()
        ct.sety(0 - data[0]*i)
        ct.setx(stuff[1])
        ct.pendown()
        ct.setx(stufl)
        ct.color(0, 0, 0)
        ct.setx(0)
        ct.write(float(i), align="left")
        ct.setx(-stufl)
        ct.color(0.75, 0.75, 0.75)
        ct.setx(-stuff[1])

    ct.color(0, 0, 0)


    ct.setx(0)
    ct.sety(-1000)
    ct.sety(1000)
    ct.sety(0)
    ct.setx(-1000)
    ct.setx(1000)
    turtle.tracer(1)
    drawOutPoints()
    drawOutLines()


def drawOutLines():
    for i in range(len(lins)):
        drawLine((lins[i][0], lins[i][1]), False, True)
        
        

def test():
    pass

def drawPoint(x, y, index):
    dt.penup()
    dt.setx(data[0]*x)
    dt.sety(data[0]*y)
    dt.pendown()
    dt.dot((10), "red")
    dt.write("P" + str(index))

def drawOutPoints():
    for i in range(len(ps)):
        
        drawPoint(float(ps["P" + str(i+1)][0]), float(ps["P" + str(i+1)][1]), i+1)
        


def AddPoint(x:float, y:float, onscreen = True, re = False):
    if onscreen == True:
        x = x / data[0]
        y = y / data[0]

    ps["P" + str(len(ps)+1)] = (x, y)
    if not re: print("Added Point" , "P" + str(len(ps)) ,"at x:" + str(x) + ", y: " + str(y))
    drawPoint(x, y, len(ps))
    return "P" + str(int(len(ps)))


def drawLine(points: iter = None, goback: bool = False, re = False):
    pos = dt.position()
    if points == None:
        points = [None, None]
        points[0] = "P" + str(int(len(ps)-1))
        points[1] = "P" + str(int(len(ps)))
    else:
        if points[0] == None:
            points[0] = "P" + str(int(len(ps)-1))
        elif points[1] == None:
            points[1] = "P" + str(int(len(ps)))
    
    
    
    dt.speed(0)
    dt.penup()
    dt.setx(float(ps[points[0]][0])*data[0])
    dt.sety(float(ps[points[0]][1])*data[0])
    
    dt.pendown()
    dt.goto(float(ps[points[1]][0])*data[0], float(ps[points[1]][1])*data[0])
    if goback: dt.goto(pos)
    
    
    dupl = False
    if not re:
        if len(lins) == 0:
            lins[0] = [points[0], points[1]]
        else:
            for i in range(len(lins)):
                
                if lins[i][0] == points[0] and lins[i][1] == points[1]:
                    dupl = True
                    break
            if not dupl:
                lins[len(lins)] = [points[0], points[1]]
    
        print("Line between", points[0], "and", points[1], "drawn")
                
                
                
                    
        
        
                
    
    




def triangulate(points: iter = None):
    if points == None:
        points = ["P" + str(int(len(ps)-2)), "P" + str(int(len(ps)-1)), "P" + str(int(len(ps)))]
        
    else:
        if points[0] == None:
            points[0] = "P" + str(int(len(ps)-2))
        elif points[1] == None:
            points[1] = "P" + str(int(len(ps)-1))
        elif points[2] == None:
            points[2] = "P" + str(int(len(ps)))

    dt.pendown()
    
    
    drawLine((points[2], points[0]))
    drawLine((points[0], points[1]))
    drawLine((points[1], points[2]))

def clearDt():
    
    print("Cleared Points")
    ps.clear()
    dt.clear()





drawGrid()
turtle.onkey(redrawplus, "Up")
turtle.onkey(redrawminus, "Down")
turtle.onkey(drawLine, "Left")
turtle.onkey(triangulate, "Right")


turtle.getscreen().onclick(AddPoint)
turtle.listen()


