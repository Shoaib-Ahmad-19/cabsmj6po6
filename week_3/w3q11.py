# A security system verifies prime-number-based keys. Write a program to 
# check whether an integer is prime, or else output its first factor.  

def prime_num(n):
    if n == 1:
        return False
    
    check = True
    for i in range (2, int(n/2)+1):
        if n %i == 0 :
            check = False
            break
    
    return check  

n = int(input("Enter a number : \n"))

if n <= 0:
    print("Invalid Input") 
elif prime_num(n):
    print("It's a Prime number")
else:
    print("It's not a Prime Number \nIt's First Factor is 1") 