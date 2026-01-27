# A math module checks sequence validity. Write a program to determine 
# whether a number is a Fibonacci number. 


def isValid(n):
    first = 0
    second = 1
    current = 0
    while(current <= n):
        if current == n :
            return True;
        current = first + second
        first = second
        second = current
    
    
    return False

n = int(input("Enter the number : "))
if(isValid(n)):
    print("It's a Fibonacci Number")
else:
    print("It's not a Fibonacci Number")