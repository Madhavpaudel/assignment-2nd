import turtle


# Function to draw the edge shape recursively
def edge(sam, length, depth):
    # if we are at the base case, draw a straight line
    if depth == 0:
        sam.forward(length)
    # else break the line into 3 segments and drawing the edge for every depth till we reach base case
    else:
        length = length / 3
        edge(sam, length, depth - 1)
        # turning right by 60 degrees for equilateral triangle
        sam.right(60)
        edge(sam, length, depth - 1)
        # then left by 120 degrees
        sam.left(120)
        edge(sam, length, depth - 1)
        # then right by 60 degrees to complete the shape
        sam.right(60)
        edge(sam, length, depth - 1)


# taking user inputs for number of sides, length of each side and recursion depth
sides = int(input("Enter number of sides::"))
length = int(input("Enter side length (pixels)::"))
depth = int(input("Enter recursion depth::"))

# setting up the turtle
sam = turtle.Turtle()
# setting the starting point of the turtle
sam.penup()
sam.goto(-length, length / 4)
sam.pendown()

# drawing the shape by calling edge function for each side
for i in range(sides):
    edge(sam, length, depth)
    # turning the shape to draw the next side
    sam.right(360 / sides)
delay = input("Press Enter to exit...")
