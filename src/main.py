import ffmpeg, os, subprocess, fnmatch, config

def check_obs_status():
    result = subprocess.run(["tasklist", "|", "Select-String", "obs"])
    if result.stdout.find("obs"):
        return true
    else:
        return false

def convert_vid(dir, pattern):
    files_returned = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                files_returned.append(name)
    for i in range(len(files_returned)):
        item = files_returned[i]
        input_file = item
        output_file = os.path.splitext(input_file)[0] + ".mp4"
        ffmpeg.input(input_file).output(output_file).run()
def main():
    obs_dir = config.directory['obs_dir']
    pattern = "*.mkv"
    if check_obs_status():
        convert_vid(test_dir, pattern)

main()