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
