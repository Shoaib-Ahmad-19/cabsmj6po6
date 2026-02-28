# A parser receives a mixed list of characters, symbols, and integers. 
# Write a program to extract and add only numeric items using isinstance().


l1 = [10, 3.14, "Hello", True, [1, 2, 3], (4, 5), {"name": "John"}]
sum = 0
for x in l1:
    if isinstance(x,int):
        sum +=x
print("The sum is : ", sum)