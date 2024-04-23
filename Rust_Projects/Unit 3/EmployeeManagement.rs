struct Employee {
    name: String,
    age: u32,
    department: String,
}

impl Employee {
    fn new(name: &str, age: u32, department: &str) -> Employee {
        Employee {
            name: name.to_string(),
            age,
            department: department.to_string(),
        }
    }

    fn display(&self) {
        println!("Name: {}", self.name);
        println!("Age: {}", self.age);
        println!("Department: {}", self.department);
        println!("-------------------------");
    }
}

fn main() {
    let mut employees: Vec<Employee> = Vec::new();

    employees.push(Employee::new("Rithvik Muthyalapati", 19, "Engineering"));
    employees.push(Employee::new("Peter Parker", 19, "Law"));
    employees.push(Employee::new("Jonathan Parker", 40, "Marketing"));

    println!("Employee Management System:");
    for employee in &employees {
        employee.display();
    }
}
