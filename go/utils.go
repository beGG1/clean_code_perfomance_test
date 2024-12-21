package main

import (
	"fmt"
	"os"
	"runtime"
	"strings"
	"sync"
	"time"

	"github.com/shirou/gopsutil/v3/process"
)

func memoryUsage(fn func(), samplingInterval time.Duration) {
	var memStats runtime.MemStats
	var memorySamples []uint64

	// Goroutine to sample memory usage
	var sampling = true
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		for sampling {
			runtime.ReadMemStats(&memStats)
			memorySamples = append(memorySamples, memStats.Alloc/(1024*1024)) // Memory in MB
			time.Sleep(samplingInterval)
		}
	}()

	// Execute the target function
	start := time.Now()
	fn()
	elapsed := time.Since(start)

	// Stop sampling
	sampling = false
	wg.Wait()

	// Calculate memory stats
	var totalMemory, peakMemory uint64
	for _, sample := range memorySamples {
		totalMemory += sample
		if sample > peakMemory {
			peakMemory = sample
		}
	}

	avgMemory := float64(totalMemory) / float64(len(memorySamples))

	fmt.Printf("Elapsed Time: %v\n", elapsed)
	fmt.Printf("Average Memory Usage: %.2f MB\n", avgMemory)
	fmt.Printf("Peak Memory Usage: %d MB\n", peakMemory)
}

func measureCPU(fn func()) (float64, float64) {
	pid := int32(os.Getpid())
	proc, err := process.NewProcess(pid)
	if err != nil {
		panic(err)
	}

	var wg sync.WaitGroup
	var cpuSamples []float64
	sampling := true

	wg.Add(1)
	go func() {
		defer wg.Done()
		for sampling {
			cpuPercent, err := proc.CPUPercent()
			if err == nil {
				cpuSamples = append(cpuSamples, cpuPercent)
			}
			time.Sleep(100 * time.Millisecond) // Adjust sampling interval as needed
		}
	}()

	// Execute the target function
	start := time.Now()
	fn()
	elapsed := time.Since(start)

	// Stop sampling
	sampling = false
	wg.Wait()

	// Calculate CPU stats
	var totalCPU, peakCPU float64
	for _, sample := range cpuSamples {
		totalCPU += sample
		if sample > peakCPU {
			peakCPU = sample
		}
	}

	avgCPU := totalCPU / float64(len(cpuSamples))

	fmt.Printf("Elapsed Time: %v\n", elapsed)
	fmt.Printf("Average CPU Usage: %.2f%%\n", avgCPU)
	fmt.Printf("Peak CPU Usage: %.2f%%\n", peakCPU)

	return avgCPU, peakCPU
}

func Decorator(fn func()) {
	start := time.Now()
	fn()
	elapsed := time.Since(start)
	fmt.Printf("Total time: %v\n", elapsed)
	fmt.Println(strings.Repeat("_", 50))

	// Memory usage
	memoryUsage(fn, 10*time.Millisecond)
	fmt.Println(strings.Repeat("_", 50))

	// CPU usage
	measureCPU(fn)
}
