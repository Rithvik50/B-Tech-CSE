#[derive(Debug)]
enum GenderCategory {
    Male, Female, NonBinary
}

#[derive(Debug)]
enum CarType {
    Hatch,
    Sedan,
    Suv
}

#[derive(Debug)]
struct Person {
    name: String,
    gender: GenderCategory
}

fn main() {
    let p1 = Person{
        name: String::from("Rama"),
        gender: GenderCategory::Male
    };

    let p2 = Person{
        name: String::from("Seetha"),
        gender: GenderCategory::Female
    };

    println!("{:?}", p1);
    println!("{:?}", p2);

    let result = is_even(3);
    println!("{:?}", result);
    println!("{:?}", is_even(30));

    print_size(Cartype::Suv);
    print_size(Cartype::Hatch);
    print_size(CarType::Sedan);
}

fn is_even(no: i32) -> Option<bool> {
    if no % 2 == 0 {
        Some(true)
    } else {
        None
    }
}

fn print_size(car: Cartype) {
    match car {
        Cartype::Hatch => {
            println!("Small sized car");
        }
        Cartype::Sedan => {
            println!("Medium sized car");
        }
        Cartype::Suv => {
            println!("Large sized sports utility car");
        }
    }
}