fn update_by_value(mut arr: [i32; 4]) {
    for i in 0..4 {
        arr[i] = 0;
    }
    println!("Inside update_by_value() {:?}", arr);
}

fn update_by_reference(arr: &mut [i32; 4]) {
    for i in 0..4 {
        arr[i] = 0;
    }
    println!("Inside update_by_reference() {:?}", arr);
}

fn main() {
    // 1st Type
    let arr1 = [10, 20, 30, 40];
    println!("Array 1 is {:?}", arr1);
    println!("Array 1 size is {}", arr1.len());
    for index in 0..4 {
        println!("Index: {}, Value: {}", index, arr1[index]);
    }
    println!("\n");

    // 2nd Type
    let arr2: [i32; 4] = [50, 60, 70, 80];
    println!("Array 2 is {:?}", arr2);
    println!("Array 2 size is {}", arr2.len());
    for val in arr2.iter() {
        println!("Value: {}", val);
    }
    println!("\n");

    // 3rd Type
    let arr3: [i32; 10] = [90; 10];
    println!("Array 3 is {:?}", arr3);
    println!("Array 3 size is {}", arr3.len());
    println!("\n");

    // Pass by value
    let arr4 = [100, 200, 300, 400];
    update_by_value(arr4);
    println!("Inside main() {:?}", arr4);
    println!("\n");

    // Pass by reference
    let mut arr5 = [500, 600, 700, 800];
    update_by_reference(&mut arr5);
    println!("Inside main() {:?}", arr5);
    println!("\n");
}


/* 
Arrays:
    Declaration:
        ArrayType: [dataype; expression]
        1) let variable_name = [value1, value2,...];
        2) let variable_name: [datatype; size_n] = [value1, value2,...,value_n]
        3) let variable_name: [datatype; size_n] = [value; number_of_times_to_repeat_the_value];

    Iteration:
        for value in index1..index2 {

        }
*/