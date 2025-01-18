use rand::Rng;
use std::time::Instant;

// Quicksort algorithm implemented as one big function
fn quicksort_big(arr: &mut [i32], low: isize, high: isize) {
    if low < high {
        let pivot = arr[high as usize]; // Pivot element
        let mut i = low - 1;

        // Partitioning the array
        for j in low..high {
            if arr[j as usize] < pivot {
                i += 1;
                arr.swap(i as usize, j as usize);
            }
        }
        arr.swap((i + 1) as usize, high as usize);
        let pi = i + 1;

        // Recursively sort elements before and after partition
        quicksort_big(arr, low, pi - 1);
        quicksort_big(arr, pi + 1, high);
    }
}

// Function to partition the array
fn partition(arr: &mut [i32], low: isize, high: isize) -> isize {
    let pivot = arr[high as usize]; // Pivot element
    let mut i = low - 1;

    for j in low..high {
        if arr[j as usize] < pivot {
            i += 1;
            arr.swap(i as usize, j as usize);
        }
    }
    arr.swap((i + 1) as usize, high as usize);
    i + 1
}

// Quicksort function that uses the partition function
fn quicksort_small(arr: &mut [i32], low: isize, high: isize) {
    if low < high {
        let pi = partition(arr, low, high);

        quicksort_small(arr, low, pi - 1);
        quicksort_small(arr, pi + 1, high);
    }
}

// Function to generate a random vector of a given size
fn generate_random_vector(size: usize) -> Vec<i32> {
    let mut rng = rand::thread_rng();
    (0..size).map(|_| rng.gen_range(0..10000)).collect()
}

fn main() {
    // Generate a random vector for testing
    let arr = generate_random_vector(10000000);

    // Measure the execution time of the big function
    let mut arr_big = arr.clone();
    let arr_big_len = arr_big.len() as isize; // Get the length before passing the mutable reference
    let start_big = Instant::now();
    quicksort_big(&mut arr_big, 0, arr_big_len - 1);
    let duration_big = start_big.elapsed();
    println!(
        "Execution time of big function: {:.6} seconds",
        duration_big.as_secs_f64()
    );

    // Measure the execution time of the small functions
    let mut arr_small = arr.clone();
    let arr_small_len = arr_small.len() as isize; // Get the length before passing the mutable reference
    let start_small = Instant::now();
    quicksort_small(&mut arr_small, 0, arr_small_len - 1);
    let duration_small = start_small.elapsed();
    println!(
        "Execution time of small functions: {:.6} seconds",
        duration_small.as_secs_f64()
    );
}