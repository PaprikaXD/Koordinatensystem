import koordinatensystem as root




while True:
    cmd = input("Input: \n")
    
    varsAP = ('ap', 'addpoint', 'addp', 'apoint', )
    if any(x in cmd.lower() for x in varsAP):

        coor = cmd.split(' ')
        
        root.AddPoint(float(coor[1]), float(coor[2]), False)


    varsDL = ('DL', 'DRAWLINE', 'DRAWL', 'DLINE', 'LINE', )
    if any(x in cmd.upper() for x in varsDL):

        coor = cmd.split(' ')
        
        root.drawLine((coor[1], coor[2]))


    varsTR = ('TRIANGULATE', 'CONNECT3', 'TR', 'TRIANGLE', )
    if any(x in cmd.upper() for x in varsTR):

        coor = cmd.split(' ')
        
        try:
            root.triangulate((coor[1], coor[2], coor[3], ))
        except:
            root.triangulate()

    varsEXIT = ('exit', 'close', 'yeet', 'altf4')
    if any(x in cmd.lower() for x in varsEXIT):
        root.turtle.bye()




    