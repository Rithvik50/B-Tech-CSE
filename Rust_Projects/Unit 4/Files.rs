use std::io::Read;
use std::io::Write;
use std::fs::OpenOptions;
use std::fs;

fn main() {
    // Writing to the file
    let mut file1 = std::fs::File::create("file_data.txt").expect("Create failed");
    file1.write_all("Hello World".as_bytes()).expect("Write failed");
    file1.write_all("\nRust Programming".as_bytes()).expect("Write failed");
    println!("Data written to the file");

    println!("\n");

    // Reading from the file
    let mut file2 = std::fs::File::open("file_data.txt").expect("Create failed");
    let mut contents = String::new();
    file2.read_to_string(&mut contents).unwrap();
    println!("{}", contents);
    println!("Data read from the file");

    println!("\n");

    // Append to the file
    let mut file3 = OpenOptions::new().write(true).append(true).open("file_data.txt").expect("Create failed");
    file3.write_all("\nMy name is".as_bytes()).expect("Append failed");
    file3.write_all("\nRithvik Muthyalapati".as_bytes()).expect("Append failed");
    println!("Data appended to the file");

    println!("\n");

    // Removing the file
    fs::remove_file("file_data.txt").expect("Could not remove file");
    println!("File has been removed");
}