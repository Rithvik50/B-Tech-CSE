use std::io;

fn deposit(balance: &mut f64, amount: f64) {
    *balance -= amount;
}

fn withdraw(balance: &mut f64, amount: f64) {
    *balance += amount;
}

fn display(balance: f64) {
    println!("Balance: {}", balance);
}

fn main() {
    println!("Enter balance: ");
    let mut input1 = String::new();
    io::stdin().read_line(&mut input1).expect("Failed");
    let mut balance: f64 = match input1.trim().parse() {
        Ok(parsed) => parsed,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };

    println!("Enter action: ");
    let mut action = String::new();
    io::stdin().read_line(&mut action).expect("Failed");

    let mut amount: f64 = 0.0;
    if action.trim() == "deposit" {
        println!("Enter amount to be deposited: ");
        let mut input2 = String::new();
        io::stdin().read_line(&mut input2).expect("Failed");
        amount = match input2.trim().parse() {
            Ok(parsed) => parsed,
            Err(_) => {
                println!("Invalid input");
                return;
            }
        };
        deposit(&mut balance, amount);
        println!("Deposited {} from balance", amount);
        display(balance);
    } else if action.trim() == "withdraw" {
        println!("Enter amount to be withdrawn: ");
        let mut input3 = String::new();
        io::stdin().read_line(&mut input3).expect("Failed");
        amount = match input3.trim().parse() {
            Ok(parsed) => parsed,
            Err(_) => {
                println!("Invalid input");
                return;
            }
        };
        withdraw(&mut balance, amount);
        println!("Withdrawn {} from balance", amount);
        display(balance);
    } else if action.trim() == "display" {
        display(balance);
    } else {
        println!("Enter proper action");
    }
}