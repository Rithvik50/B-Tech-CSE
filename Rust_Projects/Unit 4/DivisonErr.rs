use std::io;

fn main() {
    let mut input1 = String::new();
    io::stdin().read_line(&mut input1).expect("Failed to read the line");
    let dividend: i32 = input1.trim().parse().expect("Invalid input");

    let mut input2 = String::new();
    io::stdin().read_line(&mut input2).expect("Failed to read the line");
    let divisor: i32 = input2.trim().parse().expect("Invalid input");

    let divisor_check = is_zero(divisor);
    match divisor_check {
        Ok(_) => {
            println!("Quotient = {}", dividend / divisor);
        },
        Err(msg) => {
            println!("{}", msg);
        }
    }
}

fn is_zero(no: i32) -> Result<bool, String> {
    if no != 0 {
        return Ok(true);
    } else {
        return Err("Error: Divisor is 0".to_string());
    }
}