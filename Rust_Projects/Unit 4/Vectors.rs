fn main() {
    let mut v1 = Vec::new();
    v1.push(10);
    v1.push(20);
    v1.push(30);
    println!("Size of vector is {}", v1.len());
    println!("{:?}", v1);
    v1.remove(1);
    println!("Size of vector is {}", v1.len());
    println!("{:?}", v1);

    println!("\n");

    let mut v2: Vec<i32> = vec!{20, 30, 40};
    v2.push(80);
    v2.push(50);
    v2.push(10);
    println!("Size of vector is {}", v2.len());
    println!("{:?}", v2);
    println!("\n");
    let elem = 80;
    if v2.contains(&elem) {
        println!("Vector 2 contains 80");
    } else {
        println!("Vector 2 does not contain 80");
    }
}