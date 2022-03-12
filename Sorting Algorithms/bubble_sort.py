"""
Bubble Sort

1) What it does?
    Bubble Sort is based on the idea of repeatedly comparing pairs of adjacent elements and then swapping their
    positions if they exist in the wrong order. If a list of elements has to be sorted in ascending order, then Bubble
    Sort will start by comparing the first element of the list with the second one. If the first element is greater
    than the second one, it will swap both elements and move on to compare the second and third element, and so on.

2) When to use?
    Bubble Sort is often considered an inefficient sorting tool since it must exchange items before the final
    locations of the elements are known. However, Bubble Sort is a good strategy to organize elements that are already
    partially sorted.

3) Stability:
    Stable (this is the ability of a sorting algorithm to keep the relative order of equal keys in a file).

4) Time Complexity:

    -   Worst Case and Average Case (Quadratic Time Complexity - O(n^2)): Worst case occurs when array is reverse
        sorted.
    -   Best Case (Linear Time Complexity - O(n)): Best case occurs when array is already sorted.

5) Algorithm Design Strategy:
    Brute Force.

6) Sorting In Place?
    Yes (means no additional storage space is needed to perform sorting).

7) Adaptive (if it takes advantage of already 'sorted' elements in the list that is to be sorted)?
    Yes.
"""


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble(list_a):
    indexing_length = len(list_a) - 1
    sort = False

    while not sort:
        sort = True

        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sort = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a


# Driver code to test above

arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [1, 2, 3, 4, 6, 5]
bubble(arr1)

print(arr1)
