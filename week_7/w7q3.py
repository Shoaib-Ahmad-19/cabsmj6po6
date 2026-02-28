# Recursive Function of Factorial n

def fact(n):
    if n < 0:
        return -1
    elif n in [0,1]:
        return 1
    else:
        return n*fact(n-1)
    

num = int(input("Enter a number : "))

print(f"The Factorial of {num} is {fact(num)}")