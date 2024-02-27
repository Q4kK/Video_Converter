use tasklist;
use tokio::task;

fn main() {
    let task = tasklist::find_first_process_id_by_name;
    unsafe {
        if task("obs64.exe").is_some() {
            check_if_idle.await?;
            //
        } else {
        print!("No obs :)");
        }
    }
}

const check_if_idle = task::spawn(async {
    while true {
        if task("obs-ffmpeg-mux").is_some() {
            break true;
        }
    }
});