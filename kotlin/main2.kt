import kotlin.math.PI
import kotlin.system.measureTimeMillis

// Enum class for shape types
enum class ShapeType {
    CIRCLE, RECTANGLE, TRIANGLE
}

// Data class for shapes used in the when approach
data class Shape(val type: ShapeType, val dimension1: Double, val dimension2: Double)

// Function to calculate area using when
fun calculateAreaWhen(shape: Shape): Double {
    return when (shape.type) {
        ShapeType.CIRCLE -> PI * shape.dimension1 * shape.dimension1
        ShapeType.RECTANGLE -> shape.dimension1 * shape.dimension2
        ShapeType.TRIANGLE -> 0.5 * shape.dimension1 * shape.dimension2
    }
}

// Test function for when
fun testWhen() {
    val shapes = listOf(
        Shape(ShapeType.CIRCLE, 10.0, 0.0),
        Shape(ShapeType.RECTANGLE, 5.0, 10.0),
        Shape(ShapeType.TRIANGLE, 6.0, 8.0)
    )

    var totalArea = 0.0
    repeat(10_000_000) {  // Large number of iterations
        for (shape in shapes) {
            totalArea += calculateAreaWhen(shape)
        }
    }
    println("Total Area (When): $totalArea")
}

// Interface for polymorphism
interface ShapeInterface {
    fun calculateArea(): Double
}

// Circle class
class Circle(private val radius: Double) : ShapeInterface {
    override fun calculateArea(): Double {
        return PI * radius * radius
    }
}

// Rectangle class
class Rectangle(private val length: Double, private val width: Double) : ShapeInterface {
    override fun calculateArea(): Double {
        return length * width
    }
}

// Triangle class
class Triangle(private val base: Double, private val height: Double) : ShapeInterface {
    override fun calculateArea(): Double {
        return 0.5 * base * height
    }
}

// Test function for polymorphism
fun testPolymorphism() {
    val shapes: List<ShapeInterface> = listOf(
        Circle(10.0),
        Rectangle(5.0, 10.0),
        Triangle(6.0, 8.0)
    )

    var totalArea = 0.0
    repeat(10_000_000) {  // Large number of iterations
        for (shape in shapes) {
            totalArea += shape.calculateArea()
        }
    }
    println("Total Area (Polymorphism): $totalArea")
}

// Function to measure performance
fun measurePerf(testName: String, func: () -> Unit) {
    val timeMillis = measureTimeMillis {
        func()
    }
    println("$testName Elapsed Time: ${timeMillis / 1000.0} seconds")
}

fun main() {
    println("Testing When:")
    measurePerf("When", ::testWhen)

    println("Testing Polymorphism:")
    measurePerf("Polymorphism", ::testPolymorphism)
}