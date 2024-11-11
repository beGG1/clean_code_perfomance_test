import sys
from copy import deepcopy

from utils import decorator
   
    
def buble_sort(array: list) -> list:
    ln = len(array)
    flag = 1
        
    while(flag):
        flag = 0
        for i in range(ln - 1):
            if (array[i] > array[i + 1]):
                flag = 1
                array[i], array[i+1] = array[i+1], array[i]
    return array

   
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    
def merge_sort(arr: list, left: int, right: int):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge_sort_upper(array):
    left = 0
    right = len(array) - 1
    if left < right:
        mid = (left + right) // 2

        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)


       
def partition(arr, low, high):
    
        # Choose the pivot
    pivot = arr[high]
        
        # Index of smaller element and indicates 
        # the right position of pivot found so far
    i = low - 1
        
        # Traverse arr[low..high] and move all smaller
        # elements to the left side. Elements from low to 
        # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
        # Move pivot after smaller elements and
        # return its position
    arr[i + 1], arr[high] = arr[high], arr[i+1]
    return i + 1

    # The QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
            
            # pi is the partition return index of pivot
        pi = partition(arr, low, high)
            
            # Recursion calls for smaller elements
            # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    
def quick_sort(array):
    quickSort(array, 0, len(array) - 1)    


@decorator
def test():
    x = [i for i in range(500, 0, -1)]
    
    y = [(0, deepcopy(x)) for i in range(300)]
    y.extend([(1, deepcopy(x)) for i in range(300)])
    y.extend([(2, deepcopy(x)) for i in range(300)])
    
    for i, a in y:
        match i:
            case 0:
                buble_sort(a)
                break
            case 1:
                merge_sort_upper(a)
                break
            case 2:
                quick_sort(a)
                break
            case _:
                break
    
if __name__ == '__main__':
    sys.setrecursionlimit(15000000)
    test()