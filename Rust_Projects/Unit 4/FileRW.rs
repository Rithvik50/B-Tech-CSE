use std::fs::File;
use std::io::{self, BufRead, BufReader, BufWriter, Write};

fn main() -> io::Result<()> {
    // Writing to a file
    let mut writer = BufWriter::new(File::create("output.txt")?);
    writeln!(&mut writer, "Hello world!")?;
    writeln!(&mut writer, "My name is Rithvik and this is a Rust file IO example.")?;
    writer.flush()?;

    // Reading from a file
    let file = File::open("output.txt")?;
    let reader = BufReader::new(file);
    for line in reader.lines() {
        println!("{}", line?);
    }

    Ok(())
}
