use std::io;

fn main() {

    // If else
    let mut input1 = String::new();
    println!("Enter a number");
    io::stdin().read_line(&mut input1).expect("Failed to read line");
    let num: i32 = match input1.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };
    if num % 2 == 0 {
        println!("Number is even");
    } else if num % 2 == 1 {
        println!("Number is odd");
    } else {
        println!("Number invalid");
    }

    println!();

    // Match case
    let mut input2 = String::new();
    println!("Enter a number");
    io::stdin().read_line(&mut input2).expect("Failed to read line");
    let number: i32 = match input2.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };
    match number {
        0 => println!("Number is 0"),
        1..=10 => println!("Number is 1-10"),
        _ => println!("Number is outside")
    }

    let mut state_code = String::new();
    io::stdin().read_line(&mut state_code).expect("Failed to read line");
    let state = match state_code.trim() {
        "AP" => "Andhra Pradesh",
        "GA" => "Goa",
        "KA" => {println!("Found match for KA"); "Karnataka"},
        "KL" => "Kerala",
        "TN" => "Tamil Nadu",
        "TS" => "Telangana",
        _ => "Unknown state"
    };
    println!("State name is: {}", state);
}