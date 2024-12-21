package main

// // AbstractSort defines the interface for all sorting algorithms
// type AbstractSort interface {
// 	Sort() []int
// }

// // BubbleSort implements the AbstractSort interface
// type BubbleSort struct {
// 	array []int
// }

// func (b *BubbleSort) Sort() []int {
// 	arr := b.array
// 	n := len(arr)
// 	for swapped := true; swapped; {
// 		swapped = false
// 		for i := 1; i < n; i++ {
// 			if arr[i-1] > arr[i] {
// 				arr[i-1], arr[i] = arr[i], arr[i-1]
// 				swapped = true
// 			}
// 		}
// 	}
// 	return arr
// }

// // MergeSort implements the AbstractSort interface
// type MergeSort struct {
// 	array []int
// }

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

// func (m *MergeSort) mergeSort(arr []int, left, right int) {
// 	if left < right {
// 		mid := (left + right) / 2
// 		m.mergeSort(arr, left, mid)
// 		m.mergeSort(arr, mid+1, right)
// 		merge(arr, left, mid, right)
// 	}
// }

// func (m *MergeSort) Sort() []int {
// 	m.mergeSort(m.array, 0, len(m.array)-1)
// 	return m.array
// }

// // QuickSort implements the AbstractSort interface
// type QuickSort struct {
// 	array []int
// }

// func partition(arr []int, low, high int) int {
// 	pivot := arr[high]
// 	i := low - 1
// 	for j := low; j < high; j++ {
// 		if arr[j] < pivot {
// 			i++
// 			arr[i], arr[j] = arr[j], arr[i]
// 		}
// 	}
// 	arr[i+1], arr[high] = arr[high], arr[i+1]
// 	return i + 1
// }

// func (q *QuickSort) quickSort(arr []int, low, high int) {
// 	if low < high {
// 		pi := partition(arr, low, high)
// 		q.quickSort(arr, low, pi-1)
// 		q.quickSort(arr, pi+1, high)
// 	}
// }

// func (q *QuickSort) Sort() []int {
// 	q.quickSort(q.array, 0, len(q.array)-1)
// 	return q.array
// }

// // Test function to run and evaluate the sorters
// func test() {
// 	x := make([]int, 5000)
// 	for i := 0; i < 5000; i++ {
// 		x[i] = 500 - i
// 	}

// 	var sorters []AbstractSort
// 	for i := 0; i < 500; i++ {
// 		sorters = append(sorters, &BubbleSort{array: append([]int(nil), x...)})
// 		sorters = append(sorters, &MergeSort{array: append([]int(nil), x...)})
// 		sorters = append(sorters, &QuickSort{array: append([]int(nil), x...)})
// 	}
// 	for _, sorter := range sorters {
// 		sorter.Sort()
// 	}
// }

// func main() {
// 	// runtime.GOMAXPROCS(runtime.NumCPU())
// 	Decorator(test)
// }
