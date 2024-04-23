use std::io;

fn concat_by_val(s1: String, s2: String) -> String {
    return s1 + &s2;
}

fn concat_by_ref(s1: &str, s2: &str) -> String {
    let mut concat = String::new();
    concat.push_str(s1);
    concat.push_str(s2);
    return concat;
}

fn main() {
    // Value
    let mut s1 = String::new();
    io::stdin().read_line(&mut s1).expect("Failed");
    let mut s2 = String::new();
    io::stdin().read_line(&mut s2).expect("Failed");
    let s3 = concat_by_val(s1, s2);
    println!("Concatenated string: {}", s3);


    // Reference
    let s4: &str = "Rithvik";
    let s5: &str = "Muthyalapati";
    let s6 = concat_by_ref(&s4, &s5);
    println!("Concatenated string: {}", s6);
}