package main

// import (
//     "fmt"
//     "math"
//     "time"
// )

// // ShapeType is an enum for shape types
// type ShapeType int

// const (
//     CIRCLE ShapeType = iota
//     RECTANGLE
//     TRIANGLE
// )

// // ShapeStruct is a struct for shapes used in the switch/case approach
// type ShapeStruct struct {
//     Type       ShapeType
//     Dimension1 float64
//     Dimension2 float64
// }

// // calculateAreaSwitchCase calculates area using switch/case
// func calculateAreaSwitchCase(shape ShapeStruct) float64 {
//     switch shape.Type {
//     case CIRCLE:
//         return math.Pi * shape.Dimension1 * shape.Dimension1
//     case RECTANGLE:
//         return shape.Dimension1 * shape.Dimension2
//     case TRIANGLE:
//         return 0.5 * shape.Dimension1 * shape.Dimension2
//     default:
//         return 0.0
//     }
// }

// // testSwitchCase is a function to test switch/case approach
// func testSwitchCase() {
//     shapes := []ShapeStruct{
//         {CIRCLE, 10.0, 0.0},
//         {RECTANGLE, 5.0, 10.0},
//         {TRIANGLE, 6.0, 8.0},
//     }

//     totalArea := 0.0
//     for i := 0; i < 10000000; i++ {
//         for _, shape := range shapes {
//             totalArea += calculateAreaSwitchCase(shape)
//         }
//     }
//     fmt.Println("Total Area (Switch/Case):", totalArea)
// }

// // Shape interface for polymorphism
// type Shape interface {
//     CalculateArea() float64
// }

// // Circle struct
// type Circle struct {
//     Radius float64
// }

// // CalculateArea calculates the area of a circle
// func (c Circle) CalculateArea() float64 {
//     return math.Pi * c.Radius * c.Radius
// }

// // Rectangle struct
// type Rectangle struct {
//     Length float64
//     Width  float64
// }

// // CalculateArea calculates the area of a rectangle
// func (r Rectangle) CalculateArea() float64 {
//     return r.Length * r.Width
// }

// // Triangle struct
// type Triangle struct {
//     Base   float64
//     Height float64
// }

// // CalculateArea calculates the area of a triangle
// func (t Triangle) CalculateArea() float64 {
//     return 0.5 * t.Base * t.Height
// }

// // testPolymorphism is a function to test polymorphism approach
// func testPolymorphism() {
//     shapes := []Shape{
//         Circle{10.0},
//         Rectangle{5.0, 10.0},
//         Triangle{6.0, 8.0},
//     }

//     totalArea := 0.0
//     for i := 0; i < 10000000; i++ {
//         for _, shape := range shapes {
//             totalArea += shape.CalculateArea()
//         }
//     }
//     fmt.Println("Total Area (Polymorphism):", totalArea)
// }

// // measurePerf measures the performance of a function
// func measurePerf(testName string, f func()) {
//     start := time.Now()
//     f()
//     elapsed := time.Since(start)
//     fmt.Printf("%s Elapsed Time: %s\n", testName, elapsed)
// }

// func main() {
//     fmt.Println("Testing Switch/Case:")
//     measurePerf("Switch/Case", testSwitchCase)

//     fmt.Println("Testing Polymorphism:")
//     measurePerf("Polymorphism", testPolymorphism)
// }