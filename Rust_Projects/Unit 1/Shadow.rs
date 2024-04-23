fn main() {
    let x = 42;
    println!("Original x: {}", x);
    let x = "Shadowed";
    println!("Shadowed x: {}", x);
    let x = true;
    println!("Boolean x: {}", x);
    let y: i32 = 10;
    println!("Original y: {}", y);
    let y = y * 2;
    println!("Doubled y: {}", y);
}

//x can hold all 3 values, but the most recent value shadows the previous ones