#cake_project
from turtle import Screen, Turtle
from cakemakerandplatform3 import cakemakerandplatform

a = 0
b = 0
x = 0
y = 0
length = int(input("Please enter the length of one side of a table (between 200-300): "))
color = str(input("Please enter the color of the table: "))
size = int(input("Please enter the size of the cake (between 100-200): "))

print("Your cake is loading! Happy Birthday!")
print("Press any key to exit......")

cakemakerandplatform(a, b, size, x, y, color, length)











