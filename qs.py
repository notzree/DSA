"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array, l, r):
    pivot = array[r]
    i = l-1
    for j in range (l, r):
        if array[j] < pivot:
            i +=1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[r]) = (array[r], array[i + 1])
    return i+1


def qs(array, l , r ):
    if l>=r:
        return
    p = partition(array, l, r) #partition the array for the section between L and R 
    #P is the index of the pivot. 
    qs(array, l, p-1)
    qs(array, p+1, r)
    return array

def quicksort(array):
    qs(array,0,len(array)-1)
    return array
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print (quicksort(test))