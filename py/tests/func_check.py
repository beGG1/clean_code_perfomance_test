import random
import time

# Quicksort algorithm implemented as one big function
def quicksort_big(arr, low, high):
    if low < high:
        pivot = arr[high]  # Pivot element
        i = low - 1

        # Partitioning the array
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1

        # Recursively sort elements before and after partition
        quicksort_big(arr, low, pi - 1)
        quicksort_big(arr, pi + 1, high)

# Function to partition the array
def partition(arr, low, high):
    pivot = arr[high]  # Pivot element
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quicksort function that uses the partition function
def quicksort_small(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort_small(arr, low, pi - 1)
        quicksort_small(arr, pi + 1, high)

# Function to generate a random list of a given size
def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

def main():
    # Generate a random list for testing
    arr = generate_random_list(1000000)

    # Measure the execution time of the big function
    arr_big = arr[:]
    start_big = time.time()
    quicksort_big(arr_big, 0, len(arr_big) - 1)
    duration_big = time.time() - start_big
    print(f"Execution time of big function: {duration_big:.6f} seconds")

    # Measure the execution time of the small functions
    arr_small = arr[:]
    start_small = time.time()
    quicksort_small(arr_small, 0, len(arr_small) - 1)
    duration_small = time.time() - start_small
    print(f"Execution time of small functions: {duration_small:.6f} seconds")

if __name__ == "__main__":
    main()