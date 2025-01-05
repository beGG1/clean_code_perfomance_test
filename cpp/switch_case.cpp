#include <iostream>
#include <vector>
#include <chrono>
#include <sys/resource.h>
#include <cstring>

using namespace std;
using namespace std::chrono;

// Function to measure memory usage
size_t get_memory_usage() {
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    return usage.ru_maxrss; // in kilobytes
}

// Swap function
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// Bubble Sort function
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped;
    do {
        swapped = false;
        for (int i = 0; i < n - 1; ++i) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
    } while (swapped);
}

// Merge Sort functions
void merge(vector<int>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; ++i)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; ++j)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            ++i;
        } else {
            arr[k] = R[j];
            ++j;
        }
        ++k;
    }

    while (i < n1) {
        arr[k] = L[i];
        ++i;
        ++k;
    }

    while (j < n2) {
        arr[k] = R[j];
        ++j;
        ++k;
    }
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l >= r) return;

    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
}

// Quick Sort functions
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; ++j) {
        if (arr[j] < pivot) {
            ++i;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Measure performance function
template<typename Func, typename... Args>
void measure_perf(Func func, Args&&... args) {
    auto start = high_resolution_clock::now();
    func(std::forward<Args>(args)...);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Elapsed Time: " << duration.count() / 1e6 << " seconds" << endl;
}

// Test function
void test() {
    vector<int> x;
    for (int i = 1000; i > 0; --i) {
        x.push_back(i);
    }

    vector<vector<int>> arrays(900, x); // 300 BubbleSort, 300 MergeSort, 300 QuickSort

    for (int i = 0; i < 900; ++i) {
        switch (i / 300) {
            case 0:
                bubbleSort(arrays[i]);
                break;
            case 1:
                mergeSort(arrays[i], 0, arrays[i].size() - 1);
                break;
            case 2:
                quickSort(arrays[i], 0, arrays[i].size() - 1);
                break;
        }
    }
}

int main() {
    measure_perf(test);
    cout << "Memory Usage: " << get_memory_usage() / 1024.0 << " MB" << endl;
    return 0;
}