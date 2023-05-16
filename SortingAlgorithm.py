#BUBBLE SORT
def bubble_sort(array):
    n = len(array)
    #Tranverse through all array elements
    for i in range(n):
        #Last i elements are already sorted
        for j in range(0, n-i-1):
            #Swap if the element found is gretaer than the next element
            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort([1,2,4,24,2,5,3]))
    
#SELECTION SORT
def selection_sort(array):
    n = len (array)
    #Tranverse through all array elements
    for i in range (n):
        #Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        #Swap the found minimum element with the first elemen
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

#Use Hash Table to solve the questions here.
#Use Set to solve the questions also.

#INSERTION SORT
def insertionSort(array):
    for step in range(1, len(array)):
        key = array(step)
        j = step - 1
        # Compare key with each element on the left of it until an element smaller is found
        # For descending order, change keyarray[j] to key>array[j]
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        #Place key at after the element just smaller than it
        array[j + 1] = key

#MERGE SORT 
def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = array(mid)
    right = array[mid:]
