#   A science lab technician is calculating the volume of spherical containers used 
#   for experiments. Write a Python function that accepts the radius and returns 
#   the volume of the sphere using the formula:

def volume(r):
    return (4/3)*(22/7) * r**3


r = int(input("Enter the radius of the Sphere :\n"))
if r >= 0 :
    print(f"The Volume of the Sphere is : {round(volume(r),4)}")
else :
    print("INVALID INPUT !!!")