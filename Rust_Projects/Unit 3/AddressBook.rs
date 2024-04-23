struct Contact {
    name: String,
    email: String,
    phone_number: String,
}

impl Contact {
    fn new(name: &str, email: &str, phone_number: &str) -> Contact {
        Contact {
            name: name.to_string(),
            email: email.to_string(),
            phone_number: phone_number.to_string(),
        }
    }

    fn display(&self) {
        println!("Name: {}", self.name);
        println!("Email: {}", self.email);
        println!("Phone Number: {}", self.phone_number);
        println!("-------------------------");
    }
}

fn main() {
    let mut address_book: Vec<Contact> = Vec::new();

    address_book.push(Contact::new("Rithvik Muthyalapati", "rmuthyalapati@gmail.com", "+918951717766"));
    address_book.push(Contact::new("Sudhir Muthyalapati", "muthyalapati.sudhir@gmail.com", "+918660676023"));
    address_book.push(Contact::new("Elvish Yadav", "e.yadav@gmail.com", "+918235866725"));

    println!("Address Book:");
    for contact in &address_book {
        contact.display();
    }
}
