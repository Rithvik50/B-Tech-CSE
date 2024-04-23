use std::io; //Brings input output to this file's scope

fn main() {
    println!("Enter the value");
    let mut userin = String::new(); //Create this mutable string to store user input. We don't know the type of the input so keep it as string
    io::stdin().read_line(&mut userin).expect("Failed to read the line");
    let c: i32 = userin.trim().parse().expect("Invalid input");
    println!("You have entered: {}", userin.trim());
    println!("Number is {}", c);
}