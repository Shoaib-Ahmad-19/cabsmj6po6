# A grading system compares three internal-assessment scores. 
# Write a program to find the highest score among the three, using only if 
# statements.

a =int(input("Enter first number :"))
b =int(input("Enter second number :"))
c =int(input("Enter third number :"))

if a>b :
    if a>c:
        print(f"{a} is the highest score")
    else:
        print(f"{c} is the highest score")
else:
    if b>c:
        print(f"{b} is the highest score")
    else:
        print(f"{c} is the highest score")