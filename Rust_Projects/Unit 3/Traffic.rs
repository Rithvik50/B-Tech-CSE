enum TrafficLight {
    Red,
    Yellow,
    Green,
}

fn print_action(light: TrafficLight) {
    match light {
        TrafficLight::Red => println!("Stop"),
        TrafficLight::Yellow => println!("Prepare to stop"),
        TrafficLight::Green => println!("Go"),
    }
}

fn main() {
    let red_light = TrafficLight::Red;
    let yellow_light = TrafficLight::Yellow;
    let green_light = TrafficLight::Green;

    print_action(red_light);
    print_action(yellow_light);
    print_action(green_light);
}
