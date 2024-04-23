fn main() {
    let numbers = [10, 20, 30, 40, 50];
    let sum = calculate_sum(&numbers[..]);
    println!("Sum of elements: {}", sum);
}

fn calculate_sum(numbers: &[i32]) -> i32 {
    let mut sum = 0;
    for &num in numbers {
        sum += num;
    }
    sum
}