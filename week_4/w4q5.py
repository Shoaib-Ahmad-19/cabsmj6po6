#   An accountant wants a utility that extracts a digit-sum check value from 
#   transaction IDs. Write a Python function that returns the sum of digits of a 
#   given integer

def digitSum(n):
    sum = 0
    while(n>0):
        sum += n % 10
        n = n // 10
    return sum
        
n = int(input("Enter a number :\n"))
print(f"It's Sum is : {digitSum(n)}")