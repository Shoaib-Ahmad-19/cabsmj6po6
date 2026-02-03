#     A teacher wants to automate small mathematical tasks done repeatedly while 
#    checking assignments. Define separate Python functions to perform the 
#    following for the teacher: 
#    • Compute the average of any five marks obtained by a student. 
#    • Convert a given temperature from Celsius to Fahrenheit for recording lab 
#    conditions. 
#    • Calculate the perimeter of a rectangular notice board kept in the classroom 
#    using its length and width. 

def average():
    sum = 0
    for i in range(5):
        sum += int(input(f"Enter number {i} :\n"))
    return sum/5

def temperature():
    """returns Temperature"""
    return (int(input(f"Enter temperature in Celsius :\n"))*9/5) + 32


def perimeter():
    return 2*int(input("Enter Length of the Notice Board :\n"))*int(input("Enter Breadth of the Notice Board :\n"))

operation = input("Choose Operation :\na) Average\nb) Temperature\nc) Perimeter\n")

match operation:
    case 'a':
        print(f"The Average of Marks is : {average()}")
    case 'b':
        print(f"The Temperature in Farenheit is : {temperature()}")
    case 'c':
        print(f"The Perimeter of the given rectangle is : {perimeter()}")