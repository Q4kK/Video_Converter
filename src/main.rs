use tasklist;
use std::io;

fn main() {
    unsafe {
    let tl = tasklist::Tasklist::new();
        if tl.find_first_process_id_by_name("obs") {
            print!("obs");
        } else {
        print!("No obs :)");
        }
    }
}
