use std::io;

fn main() {
    println!("Enter the value");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let number: i32 = match input.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };
    println!("You entered: {}", number);
}