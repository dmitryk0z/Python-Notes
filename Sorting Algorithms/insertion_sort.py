"""
Insertion Sort

1) What it does?
    Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
    The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and
    placed at the correct position in the sorted part.

    To sort an array of size n in ascending order:
        1:  Iterate from arr[1] to arr[n] over the array.
        2:  Compare the current element (key) to its predecessor.
        3:  If the key element is smaller than its predecessor, compare it to the elements before. Move the greater
            elements one position up to make space for the swapped element.

2) When to use?
    Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted,
    only few elements are misplaced in complete big array. Not suitable for large data volumes where it looses against
    other sorting algorithms.

3) Different variations?
    Binary Insertion Sort.

4) Stability:
    Stable (this is the ability of a sorting algorithm to keep the relative order of equal keys in a file).

5) Time Complexity:

    -   Worst Case and Average Case (Quadratic Time Complexity - O(n^2)): Worst case occurs when array is reverse
        sorted.
    -   Best Case (Linear Time Complexity - O(n)): Best case occurs when array is already sorted. During each
        iteration, the first remaining element of the input is only compared with the right-most element of the
        sorted subsection of the array.

6) Algorithm Design Strategy:
    Brute Force.

7) Sorting In Place?
    Yes (means no additional storage space is needed to perform sorting).

8) Adaptive (if it takes advantage of already 'sorted' elements in the list that is to be sorted)?
    Yes.
"""


def insert_sort(arr):

    """ Increasing Insertion Sort """

    for j in range(len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

    return arr


def dec_insert_sort(arr):

    """ Decreasing Insertion Sort """

    for j in range(len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

    return arr


list_a = [5, 2, 4, 6, 1, 3]

print(insert_sort(list_a))
print(dec_insert_sort(list_a))
