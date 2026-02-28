#  find second largest number in a list using the Bubble Sort.

def swap(x,y):
    return y,x

n = int(input("Enter the length of the list : "))
l1 = []
for i in range(n):
    l1.append(int(input("Enter a number : ")))

for i in range(n):
    for j in range(n-i-1):
        if l1[j] > l1[j+1]:
            l1[j],l1[j+1] = swap(l1[j],l1[j+1])  
    if i == 2:
        break
    
print(l1[n-2])

print(l1)