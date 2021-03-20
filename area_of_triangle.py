import math

a = int(input("Enter the 1st side value:"))
b = int(input("Enter the 2nd side value:"))
c = int(input("Enter the 3rd side value:"))

s = (a + b + c)/2
area_of_triangle = math.sqrt(s*(s - a)*(s - b)*(s - c))
print("area of triangle as per herons formula",area_of_triangle)