struct Data<T> { // Generic type structure
    value: T
}

fn main() {
    let mut vector_integer: Vec<i32> = vec![20, 30];
    vector_integer.push(40);
    println!("{:?}", vector_integer);

    // Generic type of i32
    let t1: Data<i32> = Data { value: 350 };
    println!("Value is {}", t1.value);
    // Generic type of String
    let t2: Data<String> = Data { value: "Tom".to_string() };
    println!("Value is {}", t2.value);

    // Max
    let max1 = max(3, 4);
    println!("Max is {}", max1);
    let max2 = max(3.14, 3.15);
    println!("Max is {}", max2);
    let max3 = max("Hello", "Hell");
    println!("Max is {}", max3);
}

fn max<T: PartialOrd>(n1: T, n2: T) -> T { // Generic type function
    if n1 > n2 {
        n1
    } else {
        n2
    }
}