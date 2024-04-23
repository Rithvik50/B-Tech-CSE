use std::io;

fn calc(a: i32, b: i32, op: char) -> i32 {
    if op == '+' {
        return a + b;
    } else if op == '-' {
        return a - b;
    } else if op == '*' {
        return a * b;
    } else if op == '/' {
        return a / b;
    } else if op == '%' {
        return a % b;
    } else {
        return 0;
    }
}

fn immutate_no_zero(mut param_no: i32) { // Immutable parameters
    param_no *= 0;
    println!("param_no value is {}", param_no);
}

fn mutate_no_zero(param_no: &mut i32) { // Mutable parameters
    *param_no = 0;
    println!("param_no value is {}", *param_no);
}

fn display(param_name: String) {
    println!("param_name value is {}", param_name);
}

fn main() {
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
    println!("Answer is {}", calc(a, b, op));

    println!("\n\n\n");

    let mut no: i32 = 5;
    immutate_no_zero(no);
    println!("No value {}", no);
    println!("\n");
    mutate_no_zero(&mut no);
    println!("No value {}", no);

    println!("\n\n\n");

    let name: String = String::from("Rust programming");
    display(name);
}