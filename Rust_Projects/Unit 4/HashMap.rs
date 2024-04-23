use std::collections::HashMap;

fn main() {
    let mut map: HashMap<&str, i32> = HashMap::new();

    // Insertion
    map.insert("One", 1);
    map.insert("Two", 2);
    map.insert("Three", 3);
    map.insert("Four", 4);
    map.insert("Five", 5);
    println!("After insertion: {:?}", map);

    println!("\n");

    // Deletion
    if map.contains_key("Three") {
        map.remove("Three");
    }
    println!("After deletion: {:?}", map);

    println!("\n");

    // Updating
    if let Some(value) = map.get_mut("Two") {
        *value = 20;
    }
    println!("After updating: {:?}", map);

    println!("\n");

    // Accessing elements
    if let Some(value) = map.get("Four") {
        println!("The value associated with 'Four' is: {}", value);
    } else {
        println!("'Four' is not present in the map.");
    }
    
    println!("\n");

    // Looping elements
    for (key, value) in map.iter_mut() {
        if *value == 6 {
            continue;
        } else {
            map.insert("Six", 6);
            break;
        }
    }
    println!("After updating from looping: {:?}", map);
}
