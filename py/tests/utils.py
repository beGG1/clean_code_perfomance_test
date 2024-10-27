from time import perf_counter
from hwcounter import Timer

import psutil
import time
import threading
import tracemalloc
import dis

def memory_usage(func, *args, **kwargs):
    # Initialize sampling and memory allocation tracking
    memory_samples = []
    process = psutil.Process()
    
    # Start tracing memory allocations
    tracemalloc.start()
    start_snap = tracemalloc.take_snapshot()

    # Function to sample memory usage at regular intervals
    def sample_memory():
        while sampling[0]:
            memory_samples.append(process.memory_info().rss / (1024 * 1024))  # Memory in MB
            time.sleep(sampling_interval)

    # Start sampling in a separate thread
    sampling_interval = 0.01  # Adjust sampling frequency as needed
    sampling = [True]
    sampling_thread = threading.Thread(target=sample_memory)
    sampling_thread.start()
    
    # Run the target function and record start time
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    # Stop sampling
    sampling[0] = False
    sampling_thread.join()

    # Capture end snapshot and calculate memory stats
    end_snap = tracemalloc.take_snapshot()
    tracemalloc.stop()

    # Calculate average and peak memory usage
    avg_memory_usage = sum(memory_samples) / len(memory_samples) if memory_samples else 0.0
    peak_memory_usage = max(memory_samples) if memory_samples else 0.0

    # Calculate memory allocation frequency
    alloc_stats = end_snap.compare_to(start_snap, 'lineno')
    alloc_count = sum(stat.count for stat in alloc_stats)

    # Output statistics
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")
    print(f"Average Memory Usage: {avg_memory_usage:.2f} MB")
    print(f"Peak Memory Usage: {peak_memory_usage:.2f} MB")
    print(f"Memory Allocation Frequency: {alloc_count} allocations")

    return result

def cpu_usage(func, *args, **kwargs):
    # List to store CPU usage samples
    cpu_samples = []
    process = psutil.Process()

    # Function to sample CPU usage at regular intervals
    def sample_cpu():
        while sampling[0]:
            # Record the CPU usage (percentage of single CPU core usage)
            cpu_samples.append(process.cpu_percent(interval=None))
            time.sleep(sampling_interval)  # wait before next sample

    # Start sampling in a separate thread
    sampling_interval = 0.01  # Adjust for more or less frequent sampling
    sampling = [True]
    sampling_thread = threading.Thread(target=sample_cpu)
    sampling_thread.start()
    
    # Start timing and execute the function
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    # Stop sampling
    sampling[0] = False
    sampling_thread.join()

    # Calculate statistics
    if cpu_samples:
        avg_cpu_usage = sum(cpu_samples) / len(cpu_samples)
        peak_cpu_usage = max(cpu_samples)
    else:
        avg_cpu_usage = peak_cpu_usage = 0.0

    # Elapsed time
    elapsed_time = end_time - start_time

    print(f"Elapsed Time: {elapsed_time:.6f} seconds")
    print(f"Average CPU Usage: {avg_cpu_usage:.2f}%")
    print(f"Peak CPU Usage: {peak_cpu_usage:.2f}%")
    
    return result

def assembly(func, *args, **kwargs):
    dis.dis(func)

def decorator(func):
    def wrapper(*args, **kwargs):
        # Perf counter
        start = perf_counter()
        result = func(*args, **kwargs)
        stop = perf_counter()
        
        print("Total time: ", stop-start)
        
        print("_" * 50)
        # hwcounter
        with Timer() as t:
            result2 = func(*args, **kwargs)
        
        print(f'Elapsed cycles: {t.cycles:,}')
        print("_" * 50)
        
        memory_usage(func, *args, **kwargs)
        print("_" * 50)
        cpu_usage(func, *args, **kwargs)
        print("_" * 50)
        assembly(func, *args, **kwargs)
        
    return wrapper