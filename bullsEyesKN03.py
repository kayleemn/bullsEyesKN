#bullsEyes by Kaylee

from graphics import*

def draw_cir(cX, cY, cRad, cColor, cWin):
    circle = Circle(Point(cX, cY), cRad)
    circle.setFill(cColor)
    circle.draw(cWin)

cirSz = 50
cirCol = "blue"

bullWin = GraphWin("Bullseye!", cirSz * 10, cirSz * 10)
bullWin.setCoords(0, 0, cirSz * 10, cirSz * 10)

draw_cir(cirSz*5, cirSz*5, 50, cirCol, bullWin) 

#bCircle = Circle(Point(450,450), 25.5)
#bCircle.setFill(color_rgb(10,10,235))
#bCircle.draw(bullWin)

bullWin.getMouse()
bullWin.close()
