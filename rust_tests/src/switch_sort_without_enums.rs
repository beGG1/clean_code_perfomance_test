// Swap function
fn swap(arr: &mut [i32], i: usize, j: usize) {
    arr.swap(i, j);
}

// BubbleSort implementation
fn bubble_sort(mut array: Vec<i32>) -> Vec<i32> {
    let ln = array.len();
    let mut flag = true;

    while flag {
        flag = false;
        for i in 0..ln - 1 {
            if array[i] > array[i + 1] {
                flag = true;
                swap(&mut array, i, i + 1);
            }
        }
    }
    array
}

// Helper functions for MergeSort
fn calculate_n(left: usize, mid: usize, right: usize) -> (usize, usize) {
    let n1 = mid - left + 1;
    let n2 = right - mid;
    (n1, n2)
}

fn fill_lr_vectors(arr: &[i32], left: usize, mid: usize, n1: usize, n2: usize) -> (Vec<i32>, Vec<i32>) {
    let mut left_vec = vec![0; n1];
    let mut right_vec = vec![0; n2];

    for i in 0..n1 {
        left_vec[i] = arr[left + i];
    }
    for j in 0..n2 {
        right_vec[j] = arr[mid + 1 + j];
    }

    (left_vec, right_vec)
}

fn merge(arr: &mut [i32], left: usize, mid: usize, right: usize) {
    let (n1, n2) = calculate_n(left, mid, right);
    let (left_vec, right_vec) = fill_lr_vectors(arr, left, mid, n1, n2);

    let (mut i, mut j, mut k) = (0, 0, left);
    
    while i < n1 && j < n2 {
        if left_vec[i] <= right_vec[j] {
            arr[k] = left_vec[i];
            i += 1;
        } else {
            arr[k] = right_vec[j];
            j += 1;
        }
        k += 1;
    }

    while i < n1 {
        arr[k] = left_vec[i];
        i += 1;
        k += 1;
    }

    while j < n2 {
        arr[k] = right_vec[j];
        j += 1;
        k += 1;
    }
}

fn merge_sort(arr: &mut [i32], left: usize, right: usize) {
    if left < right {
        let mid = (left + right) / 2;
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// MergeSort entry function
fn merge_sort_upper(array: Vec<i32>) -> Vec<i32> {
    let mut arr = array;
    let ln = arr.len();
    merge_sort(&mut arr, 0, ln - 1);
    arr
}

// QuickSort helper functions
fn partition(arr: &mut [i32], low: usize, high: usize) -> usize {
    let pivot = arr[high];
    let mut i = low as isize - 1;

    for j in low..high {
        if arr[j] < pivot {
            i += 1;
            swap(arr, i as usize, j);
        }
    }
    swap(arr, (i + 1) as usize, high);
    (i + 1) as usize
}

fn quick_sort_helper(arr: &mut [i32], low: isize, high: isize) {
    if low < high {
        let pi = partition(arr, low as usize, high as usize);
        quick_sort_helper(arr, low, pi as isize - 1);
        quick_sort_helper(arr, pi as isize + 1, high);
    }
}

// QuickSort entry function
fn quick_sort(array: Vec<i32>) -> Vec<i32> {
    let mut arr = array;
    let ln = arr.len();
    quick_sort_helper(&mut arr, 0, ln as isize - 1);
    arr
}


pub fn test() {
    // Original data for sorting
    let data: Vec<i32> = (1..=5000).rev().collect();

    // Define the sorting jobs as a vector of tuples, each containing a sorting function reference and a copy of the data
    let mut sorting_jobs = vec![];

    // Add 300 jobs of each type with a cloned copy of `data`
    for _ in 0..300 {
        sorting_jobs.push((bubble_sort as fn(Vec<i32>) -> Vec<i32>, data.clone()));
        sorting_jobs.push((merge_sort_upper as fn(Vec<i32>) -> Vec<i32>, data.clone()));
        sorting_jobs.push((quick_sort as fn(Vec<i32>) -> Vec<i32>, data.clone()));
    }

    // Iterate over each sorting job and execute the sorting function
    for (sort_fn, arr) in sorting_jobs {
        _ = sort_fn(arr);  // Call the sorting function on `arr`
    }
}
