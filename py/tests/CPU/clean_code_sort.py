from abc import ABC, abstractmethod
import sys

from utils import decorator

class AbstractSort(ABC):

    @abstractmethod
    def sort():
        pass
    

class BubbleSort(AbstractSort):
    def __init__(self, arr: list):
        self.array = arr
    
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def sort(self) -> list:
        ln = len(self.array)
        flag = 1
        
        while(flag):
            flag = 0
            for i in range(ln - 1):
                if (self.array[i] > self.array[i + 1]):
                    flag = 1
                    self.swap(self.array, i, i + 1)
        return self.array

class MeargeSort(AbstractSort):
    def __init__(self, arr: list):
        self.array = arr
    
    def calculate_n(self, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        
        return n1, n2
        
    
    def fill_LR_vectors(self, arr, left, mid, n1, n2):
        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[left + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]
        return L, R
        
    
    def merge(self, arr, left, mid, right):
        n1, n2 = self.calculate_n(left, mid, right)
        L, R = self.fill_LR_vectors(arr, left, mid, n1, n2)

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
    
    def merge_sort(self, arr: list, left: int, right: int):
        if left < right:
            mid = (left + right) // 2

            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

    def sort(self):
        left = 0
        right = len(self.array) - 1
        if left < right:
            mid = (left + right) // 2

            self.merge_sort(self.array, left, mid)
            self.merge_sort(self.array, mid + 1, right)
            self.merge(self.array, left, mid, right)


class QuickSort(AbstractSort):
    def __init__(self, arr: list):
        self.array = arr
        
    def partition(self, arr, low, high):
    
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
                self.swap(arr, i, j)
        
        # Move pivot after smaller elements and
        # return its position
        self.swap(arr, i + 1, high)
        return i + 1

    # Swap function
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    # The QuickSort function implementation
    def quickSort(self, arr, low, high):
        if low < high:
            
            # pi is the partition return index of pivot
            pi = self.partition(arr, low, high)
            
            # Recursion calls for smaller elements
            # and greater or equals elements
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
    
    def sort(self):
        self.quickSort(self.array, 0, len(self.array) - 1)    


@decorator
def test():
    x = [i for i in range(500, 0, -1)]
    
    y = [BubbleSort(x) for i in range(300)]
    y.extend([MeargeSort(x) for i in range(300)])
    y.extend([QuickSort(x) for i in range(300)])
    
    for i in y:
        i.sort()
    
if __name__ == '__main__':
    sys.setrecursionlimit(15000000)
    test()