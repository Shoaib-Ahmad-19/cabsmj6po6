low, high = [],[]
flag = True
print("Enter Packet IDs (enter '0' to exit) : ")
while flag:
    num = int(input())
    if num == 0:
        flag = False
        continue
    else :
        high.append(num) if num&1 else low.append(num)

print("High Priority Packets are : ",high)
print("Low Priority Packets are : ",low)