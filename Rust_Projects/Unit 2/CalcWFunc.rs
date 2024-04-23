use std::io;

// Operation functions
fn add(a: i32, b: i32) -> i32 {
    return a + b;
}
fn subtract(a: i32, b: i32) -> i32 {
    return a - b;
}
fn multiply(a: i32, b: i32) -> i32 {
    return a * b;
}
fn divide(a: i32, b: i32) -> i32 {
    return a / b;
}
fn modulus(a: i32, b: i32) -> i32 {
    return a % b;
}

fn main() {
    // Operand 1
    let mut input1 = String::new();
    println!("Enter first number: ");
    io::stdin().read_line(&mut input1).expect("Failed to read line");
    let a: i32 = match input1.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };

    // Operand 2
    let mut input2 = String::new();
    println!("Enter second number: ");
    io::stdin().read_line(&mut input2).expect("Failed to read line");
    let b: i32 = match input2.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };

    // Operator
    let mut input3 = String::new();
    println!("Enter operation: ");
    io::stdin().read_line(&mut input3).expect("Failed to read line");
    let op: char = match input3.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };

    // Answer
    match op {
        '+' => println!("Sum is {}", add(a, b)),
        '-' => println!("Difference is {}", subtract(a, b)),
        '*' => println!("Product is {}", multiply(a, b)),
        '/' => println!("Quotient is {}", divide(a, b)),
        '%' => println!("Remainder is {}", modulus(a, b)),
        _ => println!("Enter valid operation")
    }
}