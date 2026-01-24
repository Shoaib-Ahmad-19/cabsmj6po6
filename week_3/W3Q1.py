def sum(arr):
    sum = 0
    for a in arr:
        sum += a
    return sum

def product(arr):
    result = 1
    for a in arr:
        result *= a
    return result

def avg(arr):
    return sum(arr)/len(arr)

n = int(input("Enter the number of values : "))
arr = [int(input(f"Enter {i+1} value : \n")) for i in range(n) ]

print(f"The Sum : {sum(arr)}")
print(f"The Product : {product(arr)}")
print(f"The Average : {avg(arr)}")
# for i in range(n):
#     arr[i] = int(input(f"Enter {i+1} value : "))