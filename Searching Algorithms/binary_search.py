"""
Binary Search

Binary Search is a search algorithm that finds the position of a target value within a sorted array.

Logarithmic Time Complexity - O(log n).
Algorithm Design Strategy - Decrease and conquer.

Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the
whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval
to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval
is empty.
"""


def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # make sure to round it down
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# Driver code to test above

arr1 = [-2, 3, 4, 7, 8, 9, 11, 13]
assert search(arr1, 11) == 6
assert search(arr1, 13) == 7
assert search(arr1, -2) == 0
assert search(arr1, 8) == 4
assert search(arr1, 6) == -1
assert search(arr1, 14) == -1
assert search(arr1, -4) == -1

arr2 = [3]
assert search(arr2, 6) == -1
assert search(arr2, 2) == -1
assert search(arr2, 3) == 0

print("If you didn't get an assertion error, this program has run successfully.")
