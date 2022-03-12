"""
Selection Sort

1) What it does?
    The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

    -   The subarray which is already sorted.
    -   Remaining subarray which is unsorted.

    In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted
    subarray is picked and moved to the sorted subarray.

2) When to use?
    Inefficient on large lists, and generally performs worse than the similar insertion sort.

3) Stability:
    Unstable (this is the ability of a sorting algorithm to keep the relative order of equal keys in a file).

4) Time Complexity:

    -   Worst Case (Quadratic Time Complexity - O(n^2)): as there are two nested loops.

5) Algorithm Design Strategy:
    Brute Force.

6) Sorting In Place?
    Yes (means no additional storage space is needed to perform sorting).

7) Adaptive (if it takes advantage of already 'sorted' elements in the list that is to be sorted)?
    No.
"""


def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

                # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Driver code to test above

arr1 = [64, 25, 12, 22, 11]
selection_sort(arr1)

print(arr1)
