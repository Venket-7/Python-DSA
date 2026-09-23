# Two Pointers Technique
"""
What is Two Pointers?
-- The Two Pointers technique uses two index variables to traverse an array or string.
-- Instead of repeatedly checking every possible pair using nested loops,
we move the pointers strategically to reduce unnecessary comparisons.
-> Common approaches:
-- Opposite-direction pointers: One pointer starts at the beginning, and the other starts at the end.
-- Same-direction pointers: Both pointers move forward at different speeds or for different purposes.
"""

# Problem 1: Find a pair with a given sum in a sorted array

def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return [arr[left], arr[right]]

        elif total < target:
            left += 1

        else:
            right -= 1

    return None

arr = [1, 2, 4, 6, 8, 9]
target = 7
print(two_sum_sorted(arr, target))

## Problem 2: Check whether a string is a palindrome

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

text = "madam"

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")