import turtle
bob = turtle.Turtle()
length = 5

def drawSquare(bob, squareSize):
    for i in range(4):
        bob.forward(squareSize)
        bob.right(90)
        
def drawRow(bob, length, squareSize):
    for i in range(length):
        drawSquare(bob, squareSize)
        bob.forward(squareSize)

def drawGrid(bob, size, squareSize):
    for i in range(size):
        drawRow(bob, length, squareSize)
        bob.penup()
        bob.backward(squareSize*length)
        bob.left(90)
        bob.forward(squareSize)
        bob.right(90)
        bob.pendown()
    
def drawSquareStairs(bob, height, squareSize):
    for i in range(height):
        global length
        drawRow(bob, length, squareSize)
        bob.penup()
        bob.backward(squareSize*length)
        bob.left(90)
        bob.forward(squareSize)
        bob.right(90)
        bob.pendown()
        length -= 1
        
    
drawSquareStairs(bob, 5, 50)
