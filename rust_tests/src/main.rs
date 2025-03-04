pub mod clean_code;
pub mod switch_sort_enum;
pub mod switch_sort_without_enums;

use std::time::Instant;
use sysinfo::{ProcessExt, System, SystemExt};
use std::{thread, time::Duration};

// Define a struct to hold statistics functions
struct Stats;

impl Stats {
    fn measure_time<F, R>(func: F) -> (R, f64)
    where
        F: FnOnce() -> R,
    {
        let start = Instant::now();
        let result = func();
        let duration = start.elapsed().as_secs_f64();
        println!("Elapsed Time: {:.6} seconds", duration);
        (result, duration)
    }

    fn measure_memory<F>(func: F) -> f64
where
    F: FnOnce(),
{
    let process_pid = sysinfo::get_current_pid().unwrap();

    let memory_samples = std::sync::Arc::new(std::sync::Mutex::new(Vec::new()));
    let sampling = std::sync::Arc::new(std::sync::atomic::AtomicBool::new(true));

    let memory_samples_clone = std::sync::Arc::clone(&memory_samples);
    let sampling_clone = std::sync::Arc::clone(&sampling);

    let sampling_thread = thread::spawn(move || {
        let mut system = System::new_all();
        while sampling_clone.load(std::sync::atomic::Ordering::Relaxed) {
            system.refresh_process(process_pid);
            if let Some(process) = system.process(process_pid) {
                let memory = process.memory() as f64 / 1024.0; // Memory in Kb
                memory_samples_clone.lock().unwrap().push(memory);
            }
            thread::sleep(Duration::from_millis(1)); // Adjust sampling interval as needed
        }
    });

    // Execute the target function
    func();

    // Stop sampling
    sampling.store(false, std::sync::atomic::Ordering::Relaxed);
    sampling_thread.join().unwrap();

    // Calculate average and max memory usage
    let memory_samples = memory_samples.lock().unwrap();
    let avg_memory = memory_samples.iter().sum::<f64>() / memory_samples.len() as f64;

    println!("Average Memory Usage: {:.2} MB", avg_memory / 1024.0);
    avg_memory as f64
}
    

    fn measure_cpu<F, R>(func: F) -> R
    where
        F: FnOnce() -> R,
    {
        let mut sys = System::new_all();

        // Refresh system state before accessing CPU usage
        sys.refresh_processes();
        let pid = sysinfo::Pid::from(std::process::id() as usize);
        let process = sys.process(pid).expect("Process not found");

        // Record CPU usage before running the function
        let cpu_before = process.cpu_usage();
        
        // Run the function
        let result = func();

        // Now that the function has finished, refresh system state again to get updated CPU info
        sys.refresh_processes(); 
        let process = sys.process(pid).expect("Process not found");

        // Record CPU usage after
        let cpu_after = process.cpu_usage();

        // Print CPU usage before and after
        println!("CPU Usage Before: {:.2}%", cpu_before);
        println!("CPU Usage After: {:.2}%", cpu_after);

        result
    }
}

// Trait for shape with an area method
// trait Shape {
//     fn area(&self) -> f64;
// }

// // Implementing Square struct and Shape trait for it
// struct Square {
//     side: f64,
// }

// impl Shape for Square {
//     fn area(&self) -> f64 {
//         self.side * self.side
//     }
// }

// // Implementing Rectangle struct and Shape trait for it
// struct Rectangle {
//     width: f64,
//     height: f64,
// }

// impl Shape for Rectangle {
//     fn area(&self) -> f64 {
//         self.width * self.height
//     }
// }

// // Implementing Triangle struct and Shape trait for it
// struct Triangle {
//     base: f64,
//     height: f64,
// }

// impl Shape for Triangle {
//     fn area(&self) -> f64 {
//         0.5 * self.base * self.height
//     }
// }

// // Implementing Circle struct and Shape trait for it
// struct Circle {
//     radius: f64,
// }

// impl Shape for Circle {
//     fn area(&self) -> f64 {
//         std::f64::consts::PI * self.radius * self.radius
//     }
// }

// // Calculates the total area of shapes in a vector
// // fn total_area(shapes: &[&dyn Shape]) -> f64 {
// //     shapes.iter().map(|shape| shape.area()).sum()
// // }

// // Optimized total_area function using four accumulators
// fn total_area_vtbl4(shapes: &[&dyn Shape], a: usize) -> f64 {
//     let mut accum0 = 0.0;
//     let mut accum1 = 0.0;
//     let mut accum2 = 0.0;
//     let mut accum3 = 0.0;

//     let count = a / 4;
//     for _ in 0..count {
//         accum0 += shapes[0].area();
//         accum1 += shapes[1].area();
//         accum2 += shapes[2].area();
//         accum3 += shapes[3].area();
//     }
//     accum0 + accum1 + accum2 + accum3
// }

// Timing function for measuring execution time, similar to a decorator
// fn measure_time<F, R>(func: F) -> R
// where
//     F: FnOnce() -> R,
// {
//     let start = Instant::now();
//     let result = func();
//     let duration = start.elapsed();
//     println!("Execution time: {:?}", duration);
//     result
// }

fn main() {
    // Create shapes and store them in a vector of trait objects
    // let shapes: Vec<&dyn Shape> = vec![
    //     &Square { side: 2.0 },
    //     &Rectangle { width: 3.0, height: 4.0 },
    //     &Triangle { base: 3.0, height: 4.0 },
    //     &Circle { radius: 5.0 },
    // ];

    // Measure total_area_vtbl4 with timing
    // measure_time(|| {
    //     let total = total_area_vtbl4(&shapes, 1000000000_usize);
    //     println!("Total Area VTBL4: {}", total);
    // });

    // measure_time(|| {
    //     switch_sort_enum::test();
    // });
    // measure_time(|| {
    //     switch_sort_without_enums::test();
    // });

    // let (_result, _time) = Stats::measure_time(|| example_function());

    println!("Clean Code-------------------------------");

    let (_result, _time) = Stats::measure_time(|| clean_code::test());

    // measure_time(|| {
    //     clean_code::test();
    // });

    Stats::measure_cpu(|| clean_code::test());

    // Measure memory usage
    Stats::measure_memory(|| clean_code::test());

    println!("-------------------------------");
    println!("Switch Enums-------------------------------");

    let (_result, _time) = Stats::measure_time(|| switch_sort_enum::test());

    // measure_time(|| {
    //     clean_code::test();
    // });

    Stats::measure_cpu(|| switch_sort_enum::test());

    // Measure memory usage
    Stats::measure_memory(|| switch_sort_enum::test());

    println!("-------------------------------");
    println!("Switch without enums-------------------------------");

    let (_result, _time) = Stats::measure_time(|| switch_sort_without_enums::test());

    // measure_time(|| {
    //     clean_code::test();
    // });

    Stats::measure_cpu(|| switch_sort_without_enums::test());

    // Measure memory usage
    Stats::measure_memory(|| switch_sort_without_enums::test());

    println!("-------------------------------");

}
