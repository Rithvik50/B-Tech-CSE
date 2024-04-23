fn add_item(cart: &mut Vec<String>, item: String) {
    cart.push(item);
}

fn remove_item(cart: &mut Vec<String>, item_index: usize) {
    if item_index < cart.len() {
        cart.remove(item_index);
    }
}

fn view_cart(cart: &Vec<String>) {
    println!("Shopping Cart: ");
    for (index, item) in cart.iter().enumerate() {
        println!("{}: {}", index + 1, item);
    }
}

fn main() {
    let mut shopping_cart: Vec<String> = Vec::new();
    add_item(&mut shopping_cart, String::from("Apple"));
    add_item(&mut shopping_cart, String::from("Banana"));
    add_item(&mut shopping_cart, String::from("Orange"));
    view_cart(&mut shopping_cart);
    remove_item(&mut shopping_cart, 1);
    view_cart(&mut shopping_cart);
}