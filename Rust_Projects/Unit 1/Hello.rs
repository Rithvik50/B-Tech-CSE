fn main() {
    let x = 5; //Variable are immutable by default
    let mut x = 6; //Variable is now mutable. System will print the 6 because this x declaration is last.
                   //If let x = 5 is last, then the system will print 5
                   //Print statement will print the x value that is most recent/last most
    println!("Hello World!");
    println!("{} and {}", x, x);
}