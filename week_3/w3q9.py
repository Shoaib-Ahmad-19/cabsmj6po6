#  A biology simulation needs repeated multiplication. Write a program to 
# compute the factorial of an integer using a loop.

n = int(input("Enter the number : "))

result = 1
for i in range(1,n+1):
    result *= i
   
print(f"The Factorial of {n} is : {result}")