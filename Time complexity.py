# O(1) - Constant time
# Regardless of the size of the input, the time taken remains constant.
a = [10,11,12,13,14,15]
print(a[0] + a[2])
print(a[1])
print(a[2])

# O(n) - Linear time
# The time taken increases linearly with input size.
a = [10,11,12,13,14,15,16,17,18,19,20]
for i in range(len(a)):
    print(a[i])

# O(n^2) - Quadratic time
# The time taken increases quadratically with input size.
n = int(input())
for i in range(1, n):      # n times
    for j in range(1, n):  # n times
        print(i, j)

# O(log n) - Logarithmic time
# The time taken increases logarithmically with input size.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
target = 5
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")

# O(n log n) - Linearithmic time
# Example: Merge Sort / Quick Sort (average case)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

a = [12, 5, 7, 3, 9, 1]
merge_sort(a)
print(a)