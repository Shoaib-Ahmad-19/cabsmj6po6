# A game engine verifies whether level IDs are arranged in a proper continuous 
# sequence. Write a Python program to check whether a given list of numbers 
# is consecutive.

def is_consecutive(nums):
    if len(nums) == 0:
        return False
    
    return (max(nums) - min(nums) + 1 == len(nums)) and (len(set(nums)) == len(nums))



numbers = [4, 2, 3, 5, 1]
if is_consecutive(numbers):
    print("The list contains consecutive numbers.")
else:
    print("The list does NOT contain consecutive numbers.")