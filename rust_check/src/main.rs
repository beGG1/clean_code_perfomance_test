use std::time::Instant;

// Enum for shape types
enum ShapeType {
    Circle,
    Rectangle,
    Triangle,
}

// Struct for shapes used in the match approach
struct Shape {
    shape_type: ShapeType,
    dimension1: f64,
    dimension2: f64,
}

// Function to calculate area using match
fn calculate_area_match(shape: &Shape) -> f64 {
    match shape.shape_type {
        ShapeType::Circle => std::f64::consts::PI * shape.dimension1 * shape.dimension1,
        ShapeType::Rectangle => shape.dimension1 * shape.dimension2,
        ShapeType::Triangle => 0.5 * shape.dimension1 * shape.dimension2,
    }
}

// Test function for match
fn test_match() {
    let shapes = vec![
        Shape {
            shape_type: ShapeType::Circle,
            dimension1: 10.0,
            dimension2: 0.0,
        },
        Shape {
            shape_type: ShapeType::Rectangle,
            dimension1: 5.0,
            dimension2: 10.0,
        },
        Shape {
            shape_type: ShapeType::Triangle,
            dimension1: 6.0,
            dimension2: 8.0,
        },
    ];

    let mut total_area = 0.0;
    for _ in 0..10_000_000 {  // Large number of iterations
        for shape in &shapes {
            total_area += calculate_area_match(shape);
        }
    }
    println!("Total Area (Match): {}", total_area);
}

// Trait for polymorphism
trait ShapeTrait {
    fn calculate_area(&self) -> f64;
}

// Circle struct
struct Circle {
    radius: f64,
}

impl ShapeTrait for Circle {
    fn calculate_area(&self) -> f64 {
        std::f64::consts::PI * self.radius * self.radius
    }
}

// Rectangle struct
struct Rectangle {
    length: f64,
    width: f64,
}

impl ShapeTrait for Rectangle {
    fn calculate_area(&self) -> f64 {
        self.length * self.width
    }
}

// Triangle struct
struct Triangle {
    base: f64,
    height: f64,
}

impl ShapeTrait for Triangle {
    fn calculate_area(&self) -> f64 {
        0.5 * self.base * self.height
    }
}

// Test function for polymorphism
fn test_polymorphism() {
    let shapes: Vec<Box<dyn ShapeTrait>> = vec![
        Box::new(Circle { radius: 10.0 }),
        Box::new(Rectangle { length: 5.0, width: 10.0 }),
        Box::new(Triangle { base: 6.0, height: 8.0 }),
    ];

    let mut total_area = 0.0;
    for _ in 0..10_000_000 {  // Large number of iterations
        for shape in &shapes {
            total_area += shape.calculate_area();
        }
    }
    println!("Total Area (Polymorphism): {}", total_area);
}

// Function to measure performance
fn measure_perf<F: FnOnce()>(test_name: &str, func: F) {
    let start = Instant::now();
    func();
    let duration = start.elapsed();
    println!("{} Elapsed Time: {:?}", test_name, duration);
}

fn main() {
    println!("Testing Match:");
    measure_perf("Match", test_match);

    println!("Testing Polymorphism:");
    measure_perf("Polymorphism", test_polymorphism);
}