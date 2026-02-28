# An architectural software checks the type of triangular panels used in design. 
# Write a program to: 
# • Compute the area of a triangle using its three sides. 
# • Print whether it is equilateral, isosceles, or scalene.

from math import sqrt

def area(a,b,c):
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

def isequilateral(a,b,c):
    if(a == b == c) :
        return True
    else :
        return False

def isTriangle(a,b,c):
    return (a <= b + c) and (b <= a + c) and (c <= a + b)

def isIsosceles(a,b,c):
    if(a == b) or (b == a) or (c == a):
        return True
    else :
        return False
    
a =int(input("Enter the length of first side of Triangle :"))
b =int(input("Enter the length of second side of Triangle :"))
c =int(input("Enter the length of third side of Triangle :"))


if isTriangle(a,b,c):
    print("The area of the trianlge is : ",area(a,b,c))

    if isequilateral(a,b,c):
        print("It is an Equilateral Triangle")
    elif isIsosceles(a,b,c):
        print("It is an Isosceles Triangle")
    else:
        print("It is a Scalene Triangle")
else:
    print("It's Not a Triangle")