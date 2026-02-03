#   A landscaping company maintains circular flower beds, each with an outer 
#   radius R and an inner unused radius r. The effective area used for fertilizer is   
#   Effective Area = 𝝅(𝑹𝟐 − 𝒓𝟐) 
#   Write a Python function that takes R and r from the user, validates that R > r, 
#   and returns the effective usable area

def effectiveArea():
    R = int(input("Enter Outer Radius : "))
    if R < 0:
        print("Invalid INPUT !!")
        return
    r = int(input("Enter Inner Radius : "))
    if r < 0 or R < r:
        print("Invalid INPUT !!")
        return

    print("The Effective Area is : ",(22/7)*(R-r)*(R + r))
    return 

effectiveArea()