use std::io;

struct Book {
    title: String,
    author: String,
    genre: String
}

fn main() {
    println!("Enter title: ");
    let mut b_title: String = String::new();
    io::stdin().read_line(&mut b_title).expect("Failed to read the line");

    println!("Enter author: ");
    let mut b_author: String = String::new();
    io::stdin().read_line(&mut b_author).expect("Failed to read the line");

    println!("Enter genre: ");
    let mut b_genre: String = String::new();
    io::stdin().read_line(&mut b_genre).expect("Failed to read the line");

    let book: Book = Book{title: b_title, author: b_author, genre: b_genre};
    println!("Title: {}, Author: {}, Genre: {}", book.title, book.author, book.genre);
}