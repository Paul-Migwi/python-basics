import math 
#take input of the two sides of the right triangle 
a=float (input ("Enter the first side"))
b=float(input ("ENter the second side "))
#calc the square of each side 
a_squared =a**2
b_squared =b**2
# calculate the hypotenuse
hypotenuse=math.sqrt(a_squared + b_squared )
print("the hypotenuse of the triangle is :", hypotenuse)
