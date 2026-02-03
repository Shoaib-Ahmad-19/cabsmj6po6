#  A data analyst needs factorial values to compute permutations. 
#  Write a Python function to calculate the factorial of a non-negative integer.

def fact(n):
    if n == 1 or n ==0:
        return 1
    else :
        return n*(n-1)
    
n = int(input("Enter a number : \n"))
if n >= 0 :
    print( f"The factorial of {n} is : ",fact(n))
else :
    print("Invalid Input !!")