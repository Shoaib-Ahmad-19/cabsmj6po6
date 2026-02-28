# A device logs data indexes between two given IDs. Given two numbers r1 
# and r2 (r1 < r2): Write a program to create a list of integers from r1 to r2 
# (inclusive) using range(). 

r1 =int(input("Enter first number :"))
r2 =int(input("Enter second number :"))
l1 = []
if (r1 < r2):
    for i in range(r1,r2+1):
        l1.append(i)
    print("The list is : ",l1)
else:
    print("Recheck input !")