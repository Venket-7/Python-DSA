"""
Maximum Sum of Subarray using Sliding Window

Sliding Window technique is used to find the maximum sum
of a contiguous subarray of given size.

Instead of calculating every subarray sum again and again,
we slide the window by one position and update the sum.

This reduces time complexity.

PROBLEM:
Find maximum sum of subarray of size k.

ALGORITHM:
STEP 1: Read array elements
STEP 2: Read subarray size k
STEP 3: Find sum of first k elements
STEP 4: Store it as maxsum
STEP 5: Slide window one by one:
        Add next element
        Remove first element of previous window
STEP 6: Update maxsum if current sum is greater
STEP 7: Print maximum sum

TIME COMPLEXITY : O(n)
SPACE COMPLEXITY: O(1)
"""

def max_sum(arr, size):

    # If window size is greater than array size
    if size > len(arr):
        return None

    windowsum = 0
    maxsum = 0

    # Sum of first window
    for i in range(size):
        windowsum += arr[i]

    maxsum = windowsum

    # Slide the window
    for j in range(size, len(arr)):
        windowsum += arr[j]          # Add next element
        windowsum -= arr[j - size]  # Remove old element

        if windowsum > maxsum:
            maxsum = windowsum

    return maxsum


# Input
arr = list(map(int, input("Enter Array: ").split()))
size = int(input("Enter Size of Sub Array: "))

# Function call
maxsum = max_sum(arr, size)

print("Maximum Sum =", maxsum)