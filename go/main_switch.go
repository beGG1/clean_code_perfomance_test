package main

// import (
// 	"fmt"
// 	"runtime"
// 	"time"
// )

// // Swap function to swap two elements in a slice
// func swap(arr []int, i, j int) {
// 	arr[i], arr[j] = arr[j], arr[i]
// }

// // Bubble Sort Implementation
// func bubbleSort(array []int) []int {
// 	n := len(array)
// 	for swapped := true; swapped; {
// 		swapped = false
// 		for i := 1; i < n; i++ {
// 			if array[i-1] > array[i] {
// 				swap(array, i-1, i)
// 				swapped = true
// 			}
// 		}
// 	}
// 	return array
// }

// // Merge Sort Helper Functions
// func merge(arr []int, left, mid, right int) {
// 	n1 := mid - left + 1
// 	n2 := right - mid

// 	L := make([]int, n1)
// 	R := make([]int, n2)

// 	for i := 0; i < n1; i++ {
// 		L[i] = arr[left+i]
// 	}
// 	for j := 0; j < n2; j++ {
// 		R[j] = arr[mid+1+j]
// 	}

// 	i, j, k := 0, 0, left
// 	for i < n1 && j < n2 {
// 		if L[i] <= R[j] {
// 			arr[k] = L[i]
// 			i++
// 		} else {
// 			arr[k] = R[j]
// 			j++
// 		}
// 		k++
// 	}

// 	for i < n1 {
// 		arr[k] = L[i]
// 		i++
// 		k++
// 	}

// 	for j < n2 {
// 		arr[k] = R[j]
// 		j++
// 		k++
// 	}
// }

// func mergeSort(arr []int, left, right int) {
// 	if left < right {
// 		mid := (left + right) / 2
// 		mergeSort(arr, left, mid)
// 		mergeSort(arr, mid+1, right)
// 		merge(arr, left, mid, right)
// 	}
// }

// func mergeSortWrapper(array []int) []int {
// 	mergeSort(array, 0, len(array)-1)
// 	return array
// }

// // Quick Sort Implementation
// func partition(arr []int, low, high int) int {
// 	pivot := arr[high]
// 	i := low - 1
// 	for j := low; j < high; j++ {
// 		if arr[j] < pivot {
// 			i++
// 			swap(arr, i, j)
// 		}
// 	}
// 	swap(arr, i+1, high)
// 	return i + 1
// }

// func quickSort(arr []int, low, high int) {
// 	if low < high {
// 		pi := partition(arr, low, high)
// 		quickSort(arr, low, pi-1)
// 		quickSort(arr, pi+1, high)
// 	}
// }

// func quickSortWrapper(array []int) []int {
// 	quickSort(array, 0, len(array)-1)
// 	return array
// }

// // Test function to run all sorting algorithms
// func test() {
// 	// Generate reverse-ordered array
// 	x := make([]int, 5000)
// 	for i := 0; i < 5000; i++ {
// 		x[i] = 500 - i
// 	}

// 	// Initialize sorting jobs
// 	var jobs []struct {
// 		algo int
// 		data []int
// 	}
// 	for i := 0; i < 500; i++ {
// 		jobs = append(jobs, struct {
// 			algo int
// 			data []int
// 		}{algo: 0, data: append([]int(nil), x...)})
// 		jobs = append(jobs, struct {
// 			algo int
// 			data []int
// 		}{algo: 1, data: append([]int(nil), x...)})
// 		jobs = append(jobs, struct {
// 			algo int
// 			data []int
// 		}{algo: 2, data: append([]int(nil), x...)})
// 	}

// 	// Measure execution time
// 	start := time.Now()
// 	for _, job := range jobs {
// 		switch job.algo {
// 		case 0:
// 			bubbleSort(job.data)
// 		case 1:
// 			mergeSortWrapper(job.data)
// 		case 2:
// 			quickSortWrapper(job.data)
// 		default:
// 			continue
// 		}
// 	}
// 	elapsed := time.Since(start)
// 	fmt.Printf("Total time: %v\n", elapsed)
// }

// func main() {
// 	runtime.GOMAXPROCS(runtime.NumCPU())
// 	Decorator(test)
// }
