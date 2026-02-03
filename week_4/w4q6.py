#   A math research assistant is verifying test values for numerical experiments. 
#   Write a Python function to check whether a number is a perfect number. In 
#   number theory, a perfect number is a positive integer that is equal to the sum 
#   of its proper positive divisors, that is, the sum of its positive divisors 
#   excluding the number itself. Example:6, 28 etc. 


def perfect_num (n):
    sum = 0
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            sum+= i 
    if sum == n:
        return True
    else :
        return False

n = int(input("Enter a number : \n"))

if perfect_num(n):
    print("It's a perfect Number")
else:
    print("It's not a perfect Number")