use std::io;

fn main() {
    println!("Enter first number: ");
    let mut input1 = String::new();
    io::stdin().read_line(&mut input1).expect("Failed to read line");
    let a: i32 = match input1.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };

    println!("Enter operator: ");
    let mut input2 = String::new();
    io::stdin().read_line(&mut input2).expect("Failed to read line");
    let op: char = match input2.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };

    println!("Enter second number: ");
    let mut input3 = String::new();
    io::stdin().read_line(&mut input3).expect("Failed to read line");
    let b: i32 = match input3.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };
    
    match op {
        '+' => println!("Sum = {}", a + b),
        '-' => println!("Difference = {}", a - b),
        '*' => println!("Product = {}", a * b),
        '/' => println!("Quotient = {}", a / b),
        '%' => println!("Modulus = {}", a % b),
        _ => println!("Enter a proper operator")
    }
}