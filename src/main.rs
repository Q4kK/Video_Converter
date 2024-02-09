use tasklist;
use tokio;

fn main() {
    unsafe {
        if tasklist::find_first_process_id_by_name("obs64.exe").is_some() {
            let obs = tasklist::find_process_id_by_name("obs64.exe");
        } else {
        print!("No obs :)");
        }
    }
}

async fn await_idle() {
// Wait for obs-ffmpeg-mux.exe to stop running
}
