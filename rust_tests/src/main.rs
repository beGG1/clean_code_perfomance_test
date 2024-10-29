use std::{time::Instant};

// Trait for shape with an area method
trait Shape {
    fn area(&self) -> f64;
}

// Implementing Square struct and Shape trait for it
struct Square {
    side: f64,
}

impl Shape for Square {
    fn area(&self) -> f64 {
        self.side * self.side
    }
}

// Implementing Rectangle struct and Shape trait for it
struct Rectangle {
    width: f64,
    height: f64,
}

impl Shape for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }
}

// Implementing Triangle struct and Shape trait for it
struct Triangle {
    base: f64,
    height: f64,
}

impl Shape for Triangle {
    fn area(&self) -> f64 {
        0.5 * self.base * self.height
    }
}

// Implementing Circle struct and Shape trait for it
struct Circle {
    radius: f64,
}

impl Shape for Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * self.radius * self.radius
    }
}

// Calculates the total area of shapes in a vector
// fn total_area(shapes: &[&dyn Shape]) -> f64 {
//     shapes.iter().map(|shape| shape.area()).sum()
// }

// Optimized total_area function using four accumulators
fn total_area_vtbl4(shapes: &[&dyn Shape], a: usize) -> f64 {
    let mut accum0 = 0.0;
    let mut accum1 = 0.0;
    let mut accum2 = 0.0;
    let mut accum3 = 0.0;

    let count = a / 4;
    for _ in 0..count {
        accum0 += shapes[0].area();
        accum1 += shapes[1].area();
        accum2 += shapes[2].area();
        accum3 += shapes[3].area();
    }
    accum0 + accum1 + accum2 + accum3
}

// Timing function for measuring execution time, similar to a decorator
fn measure_time<F, R>(func: F) -> R
where
    F: FnOnce() -> R,
{
    let start = Instant::now();
    let result = func();
    let duration = start.elapsed();
    println!("Execution time: {:?}", duration);
    result
}

fn main() {
    // Create shapes and store them in a vector of trait objects
    let shapes: Vec<&dyn Shape> = vec![
        &Square { side: 2.0 },
        &Rectangle { width: 3.0, height: 4.0 },
        &Triangle { base: 3.0, height: 4.0 },
        &Circle { radius: 5.0 },
    ];

    // Measure total_area_vtbl4 with timing
    measure_time(|| {
        let total = total_area_vtbl4(&shapes, 1000000000_usize);
        println!("Total Area VTBL4: {}", total);
    });
}
