"""
File Input and Output

Python program to ask the user to type in 10 integer values, calculate the average and standard deviation of the values,
write the 10 values and the average and standard deviation to a file (called Results.txt).
"""

from statistics import stdev


def avg_and_st_dev(arr):
    """
    Function to calculate average and standard deviation of the values provided in the list (expects integers).
    :param arr: List of integers (values provided by the user)
    :return: List of two elements: [0] - average | [1] - standard deviation
    """
    try:
        res = [sum(arr) / len(arr), stdev(arr)]
        return res
    except TypeError as e:
        print("\nEnsure that the param 'arr' stores numbers only to avoid the following error:", e)


def write_file(arr, res):
    """
    Function to create the file "Results.txt" and write 10 values, the average and standard deviation to a file.
    :param arr: List of integers (values provided by the user)
    :param res: List of two elements: [0] - average | [1] - standard deviation
    :return: No return value
    """
    try:
        with open('D:/Results.txt', 'w') as f:
            for i in arr:
                f.write(str(i))
                f.write('\n')

            f.write('Average: ')
            f.write(str(res[0]))
            f.write(' Standard Dev: ')
            f.write(str(res[1]))

            print('File created')
    except IOError as e:
        print('\nSomething went wrong -->', e)


def main():
    arr_int = []
    print('\nPlease provide 10 integers:')
    try:
        for i in range(10):
            arr_int.append(int(input()))
        res = avg_and_st_dev(arr_int)
        write_file(arr_int, res)
    except ValueError as e:
        print('\nPlease provide integers only to avoid the following error:', e)
        main()


if __name__ == '__main__':
    main()
