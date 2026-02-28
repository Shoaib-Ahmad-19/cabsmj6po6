# Merge two lists of Product Ids and Display the Final list in Sorted Order

merge =[]
i,j = 0,0

l1 = sorted([1,5,5,8,3,151,63])
l2 = sorted([453,453,12,45,21,96])

while i < len(l1) and j < len(l2):
    if l1[i] <= l2[j] :
        merge.append(l1[i])
        i += 1
    else:
        merge.append(l2[j])
        j += 1

while i < len(l1):
    merge.append(l1[i])
    i += 1
    
while j < len(l2):
    merge.append(l2[j])
    j += 1
    
print(merge)