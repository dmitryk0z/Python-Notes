"""
Merge Sort

1) What it does?
    The implementation of the Quick Sort is based around the idea of selecting a pivot element from the given array and
    using that pivot element to partition the other elements of the array. This will result in breaking the array into
    sub-arrays (or partitions), where all elements that are positioned before the pivot will be smaller than the pivot
    and all elements that are positioned after the pivot will be greater than the pivot element. Using recursion, we
    repeat these steps for each sub-array until the original array is sorted. It is important to note that selection of
    the pivot element (partition strategy) can have major impact on algorithm runtime.

2) When to use?
    Merge Sort is also an efficient sorting algorithm that is used to sort different datasets. This algorithm does
    great job when it comes to sorting large datasets.

3) Stability:
    Stable (this is the ability of a sorting algorithm to keep the relative order of equal keys in a file).

4) Time Complexity:
    The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.

    -   Worst Case (Quadratic Time Complexity - O(n^2)): The worst case occurs when the partition process always
        picks greatest or smallest element as pivot. If we consider partition strategy where last element is
        always picked as pivot, the worst case would occur when the array is already sorted in increasing or
        decreasing order.
    -   Best Case (Linearithmic Time Complexity - O(n*log n)): The best case occurs when the partition process
        always picks the middle element as pivot.
    -   Average Case is also Linearithmic Time Complexity - O(n*log n).

5) Algorithm Design Strategy:
    Divide and Conquer.

6) Sorting In Place?
    No (means additional storage space is needed to perform sorting).

7) Adaptive (if it takes advantage of already 'sorted' elements in the list that is to be sorted)?
    No.
"""


def merge(arr, l, m, r):
    # copy the first half of the list into the variable n1
    # the +1 is used to include the middle element in the first half
    n1 = m - l + 1
    # copy the second half of the list into the variable n2
    n2 = r - m
    # create temp arrays with the indices held by n1 and n2
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    # in a range from 0 to n1
    for i in range(0, n1):
        # add to the lower index all elements until n1
        L[i] = arr[l + i]

        # in a range from 0 to n2 (last element)
    for j in range(0, n2):
        # add to the middle + 1 all elements until the last
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    # while you don't reach the end of each array, do...
    while i < n1 and j < n2:
        # compare the first element of each subarray
        if L[i] <= R[j]:
            # make the smallest one the first element of the sorted array
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
# this function tells who the middle element is


def mergesort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        # Sort first and second halves
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        # Merge the two halves
        merge(arr, l, m, r)


# Driver code to test above

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is", arr)

mergesort(arr, 0, n - 1)
print("\n\nSorted array is", arr)
