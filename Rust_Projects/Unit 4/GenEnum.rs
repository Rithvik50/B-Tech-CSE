enum Value<T> {
    Int(T),
    Str(T),
}

fn main() {
    let int_value: Value<i32> = Value::Int(42);
    match int_value {
        Value::Int(num) => println!("Integer value: {}", num),
        Value::Str(_) => println!("Expected an integer, but got a string."),
    }

    let str_value: Value<String> = Value::Str(String::from("Hello world!"));
    match str_value {
        Value::Int(_) => println!("Expected a string, but got an integer."),
        Value::Str(s) => println!("String value: {}", s),
    }
}
