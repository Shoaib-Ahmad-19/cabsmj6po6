def surfaceArea(length,breadth,height):
    return 2*(length*breadth + length*height + breadth*height)


def volume(length,breadth,height):
    return length*breadth*height


length = int(input("Enter the length : "))
breadth = int(input("Enter the breadth : "))
height = int(input("Enter the height : "))

print(f"The Surface Area of Cuboid is : {surfaceArea(length,breadth,height)}")
print(f"The Volume of Cuboid is : {volume(length,breadth,height)}")