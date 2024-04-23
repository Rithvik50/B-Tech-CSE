fn display(v5: Vec<i32>) -> Vec<i32> {
    println!("Inside display v5: {:?}", v5);
    return v5;
}

fn main() {
    let v1: Vec<i32> = vec![1, 2, 3];
    let v2 = v1;
    println!("v2: {:?}", v2);

    // ISA 1 Question
    // let a: i64 = 5;
    // let b: i32 = a; // Returns error. Although both are integers, they must be exactly the same integer type. Either both have to be i32 or both have to be i64. This rule applies to all datatypes
    // println!("{}", b);

    let c = 6;
    let _d = c; // Variables can have underscore in front of the name
    println!("c: {}", c);
    println!("d: {}", _d);

    let s1 = String::from("Hello");
    let s2 = s1;
    // println!("s1: {}", s1); // Returns error
    println!("s2: {}", s2);


    let v3 = vec![1, 2, 3];
    let v4 = v3; // v4 gains ownership of v3's value
    let v6 = display(v4); // v5 in display gains ownership of v4's value. When the function returns v5, ownership gets transferred to v6
    println!("In main v6: {:?}", v6);
}

/*
- Each value in Rust has a variable that's called its owner. There can only be one ower at a time, when the ower goes out of scope the value is dropped
- Ex: let age = 30, age is the owner of the value 30
- Trasferring ownership:
    - Assigning value of one variable to another
    - Passing value to a function
    - Returning value from a function
- When value is transferred from owner and you try to operate on the owner, it will return a borrow error. This works on non-primitive datatype variables
*/