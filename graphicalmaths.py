import math
           #area of circle and circumference#
# radius = int(input("enter the radius of the circle"))
# area = math.pi * radius * radius;
# circ = 2 * math.pi * radius
# print("Area of circle is ", area)
# print("circference of circle",circ)
           #area of square and perimeter#
# side = int(input("enter of the square"))
# area = side * side
# perimeter = 4 * side
# print("area of square is ",area)
# print("area of perimeter is ",perimeter)

               #area of rectangle
# length = float(input("enter the length of rectangle : "))
# breadth = int(input("enter the breadth of rectangle : "))
# area = length * breadth
# perimeter = 2 *(length + breadth)
# print("area of rectangle is",area)
# print("area of perimeter is ",perimeter)
                       #  Area of traingle
side1 = int(input("enter the side1 of triangle:"))
side2 = int(input("enter the side2 of triangle:"))
side3 = int(input("enter the side3 of triangle"))
s = (side1 + side2 + side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
per = side1 + side2 + side3
print("area of triangle is ",area)
print("per of triangle is",per)




