## Insertion Sort
"""
Concept:
Insertion Sort builds a sorted portion of the array one element at a time.
It takes each new element and inserts it into its correct position
among the elements that have already been sorted.
"""

arr = list(map(int, input().split()))
for i in range(1, len(arr)):
    j= i
    while arr[j - 1] > arr[j] and j > 0:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1
print("Sorted list:", arr)