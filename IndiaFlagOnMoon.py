# MonChefDoeuvre1237.py
# description: A program to draw the Indian flag on the south
#              pole of the moon using Python's Turtle module.
# author: Pranay Ratan
# date: Today's Date
# Date (last modified): T Oct. 25/10/23

#importing the required libraries
import turtle
import random

# Void function to draw a rectangle of a specific color 
# and mentioned coordinates
def draw_rectangle(t, color, x, y, width, height):
    # positioning turtle
    position_turtle(t, x, y)
    # filling it with color
    t.begin_fill()
    t.fillcolor(color)
    # starting a for loop to trace the path
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    return None

# Void function to position the turtle
def position_turtle(t, x, y):
    t.penup()
    # positioning turtle
    t.goto(x, y)
    t.pendown()
    return None

# Void function to draw a circle
def draw_circle(t, x, y, radius, color):
    t.penup()
    # positioning turtle
    t.goto(x, y-radius)
    t.pendown()
    # filling it with color
    t.color(color)
    #tracing it to the desired radius
    t.circle(radius)
    t.end_fill()
    return None


# Void function to draw spokes 
def draw_spokes(t, x, y, radius):
    angle = 360 / 24
    #starting the for loop for the desired number of spokes
    for _ in range(24):
        t.penup()
        # positioning turtle
        t.goto(x, y-radius)
        t.pendown()
        t.forward(radius)
        t.backward(radius)
        t.left(angle)
    return None    
# Function to create a turtle and set its speed
def create_turtle():
    # creating turtle
    t = turtle.Turtle()
    # setting its speed
    t.speed(20)
    return t



# Function to create Stars in the background
def draw_star(t, x, y, size=3):
    t.penup()
    # positioning turtle
    t.goto(x, y)
    t.pendown()
    t.color("white")
    # filling it with color
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    return None
# Function to make the background starry
def draw_starry_background(t, num_stars):
    for _ in range(num_stars):
        # setting the range in which it will be created
        x = random.randint(-450, 450) 
        y = random.randint(-300, 350)
        draw_star(t, x, y)
    return None
# Drawing moon's surface 
def draw_moon_surface(t):
    # Setting background color
    screen = turtle.Screen()
    screen.bgcolor("Black")
    draw_starry_background(t, 40)
    # Create a white semi-circle
    t.penup()
    # Position the turtle at the center bottom
    t.goto(600, -800)  
    # Point turtle upwards
    t.setheading(90)  
    t.pendown()
    t.color("light grey")
    t.begin_fill()
    # Draw a semi-circle
    t.circle(600, 180) 
    t.end_fill() 
    t.hideturtle()
    return None

# Main function to draw the flag and the backgrounbd
def main():
    # Creating a turtle
    t = create_turtle()
    # Drawing the moon surface
    draw_moon_surface(t)
    # Drawing the orange part
    draw_rectangle(t, "#FF9933", 350, 150, 100, 700)
    # Drawing the white part
    draw_rectangle(t, "white", 350, 50, 100, 700)
    # Drawing the green part
    draw_rectangle(t, "#138808", 350, -50, 100, 700)
    # Drawing the Ashoka Chakra
    draw_circle(t, -50, 50, 50, "blue")
    # Drawing the 24 spokes
    draw_spokes(t, 0, 50, 50)
    # Hiding the turtle and display the result
    turtle.hideturtle()
    turtle.exitonclick()

# Calling the main function
main()
