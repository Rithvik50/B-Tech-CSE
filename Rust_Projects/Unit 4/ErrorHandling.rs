use std::fs::File;

fn main() {
    let n = 10;
    if n % 2 == 0 {
        println!("Number is even");
    } else {
        panic!("Number is odd");
    }

    // let a = [10, 20, 30];
    // a[10]; // Invokes an error

    println!("\n\n");

    let f1 = File::open("main.jpg");
    println!("{:?}", f1);

    let f2 = File::open("main.jpg");
    match f2 {
        Ok(f2) => {
            println!("File found {:?}", f2);
        },
        Err(e) => {
            println!("File not found {:?}", e);
        }
    }

    let result = is_even(12);
    match result {
        Ok(d) => {
            println!("No is even {}", d);
        },
        Err(msg) => {
            println!("Error message is {}", msg);
        }
    }
    println!("End of main");
}

fn is_even(no: i32) -> Result<bool, String> {
    if no % 2 == 0 {
        return Ok(true);
    } else {
        return Err("Not an even number".to_string());
    }
}

/*
Error Handling:

panic!("Hello");
println!("End of main"); // Unreachable statement
*/