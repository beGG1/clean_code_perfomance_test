#include <iostream>
#include <vector>
#include <chrono>
#include <algorithm>

// Quicksort algorithm implemented as one big function
void quicksort_big(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivot = arr[high]; // Pivot element
        int i = (low - 1);

        // Partitioning the array
        for (int j = low; j <= high - 1; ++j) {
            if (arr[j] < pivot) {
                ++i;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        int pi = i + 1;

        // Recursively sort elements before and after partition
        quicksort_big(arr, low, pi - 1);
        quicksort_big(arr, pi + 1, high);
    }
}

// Function to partition the array
int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high]; // Pivot element
    int i = (low - 1);

    for (int j = low; j <= high - 1; ++j) {
        if (arr[j] < pivot) {
            ++i;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return (i + 1);
}

// Quicksort function that uses the partition function
void quicksort_small(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quicksort_small(arr, low, pi - 1);
        quicksort_small(arr, pi + 1, high);
    }
}

// Helper function to print the array
void printArray(const std::vector<int>& arr) {
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

// Function to generate a random vector of a given size
std::vector<int> generateRandomVector(int size) {
    std::vector<int> vec(size);
    std::generate(vec.begin(), vec.end(), std::rand);
    return vec;
}

// Main function to test and compare the performance of both implementations
int main() {
    // Generate a random vector for testing
    std::vector<int> arr = generateRandomVector(10000000);
    
    // Measure the execution time of the big function
    std::vector<int> arr_big = arr; // Copy original array
    auto start_big = std::chrono::high_resolution_clock::now();
    quicksort_big(arr_big, 0, arr_big.size() - 1);
    auto end_big = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration_big = end_big - start_big;
    
    // Measure the execution time of the small functions
    std::vector<int> arr_small = arr; // Copy original array
    auto start_small = std::chrono::high_resolution_clock::now();
    quicksort_small(arr_small, 0, arr_small.size() - 1);
    auto end_small = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration_small = end_small - start_small;

    // Output the results
    std::cout << "Execution time of big function: " << duration_big.count() << " seconds\n";
    std::cout << "Execution time of small functions: " << duration_small.count() << " seconds\n";

    return 0;
}