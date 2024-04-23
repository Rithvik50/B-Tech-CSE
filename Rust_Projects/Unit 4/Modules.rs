// Define a module named `geometry`
mod geometry {
    const PI: f64 = 3.14159;

    // Function to calculate the area of a circle
    pub fn circle_area(radius: f64) -> f64 {
        PI * radius * radius
    }

    // Function to calculate the area of a rectangle
    pub fn rectangle_area(length: f64, width: f64) -> f64 {
        length * width
    }
}

fn main() {
    let radius = 9.0;
    let circle_area = geometry::circle_area(radius);
    println!("Area of circle with radius {}: {}", radius, circle_area);

    let length = 2.0;
    let width = 10.0;
    let rectangle_area = geometry::rectangle_area(length, width);
    println!("Area of rectangle with length {} and width {}: {}", length, width, rectangle_area);
}

/*
Modules are used to group parts of code together
You can put functions in modules and they can either be private(default) or public for outside use(put pub fn funcname())
*/