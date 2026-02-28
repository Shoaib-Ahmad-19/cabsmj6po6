# An architectural software checks the type of triangular panels used in design. 
# Write a program to: 
# • Compute the area of a triangle using its three sides. 
# • Print whether it is equilateral, isosceles, or scalene.

from math import sqrt

def area(a,b,c):
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

def isequilateral(a,b,c):
    if(a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
        return True
    else :
        return False


def isIsosceles(a,b,c):
    if(a == b) or (b == a) or (c == a):
        return True
    else :
        return False
    
a =int(input("Enter the length of first side :"))
b =int(input("Enter the length of second side :"))
c =int(input("Enter the length of third side :"))


print("The area of the trianlge is : ",area(a,b,c))

if isequilateral(a,b,c):
    print("It is an Equilateral Triangle")
elif isIsosceles(a,b,c):
    print("It is an Isosceles Triangle")
else:
    print("It is a Scalene Triangle")