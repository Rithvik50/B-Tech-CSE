fn main() {
    println!("String Slicing:");
    let s1: String = String::from("Hello World!");
    let s2: &str = &s1[1..4];
    println!("{:?}", s2);
    let mut strdata = "Rithvik";
    str_slice(&mut strdata[1..4]);
    
    println!("\n");

    println!("Array Slicing:");
    let a1 = [1, 2, 3, 4, 5];
    let a2 = &a1[1..=4];
    println!("{:?}", a2);
    let mut arrdata = [10, 20, 30, 40, 50];
    arr_slice(&mut arrdata[1..4]);

    println!("\n");

    println!("Vector Slicing:");
    let v1: Vec<i32> = vec![60, 70, 80, 90, 100];
    let v2 = &v1[1..4];
    println!("{:?}", v2);
    let mut vecdata = vec![10, 20, 30, 40, 50];
    vec_slice(&mut vecdata[1..4]);
}

fn str_slice(slice: &str) {
    println!("Length of the slice is {:?}", slice.len());
    slice[1] = 'f';
    println!("{:?}", slice);
}

fn arr_slice(slice: &mut [i32]) {
    println!("Length of the slice is {:?}", slice.len());
    slice[1] = 5;
    println!("{:?}", slice);
}

fn vec_slice(slice: &mut Vec<i32>) {
    println!("Length of the slice is {:?}", slice.len());
    slice[1] = 5;
    println!("{:?}", slice);
}

/* 
Slices: represents a portion of a data structure, can be done for the following data structures
    - Arrays
    - Vectors
    - Strings
*/
