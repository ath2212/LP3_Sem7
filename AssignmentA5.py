def partition(array, l, r):
    pivot = array[r]
    i = l 

    for j in range(l, r):
        if array[j] <= pivot:
            # i = i + 1
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[i], array[r] = array[r], array[i]

    return i

def quickSort(array, l, r):
    if l<r:
        pivot = partition(array, l, r)

        quickSort(array, l, pivot-1)
        quickSort(array, pivot+1, r)

array = [1, 3, 5, 2, 5 ,6, 2, 5, 2, 1, 2, 8, 9, 6, 4, 0]
quickSort(array, 0, len(array)-1)
print(array)