// Define the Sort trait
trait Sort {
    fn sort(&mut self) -> Vec<i32>;
}

// BubbleSort implementation
struct BubbleSort {
    array: Vec<i32>,
}

impl BubbleSort {
    fn new(arr: Vec<i32>) -> Self {
        BubbleSort { array: arr }
    }

    fn swap(arr: &mut [i32], i: usize, j: usize) {
        arr.swap(i, j);
    }
}

impl Sort for BubbleSort {
    fn sort(&mut self) -> Vec<i32> {
        let ln = self.array.len();
        let mut flag = true;

        while flag {
            flag = false;
            for i in 0..ln - 1 {
                if self.array[i] > self.array[i + 1] {
                    flag = true;
                    Self::swap(&mut self.array, i, i + 1);
                }
            }
        }
        self.array.clone()
    }
}

// MergeSort implementation
struct MergeSort {
    array: Vec<i32>,
}

impl MergeSort {
    fn new(arr: Vec<i32>) -> Self {
        MergeSort { array: arr }
    }

    fn merge(&mut self, left: usize, mid: usize, right: usize) {
        let n1 = mid - left + 1;
        let n2 = right - mid;

        let left_vec = self.array[left..left + n1].to_vec();
        let right_vec = self.array[mid + 1..mid + 1 + n2].to_vec();

        let (mut i, mut j, mut k) = (0, 0, left);

        while i < n1 && j < n2 {
            if left_vec[i] <= right_vec[j] {
                self.array[k] = left_vec[i];
                i += 1;
            } else {
                self.array[k] = right_vec[j];
                j += 1;
            }
            k += 1;
        }

        while i < n1 {
            self.array[k] = left_vec[i];
            i += 1;
            k += 1;
        }

        while j < n2 {
            self.array[k] = right_vec[j];
            j += 1;
            k += 1;
        }
    }

    fn merge_sort(&mut self, left: usize, right: usize) {
        if left < right {
            let mid = (left + right) / 2;
            self.merge_sort(left, mid);
            self.merge_sort(mid + 1, right);
            self.merge(left, mid, right);
        }
    }
}

impl Sort for MergeSort {
    fn sort(&mut self) -> Vec<i32> {
        let right = self.array.len() - 1;
        self.merge_sort(0, right);
        self.array.clone()
    }
}

// QuickSort implementation
struct QuickSort {
    array: Vec<i32>,
}

impl QuickSort {
    fn new(arr: Vec<i32>) -> Self {
        QuickSort { array: arr }
    }

    fn partition(arr: &mut [i32], low: usize, high: usize) -> usize {
        let pivot = arr[high];
        let mut i = low;

        for j in low..high {
            if arr[j] < pivot {
                arr.swap(i, j);
                i += 1;
            }
        }
        arr.swap(i, high);
        i
    }

    fn quick_sort(&mut self, low: isize, high: isize) {
        if low < high {
            let pi = Self::partition(&mut self.array, low as usize, high as usize) as isize;
            self.quick_sort(low, pi - 1);
            self.quick_sort(pi + 1, high);
        }
    }
}

impl Sort for QuickSort {
    fn sort(&mut self) -> Vec<i32> {
        let high = self.array.len() as isize - 1;
        self.quick_sort(0, high);
        self.array.clone()
    }
}

// Test function to run all sorts
pub fn test() {
    let data = (1..=5000).rev().collect::<Vec<i32>>();
    let mut bubble_sorts: Vec<_> = (0..300).map(|_| BubbleSort::new(data.clone())).collect();
    let mut merge_sorts: Vec<_> = (0..300).map(|_| MergeSort::new(data.clone())).collect();
    let mut quick_sorts: Vec<_> = (0..300).map(|_| QuickSort::new(data.clone())).collect();


    for sorter in bubble_sorts.iter_mut() {
        sorter.sort();
    }
    for sorter in merge_sorts.iter_mut() {
        sorter.sort();
    }
    for sorter in quick_sorts.iter_mut() {
        sorter.sort();
    }
}

