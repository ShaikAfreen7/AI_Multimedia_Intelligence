def run_video_sim(video_text_path):
    with open(video_text_path, "r") as file:
        text = file.read().lower()
    if "running" in text:
        return "Video Alert: Sudden Motion Detected!"
    else:
        return "Video Status: Normal Activity"
