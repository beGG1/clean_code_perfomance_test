#include <iostream>
#include <vector>
#include <chrono>
#include <cmath>

using namespace std;
using namespace std::chrono;

// Enum for shape types
enum ShapeType { CIRCLE, RECTANGLE, TRIANGLE };

// Struct for shapes used in the switch/case approach
struct ShapeStruct {
    ShapeType type;
    double dimension1;
    double dimension2;
};

// Function to calculate area using switch/case
double calculateAreaSwitchCase(const ShapeStruct& shape) {
    switch (shape.type) {
        case CIRCLE:
            return M_PI * shape.dimension1 * shape.dimension1;
        case RECTANGLE:
            return shape.dimension1 * shape.dimension2;
        case TRIANGLE:
            return 0.5 * shape.dimension1 * shape.dimension2;
        default:
            return 0.0;
    }
}

// Test function for switch/case
void testSwitchCase() {
    ShapeStruct shapes[3] = {
        {CIRCLE, 10.0, 0.0},
        {RECTANGLE, 5.0, 10.0},
        {TRIANGLE, 6.0, 8.0}
    };

    double totalArea = 0.0;
    for (int i = 0; i < 100000000; ++i) {  // Large number of iterations
        for (const auto& shape : shapes) {
            totalArea += calculateAreaSwitchCase(shape);
        }
    }
    cout << "Total Area (Switch/Case): " << totalArea << endl;
}

// Abstract Shape class for polymorphism
class Shape {
public:
    virtual ~Shape() = default;
    virtual double calculateArea() const = 0;
};

// Circle class
class Circle : public Shape {
    double radius;
public:
    Circle(double r) : radius(r) {}
    double calculateArea() const override {
        return M_PI * radius * radius;
    }
};

// Rectangle class
class Rectangle : public Shape {
    double length, width;
public:
    Rectangle(double l, double w) : length(l), width(w) {}
    double calculateArea() const override {
        return length * width;
    }
};

// Triangle class
class Triangle : public Shape {
    double base, height;
public:
    Triangle(double b, double h) : base(b), height(h) {}
    double calculateArea() const override {
        return 0.5 * base * height;
    }
};

// Test function for polymorphism
void testPolymorphism() {
    vector<Shape*> shapes = {
        new Circle(10.0),
        new Rectangle(5.0, 10.0),
        new Triangle(6.0, 8.0)
    };

    double totalArea = 0.0;
    for (int i = 0; i < 100000000; ++i) {  // Large number of iterations
        for (const auto& shape : shapes) {
            totalArea += shape->calculateArea();
        }
    }

    for (auto& shape : shapes) {
        delete shape;
    }

    cout << "Total Area (Polymorphism): " << totalArea << endl;
}

// Function to measure performance
template<typename Func, typename... Args>
void measure_perf(const string& test_name, Func func, Args&&... args) {
    auto start = high_resolution_clock::now();
    func(std::forward<Args>(args)...);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    cout << test_name << " Elapsed Time: " << duration.count() << " milliseconds" << endl;
}

int main() {
    cout << "Testing Switch/Case:" << endl;
    measure_perf("Switch/Case", testSwitchCase);

    cout << "Testing Polymorphism:" << endl;
    measure_perf("Polymorphism", testPolymorphism);

    return 0;
}