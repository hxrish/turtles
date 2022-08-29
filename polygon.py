#This program will help you create your polygon 
import turtle
sides = int(input('How many sides are there in your polygon?: '))
length = int(input('What is the length of the side in your polygon?: '))
color = input('What color is the outline?: ')
fillcolor = input('What color is your polygon filled with?: ')
wn = turtle.Screen()
artist = turtle.Turtle()
artist.color(color, fillcolor)

artist.begin_fill()
for _ in range(sides):
    artist.forward(length)
    artist.left(360/sides)

artist.end_fill()

wn.endonclick()
