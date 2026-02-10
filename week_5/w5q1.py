# A data automation team is creating a utility module that performs multiple 
# independent calculations based on user inputs. Write a Python program that 
# accepts required inputs from the user and defines separate functions to 
# perform: 
# • Find the largest of three numbers (positional arguments). 
# • Compute the volume based on user’s chosen shape: – cylinder (r, h), cube (a), or rectangular box (l, w, h). 
# • Compute the area of a rectangle. 
# • Compute the circumference of a circle. 
# • Exchange the values of two variables. 
# • Find the distance between two points (x1, y1) and (x2, y2) using math.dist(). 
# (Use switch case to execute the required function)
def cylinder(r,h):
    print(f"The Volume of given Cylinder is : {(22/7)*r*r*h}")

def cube(a):
    print(f"The Volume of given cube is : {a**3}")

def rect_box(l,w,h):
    print(f"The Volume of given Rectangular Box is : {l*w*h}")

def largest(a,b,c):
    return max(a,b,c)

def volume():
    s = int(input("Enter Shape :\n1) Cylinder\n2) Cube\n3) Rectangular Box"))
    match s:
        case 1:
            cylinder(int(input("Enter radius:")),int(input("Enter height:")))
        case 2:
            cube(int(input("Enter the length of Sides:")))
        case 3:
            rect_box(int(input("Enter length:")),int(input("Enter width:")),int(input("Enter height:")))
            
def areaOfRectangle():
    print(f"The Area of the Rectangle is : {int(input('Enter length:'))*int(input('Enter breadth:'))}")

def circumference():
    res = 2*(22/7)*int(input('Enter radius:'))
    print(f"The Circumference of the given circle is : {res}")
    
def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    print(f"A = {a}, B = {b}")
    
def distance():
    x1,y1 = int(input('Enter X1:')),int(input('Enter Y1:'))
    x2,y2 = int(input('Enter X2:')),int(input('Enter Y2:'))
    
    print("The distance between given two points is : {math.sqrt((x2-x1)**2 + (y2-y1)**2)}")
    

n = int(input("Enter the Operation number : \n1) Find the largest of three numbers\n2) Compute the volume\n3) Compute the area of a rectangle\n4) Compute the circumference of a circle\n5) Exchange the values of two variables\n6) Find the distance between two points"))
match n:
    case 1:
        print(f"The Largest number is {largest(int(input('Enter first number :')),int(input('Enter Second number :')),int(input('Enter third number :')))}")
    case 2:
        volume()
    case 3:
        areaOfRectangle()
    case 4:
        circumference()
    case 5:
        swap(int(input('Enter value of A:')),int(input('Enter value of B:')))
    case 6:
        distance()