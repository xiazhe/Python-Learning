# Pythonic code
# pep8 --first quicksort.py


def quicksort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array

    pivot = array.pop()

    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)

    return quicksort(less) + [pivot] + quicksort(greater)


print quicksort([9, 8, 4, 5, 32, 64, 2, 1, 0, 10, 19, 27])
# [0, 1, 2, 4, 5, 8, 9, 10, 19, 27, 32, 64]
