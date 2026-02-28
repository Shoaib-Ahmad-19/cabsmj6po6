# Recursive function of Fibonacci Sequence

def Fib(n):
    if n <= 1:
        return n
    else :
        return Fib(n-1) + Fib(n-2)
    
def print_fib(n):
    for i in range(n):
        print(Fib(i), end =" ")

n = int(input("Enter a number :"))
print(print_fib(n))
