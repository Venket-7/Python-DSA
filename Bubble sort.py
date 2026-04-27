"""
Bubble Sort

Bubble Sort is a simple sorting technique used to arrange elements
in ascending or descending order.

It works by repeatedly comparing two adjacent elements and swapping
them if they are in the wrong order.

After each pass, the largest element moves to the end of the list,
just like a bubble rising to the top.

ALGORITHM:
STEP 1: Read the list of elements
STEP 2: Compare adjacent elements
STEP 3: If left element > right element, swap them
STEP 4: Continue until end of list
STEP 5: Repeat passes until list is sorted

TIME COMPLEXITY:
Best Case   : O(n)
Average Case: O(n²)
Worst Case  : O(n²)
"""

lst = list(map(int, input("Enter elements: ").split()))
n = len(lst)

for i in range(n - 1):                 
    for j in range(n - i - 1):        
        if lst[j] > lst[j + 1]:       
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Sorted list:", lst)