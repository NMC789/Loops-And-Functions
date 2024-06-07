import turtle
bob = turtle.Turtle()

def drawNgon(myTurtle, numSides, sideLength):
    for i in range(numSides):
        bob.forward(sideLength)
        bob.left(360//numSides)

def drawNgonSpiral(myTurtle, numSides, sideLength, numShapes):
    for i in range(numShapes):
        drawNgon(bob, numSides, sideLength)
        bob.left(20)

drawNgonSpiral(bob, 6, 50, 35)
