use std::io;

fn create(arr: &mut [i32; 4]) {
    for i in 0..4 {
        let mut input1 = String::new();
        io::stdin().read_line(&mut input1).expect("Invalid");
        let val: i32 = match input1.trim().parse() {
            Ok(parsed) => parsed,
            Err(_) => {
                println!("Nee vaisuki buddhi gnanam asalu raledhu");
                return;
            }
        };
        arr[i] = val;
    }
}

fn display(arr: &mut [i32; 4]) {
    println!("{:?}", arr);
}

fn product(arr: &mut [i32; 4]) -> i32 {
    let mut product: i32 = 1;
    for i in 0..4 {
        product *= arr[i];
    }
    return product;
}

fn main() {
    let mut arr: [i32; 4] = [0; 4];
    create(&mut arr);
    println!();
    display(&mut arr);
    println!();
    let product: i32 = product(&mut arr);
    println!("Product of the array elements is {}", product);
}