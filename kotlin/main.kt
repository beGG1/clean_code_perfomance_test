import java.lang.management.ManagementFactory
import java.lang.management.OperatingSystemMXBean
import kotlin.system.measureNanoTime

abstract class SortAlgorithm {
    abstract fun sort(arr: IntArray)
}

class BubbleSort : SortAlgorithm() {
    override fun sort(arr: IntArray) {
        val n = arr.size
        for (i in 0 until n - 1) {
            for (j in 0 until n - i - 1) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1)
                }
            }
        }
    }

    private fun swap(arr: IntArray, i: Int, j: Int) {
        val temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    }
}

class MergeSort : SortAlgorithm() {
    override fun sort(arr: IntArray) {
        if (arr.size > 1) {
            val mid = arr.size / 2
            val left = arr.sliceArray(0 until mid)
            val right = arr.sliceArray(mid until arr.size)

            sort(left)
            sort(right)
            merge(arr, left, right)
        }
    }

    private fun merge(arr: IntArray, left: IntArray, right: IntArray) {
        var i = 0
        var j = 0
        var k = 0

        while (i < left.size && j < right.size) {
            if (left[i] <= right[j]) {
                arr[k] = left[i]
                i++
            } else {
                arr[k] = right[j]
                j++
            }
            k++
        }

        while (i < left.size) {
            arr[k] = left[i]
            i++
            k++
        }

        while (j < right.size) {
            arr[k] = right[j]
            j++
            k++
        }
    }
}

class QuickSort : SortAlgorithm() {
    override fun sort(arr: IntArray) {
        quickSort(arr, 0, arr.size - 1)
    }

    private fun quickSort(arr: IntArray, low: Int, high: Int) {
        if (low < high) {
            val pi = partition(arr, low, high)
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)
        }
    }

    private fun partition(arr: IntArray, low: Int, high: Int): Int {
        val pivot = arr[high]
        var i = low - 1
        for (j in low until high) {
            if (arr[j] < pivot) {
                i++
                swap(arr, i, j)
            }
        }
        swap(arr, i + 1, high)
        return i + 1
    }

    private fun swap(arr: IntArray, i: Int, j: Int) {
        val temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    }
}

fun bubbleSort(arr: IntArray) {
    val n = arr.size
    for (i in 0 until n - 1) {
        for (j in 0 until n - i - 1) {
            if (arr[j] > arr[j + 1]) {
                val temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
}

fun mergeSort(arr: IntArray) {
    if (arr.size > 1) {
        val mid = arr.size / 2
        val left = arr.sliceArray(0 until mid)
        val right = arr.sliceArray(mid until arr.size)

        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)
    }
}

fun merge(arr: IntArray, left: IntArray, right: IntArray) {
    var i = 0
    var j = 0
    var k = 0

    while (i < left.size && j < right.size) {
        if (left[i] <= right[j]) {
            arr[k] = left[i]
            i++
        } else {
            arr[k] = right[j]
            j++
        }
        k++
    }

    while (i < left.size) {
        arr[k] = left[i]
        i++
        k++
    }

    while (j < right.size) {
        arr[k] = right[j]
        j++
        k++
    }
}

fun quickSort(arr: IntArray, low: Int = 0, high: Int = arr.size - 1) {
    if (low < high) {
        val pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    }
}

fun partition(arr: IntArray, low: Int, high: Int): Int {
    val pivot = arr[high]
    var i = low - 1
    for (j in low until high) {
        if (arr[j] < pivot) {
            i++
            val temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        }
    }
    val temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    return i + 1
}

enum class SortType {
    BUBBLE, MERGE, QUICK
}

fun sortArray(arr: IntArray, sortType: SortType) {
    when (sortType) {
        SortType.BUBBLE -> bubbleSort(arr)
        SortType.MERGE -> mergeSort(arr)
        SortType.QUICK -> quickSort(arr)
    }
}

fun sortArraySwitch(arr: IntArray, sortType: String) {
    when (sortType) {
        "BUBBLE" -> bubbleSort(arr)
        "MERGE" -> mergeSort(arr)
        "QUICK" -> quickSort(arr)
    }
}




fun measurePerformance(func: () -> Unit) {
    val runtime = Runtime.getRuntime()
    val osBean = ManagementFactory.getOperatingSystemMXBean() as com.sun.management.OperatingSystemMXBean

    // Measure execution time
    val executionTime = measureNanoTime {
        func()
    }

    // Measure memory usage
    val memorySamples = mutableListOf<Long>()
    val samplingInterval = 100L // in milliseconds
    var sampling = true

    val samplingThread = Thread {
        while (sampling) {
            val usedMemory = runtime.totalMemory() - runtime.freeMemory()
            memorySamples.add(usedMemory)
            Thread.sleep(samplingInterval)
        }
    }

    // Start sampling
    samplingThread.start()

    // Execute the target function
    func()

    // Stop sampling
    sampling = false
    samplingThread.join()

    // Calculate average and peak memory usage
    val avgMemory = memorySamples.average() / (1024 * 1024) // Convert to MB
    val peakMemory = memorySamples.maxOrNull()?.toDouble()?.div(1024 * 1024) ?: 0.0 // Convert to MB

    // Measure CPU usage
    val cpuLoad = osBean.processCpuLoad * 100

    // Print results
    println("Execution Time: ${executionTime / 1_000_000} ms")
    println("Average Memory Usage: %.2f MB".format(avgMemory))
    println("Peak Memory Usage: %.2f MB".format(peakMemory))
    println("Average CPU Usage: %.2f%%".format(cpuLoad))
}

fun testWithClasses() {
    val bubbleSort = BubbleSort()
    val mergeSort = MergeSort()
    val quickSort = QuickSort()

    repeat(300) {
        val array = IntArray(5000) { 500 - it }
        bubbleSort.sort(array)
    }

    repeat(300) {
        val array = IntArray(5000) { 500 - it }
        mergeSort.sort(array)
    }

    repeat(300) {
        val array = IntArray(5000) { 500 - it }
        quickSort.sort(array)
    }
}

fun testWithEnums() {
    repeat(300) {
        val array = IntArray(5000) { 500 - it }
        sortArray(array, SortType.BUBBLE)
    }

    repeat(300) {
        val array = IntArray(5000) { 500 - it }
        sortArray(array, SortType.MERGE)
    }

    repeat(300) {
        val array = IntArray(5000) { 500 - it }
        sortArray(array, SortType.QUICK)
    }
}

fun testWithSwitchCase() {
    repeat(300) {
        val array = IntArray(5000) { 500 - it }
        sortArraySwitch(array, "BUBBLE")
    }

    repeat(300) {
        val array = IntArray(5000) { 500 - it }
        sortArraySwitch(array, "MERGE")
    }

    repeat(300) {
        val array = IntArray(5000) { 500 - it }
        sortArraySwitch(array, "QUICK")
    }
}

fun main() {
    println("Testing with Classes:")
    measurePerformance { testWithClasses() }

    println("\nTesting with Enums:")
    measurePerformance { testWithEnums() }

    println("\nTesting with Switch Case:")
    measurePerformance { testWithSwitchCase() }
}