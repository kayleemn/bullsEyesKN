#bullsEyes by Kaylee

from graphics import*

def draw_cir(Cx, Cy, size, color, bullWin):
    circle = circle(Point(Cx, Cy),Point(Cx, Cy))
    circle.setFill(color)
    circle.draw(bullWin)

cirSz = 50
cirCol = "blue"

bullWin = GraphWin("Bullseye!", cirSz * 10, cirSz * 10)
bullWin.setCoords(0, 0, 900, 900)

bCircle = Circle(Point(450,450), 25.5)
bCircle.setFill(color_rgb(10,10,235))
bCircle.draw(bullWin)

bullWin.getMouse()
bullWin.close()
