fn main() {
    let age: i32 = 90;
    let is_value: bool = true;
    let name: &str = "Rithvik";
    println!("Name: {}, Age: {}, Is_value: {}", name, age, is_value);

    //Integer
    let integer_number: i32 = -42;
    let unsigned_integer_number: u64 = 123;
    //Float
    let float_number: f64 = 3.14;
    //Boolean
    let is_true: bool = true;
    //Character
    let character: char = 'A';
    //String
    let string_text: String = String::from("Hello Rust!"); //String::new() for empty string
    //Tuple
    let tuple_example: (i32, f64, char) = (10, 3.5, 'X');
    //Array
    let array_example: [i32; 3] = [1, 2, 6];

    println!("Integers: {} {}\nFloat: {}\nBoolean: {}\nCharacter: {}\nString: {}Tuple: {:?}\nArray: {:?}", 
            integer_number, unsigned_integer_number, float_number, is_true, character, string_text, tuple_example, array_example);
}