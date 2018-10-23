#ascending order
def insertionSort(array):           # Here the reference of the array 'arr' is passed to the function i.e. no copy of the array is formed, 
    for i in range(1, len(array)):  # array 'array' and 'arr' point to the same memory location.
        key = array[i]
        j = i - 1

        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
        print(i, ":", array)

arr = [5, 2, 4, 6, 1, 3]
insertionSort(arr)
print("Sorted :", arr)
