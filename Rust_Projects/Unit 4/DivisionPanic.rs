use std::io;

fn main() {
    let mut input1 = String::new();
    io::stdin().read_line(&mut input1).expect("Failed to read the line");
    let dividend: i32 = input1.trim().parse().expect("Invalid input");

    let mut input2 = String::new();
    io::stdin().read_line(&mut input2).expect("Failed to read the line");
    let divisor: i32 = input2.trim().parse().expect("Invalid input");

    if divisor != 0 {
        println!("Quotient = {}", dividend / divisor);
    } else {
        panic!("Cannot divide with 0");
    }
}