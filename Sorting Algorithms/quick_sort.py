"""
Quicksort

1) What it does?
    It picks an element as pivot and partitions the given array around the picked pivot. There are many different
    versions of quickSort that pick pivot in different ways.

    - Always pick first element as pivot.
    - Always pick last element as pivot
    - Pick a random element as pivot.
    - Pick median as pivot.

    Choice of pivot depends on the dataset. Generally advised to randomly pick the pivot.

    The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as
    pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put
    all greater elements (greater than x) after x.

2) When to use?
    The quick sort cannot work well with large datasets. Quick sort is more efficient and works faster in case of
    smaller array size or datasets.

3) Different variations?
    Stable Quicksort.

4) Stability:
    Unstable (this is the ability of a sorting algorithm to keep the relative order of equal keys in a file).

5) Time Complexity:
    The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.

    -   Worst Case (Quadratic Time Complexity - O(n^2)): The worst case occurs when the partition process always
        picks greatest or smallest element as pivot. If we consider partition strategy where last element is
        always picked as pivot, the worst case would occur when the array is already sorted in increasing or
        decreasing order.
    -   Best Case (Linearithmic Time Complexity - O(n*log n)): The best case occurs when the partition process
        always picks the middle element as pivot.
    -   Average Case is also Linearithmic Time Complexity - O(n*log n).

6) Algorithm Design Strategy:
    Divide and Conquer.

7) Sorting In Place?
    Yes (means no additional storage space is needed to perform sorting).

8) Adaptive (if it takes advantage of already 'sorted' elements in the list that is to be sorted)?
    Yes.
"""


def quicksort(arr, left, right):
    if left >= right:
        return
    p = partition4(arr, left, right)

    quicksort(arr, left, p - 1)
    quicksort(arr, p + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def partition2(arr, left, right):
    pivot = arr[left]
    i = left
    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[left] = arr[left], arr[i]
    return i


def partition3(arr, left, right):
    mid = (right + left) // 2
    arr[right], arr[mid] = arr[mid], arr[right]
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def partition4(arr, left, right):
    pivot = arr[left + (right - left) // 2]
    arr[left + (right - left) // 2], arr[right] = arr[right], arr[left + (right - left) // 2]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


# Driver code to test above:

a1 = [45, 23, 11, 89, 77, 98, 4, 28, 65, 43]
a2 = [2, 4, 6]
a3 = []
a4 = [3, 1, -1, 0, 2, 5, 8, 7]
a5 = [2, 2, 1, 1, 0, 0, 4, 4, 2, 2, 2]
a6 = [0]
a7 = [3, -2, -1, 0, 2, 4, 1]
a8 = [1, 2, 3, 4, 5, 6, 7]
a9 = [2, 2, 2, 2, 2, 2, 2]

quicksort(a1, 0, len(a1) - 1)
quicksort(a2, 0, len(a2) - 1)
quicksort(a3, 0, len(a3) - 1)
quicksort(a4, 0, len(a4) - 1)
quicksort(a5, 0, len(a5) - 1)
quicksort(a6, 0, len(a6) - 1)
quicksort(a7, 0, len(a7) - 1)
quicksort(a8, 0, len(a8) - 1)
quicksort(a9, 0, len(a9) - 1)

assert a1 == [6, 8, 9, 10, 11, 14, 20, 60]
assert a2 == [2, 4, 6]
assert a3 == []
assert a4 == [-1, 0, 1, 2, 3, 5, 7, 8]
assert a5 == [0, 0, 1, 1, 2, 2, 2, 2, 2, 4, 4]
assert a6 == [0]
assert a7 == [-2, -1, 0, 1, 2, 3, 4]
assert a8 == [1, 2, 3, 4, 5, 6, 7]
assert a9 == [2, 2, 2, 2, 2, 2, 2]

print("If no assertion error, then the program has successfully sorted given arrays.")
