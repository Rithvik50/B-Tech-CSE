use std::io;

fn main() {
    // For loop (definite)
    let mut input1 = String::new();
    io::stdin().read_line(&mut input1).expect("Failed to read line");
    let i: i32 = match input1.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };
    for x in 1..i {
        if x == 5 {
            continue;
        }
        if x == 9 {
            break;
        }
        println!("x is {}", x);
    }

    // While loop (indefinite)
    let mut input2 = String::new();
    io::stdin().read_line(&mut input2).expect("Failed to read line");
    let j: i32 = match input2.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };
    println!("Even numbers");
    let mut i = 0;
    while i < j {
        if i % 2 == 0 {
            println!("{}", i);
        }
        i += 1;
    }

    // Loop loop
    let mut input3 = String::new();
    io::stdin().read_line(&mut input3).expect("Failed to read line");
    let count: i32 = match input3.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };
    let mut k = 0;
    loop {
        k += 1;
        if k == count {
            break;
        }
        println!("Wake Up!");
    }
}
