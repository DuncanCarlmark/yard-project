from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi


# Load all video IDs from the text file
video_ids = []
with open("data/video_ids.txt", "r") as input_file:
    for line in input_file:
        video_ids.append(line.strip())

SUCCESSFUL_VIDEOS = 0
UNSUCCESSFUL_VIDEOS = 0

errored_video_ids = []

# Loop through all video IDs and attempt to download subtitles
for video_id in video_ids:

    try:
        # URL of the YouTube video
        video_url = "https://www.youtube.com/watch?v=" + video_id

        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the video ID from the URL
        video_id = yt.video_id

        # Get the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Create a file to save the subtitles
        output_path = "data/subtitles/"
        subtitles_filename = f"{video_id}_subtitles.txt"

        # Save the subtitles with timestamps to a file
        with open(output_path + subtitles_filename, "w", encoding="utf-8") as subtitles_file:
            for entry in transcript:
                start_time = entry['start']
                end_time = entry['start'] + entry['duration']
                subtitle_text = entry['text']
                
                formatted_start_time = f"{round(start_time // 60, 2)}:{round(start_time % 60, 4)}"
                formatted_end_time = f"{round(end_time // 60, 2)}:{round(end_time % 60, 2)}"
                
                subtitles_file.write(f"{formatted_start_time} --> {formatted_end_time}\n{subtitle_text}\n\n")

        SUCCESSFUL_VIDEOS += 1
        print("Subtitles download with timestamps completed.")

    except:
        UNSUCCESSFUL_VIDEOS += 1
        errored_video_ids.append(video_id)
        print(f"Error downloading subtitles for video {video_id}")
        print(f"Number of errored videos: {UNSUCCESSFUL_VIDEOS}")

# Log results of the run

log_path = "data/subtitles_download_log.txt"

with open(log_path, "w") as log_file:
    log_file.write(f"Number of successful downloads: {SUCCESSFUL_VIDEOS}\n")
    log_file.write(f"Number of unsuccessful downloads: {UNSUCCESSFUL_VIDEOS}\n")
    log_file.write(f"Total number of videos: {SUCCESSFUL_VIDEOS + UNSUCCESSFUL_VIDEOS}\n") 
    log_file.write(f"Errored video IDs: {errored_video_ids}\n")