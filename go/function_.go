package main

// import (
// 	"fmt"
// 	"math/rand"
// 	"time"
// )

// // Quicksort algorithm implemented as one big function
// func quicksortBig(arr []int, low, high int) {
// 	if low < high {
// 		pivot := arr[high] // Pivot element
// 		i := low - 1

// 		// Partitioning the array
// 		for j := low; j <= high-1; j++ {
// 			if arr[j] < pivot {
// 				i++
// 				arr[i], arr[j] = arr[j], arr[i]
// 			}
// 		}
// 		arr[i+1], arr[high] = arr[high], arr[i+1]
// 		pi := i + 1

// 		// Recursively sort elements before and after partition
// 		quicksortBig(arr, low, pi-1)
// 		quicksortBig(arr, pi+1, high)
// 	}
// }

// // Function to partition the array
// func partition(arr []int, low, high int) int {
// 	pivot := arr[high] // Pivot element
// 	i := low - 1

// 	for j := low; j <= high-1; j++ {
// 		if arr[j] < pivot {
// 			i++
// 			arr[i], arr[j] = arr[j], arr[i]
// 		}
// 	}
// 	arr[i+1], arr[high] = arr[high], arr[i+1]
// 	return i + 1
// }

// // Quicksort function that uses the partition function
// func quicksortSmall(arr []int, low, high int) {
// 	if low < high {
// 		pi := partition(arr, low, high)

// 		quicksortSmall(arr, low, pi-1)
// 		quicksortSmall(arr, pi+1, high)
// 	}
// }

// // Helper function to generate a random slice of a given size
// func generateRandomSlice(size int) []int {
// 	slice := make([]int, size)
// 	for i := range slice {
// 		slice[i] = rand.Intn(10000) // Random number between 0 and 9999
// 	}
// 	return slice
// }

// func main() {
// 	// Generate a random slice for testing
// 	arr := generateRandomSlice(10000000)

// 	// Measure the execution time of the big function
// 	arrBig := make([]int, len(arr))
// 	copy(arrBig, arr)
// 	startBig := time.Now()
// 	quicksortBig(arrBig, 0, len(arrBig)-1)
// 	durationBig := time.Since(startBig)
// 	fmt.Printf("Execution time of big function: %v seconds\n", durationBig.Seconds())

// 	// Measure the execution time of the small functions
// 	arrSmall := make([]int, len(arr))
// 	copy(arrSmall, arr)
// 	startSmall := time.Now()
// 	quicksortSmall(arrSmall, 0, len(arrSmall)-1)
// 	durationSmall := time.Since(startSmall)
// 	fmt.Printf("Execution time of small functions: %v seconds\n", durationSmall.Seconds())
// }
