"""

Binary :: Binary Search works on sorted list only repeatedly dividing the list into half
ALGORITHM :
STEP 1: Find the middle element
STEP 2: If key double middle found
STEP 3: If key < middle ----> left half
STEP 4; If key > middle ----> right half

"""
lst = list(map(int, input("Enter sorted elements : ").split()))
key = int(input("Enter key : "))

left = 0
right = len(lst) - 1
f = True

while left <= right:
    mid = (left + right) // 2

    if lst[mid] == key:
        f = False
        print("Object found at index :", mid)
        break

    elif key < lst[mid]:
        right = mid - 1  

    else:
        left = mid + 1    

if f:
    print("Object not found")