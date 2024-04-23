fn main() {
    let mut s = String::from("Hello this is a string");

    // Inserting into the string
    s.insert_str(6, "epic ");
    println!("After inserting: {}", s);

    println!("\n");

    // Deleting a character
    s.remove(13);
    println!("After removing: {}", s);

    println!("\n");

    // Searching for an element
    if let Some(index) = s.find('s') {
        println!("Found 's' at index {}", index);
    } else {
        println!("'s' not found in the string");
    }
}
