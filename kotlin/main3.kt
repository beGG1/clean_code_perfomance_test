import kotlin.random.Random
import kotlin.system.measureTimeMillis

// Quicksort algorithm implemented as one big function
fun quicksortBig(arr: IntArray, low: Int, high: Int) {
    if (low < high) {
        val pivot = arr[high] // Pivot element
        var i = low - 1

        // Partitioning the array
        for (j in low until high) {
            if (arr[j] < pivot) {
                i++
                arr[i] = arr[j].also { arr[j] = arr[i] }
            }
        }
        arr[i + 1] = arr[high].also { arr[high] = arr[i + 1] }
        val pi = i + 1

        // Recursively sort elements before and after partition
        quicksortBig(arr, low, pi - 1)
        quicksortBig(arr, pi + 1, high)
    }
}

// Function to partition the array
fun partition(arr: IntArray, low: Int, high: Int): Int {
    val pivot = arr[high] // Pivot element
    var i = low - 1

    for (j in low until high) {
        if (arr[j] < pivot) {
            i++
            arr[i] = arr[j].also { arr[j] = arr[i] }
        }
    }
    arr[i + 1] = arr[high].also { arr[high] = arr[i + 1] }
    return i + 1
}

// Quicksort function that uses the partition function
fun quicksortSmall(arr: IntArray, low: Int, high: Int) {
    if (low < high) {
        val pi = partition(arr, low, high)

        quicksortSmall(arr, low, pi - 1)
        quicksortSmall(arr, pi + 1, high)
    }
}

// Function to generate a random array of a given size
fun generateRandomArray(size: Int): IntArray {
    return IntArray(size) { Random.nextInt(0, 10000) }
}

fun main() {
    // Generate a random array for testing
    val arr = generateRandomArray(10000000)

    // Measure the execution time of the big function
    val arrBig = arr.copyOf()
    val durationBig = measureTimeMillis {
        quicksortBig(arrBig, 0, arrBig.size - 1)
    }
    println("Execution time of big function: $durationBig ms")

    // Measure the execution time of the small functions
    val arrSmall = arr.copyOf()
    val durationSmall = measureTimeMillis {
        quicksortSmall(arrSmall, 0, arrSmall.size - 1)
    }
    println("Execution time of small functions: $durationSmall ms")
}