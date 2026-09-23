
## Selection Sort

"""
Concept:
Selection Sort repeatedly finds the smallest element
from the unsorted portion of the array and places it at the beginning.
"""
# Code:

arr = list(map(int, input().split()))
n = len(arr)

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)