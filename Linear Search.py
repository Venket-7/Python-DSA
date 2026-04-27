"""

Linear Search Algorithm
STEP1: Start from the first element
STEP2: Compare key with each element
STEP3: If element found return the index
STEP4: if end reached return not found

"""

# Implementation of Linear Search Algorithm in Python 

ls=list(map(int,input("Enter elements :").split()))
number=int(input("Enter number to be searched :"))
for i in range(len(ls)):
    if ls[i] == number:
        print("Object Found at index :",i)
        break
