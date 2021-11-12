use std::fs;

pub fn day01() {
    let contents = fs::read_to_string("src/data/day01");
    let x = contents.ok().unwrap();
    let x = x.trim();
    let mut total = 0;
    let mut first_negative = -1;
    for (i, c) in x.chars().enumerate() {
        if c == '(' {
            total += 1;
        }
        else if c == ')'  {
            total -= 1;
        }
        if total < 0 && first_negative < 0 {
            first_negative = (i + 1) as i32;
        }
    }
    println!("Part 1: {:?}", total);
    println!("Part 2: {:?}", first_negative);
}
