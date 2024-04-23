struct User {
    id: i32,
    name: String,
    is_admin: bool,
}

fn get_user(name: String) -> User {
    return User {
        id: 1,
        name, // This is called field init shorthand and it is the same as name: name,
        is_admin: false,
    }
}

fn main() {
    let mut user1 = User{id: 451, name: String::from("Rithvik"), is_admin: true}; // Need to make instance of structure as mutable to change the value of the fields
    println!("{} {} {}", user1.id, user1.name, user1.is_admin);
    user1.is_admin = false;
    println!("{} {} {}", user1.id, user1.name, user1.is_admin);

    let user2 = get_user(String::from("Elvish"));
    println!("{} {} {}", user2.id, user2.name, user2.is_admin);
    
    let user3: User = User{name: String::from("Niteesh"), ..user1}; // ..user1 will fill the rest of user3's fields with the respective values from user1
    println!("{} {} {}", user3.id, user3.name, user3.is_admin);
}