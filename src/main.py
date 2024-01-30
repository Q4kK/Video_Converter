import ffmpeg, os, subprocess, fnmatch, config, wmi

def check_obs_status():
    c = wmi.WMI()
    for process in c.Win32_Process():
        if "obs" not in f"{process.Name}":
            continue
        else:
            exit(1)
    print("we all good")
    return True
def convert_vid(dir, pattern):
    files_returned = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                files_returned.append(name)
    print(files_returned)
    for i in range(len(files_returned)):
        input_file = files_returned[i]
        output_file = os.path.splitext(input_file)[0] + ".mp4"
        ffmpeg.input(input_file).output(output_file).run()
def main():
    obs_dir = config.directory['obs_dir']
    pattern = "*.mkv"
    if check_obs_status():
        convert_vid(obs_dir, pattern)

main()
