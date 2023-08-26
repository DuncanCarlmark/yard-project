from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# URL of the YouTube video
video_url = "https://www.youtube.com/watch?v=UI0n7ElZkHY"

# Create a YouTube object
yt = YouTube(video_url)

# Get the video ID from the URL
video_id = yt.video_id

# Get the transcript for the video
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Create a file to save the subtitles
output_path = "subtitles/"
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

print("Subtitles download with timestamps completed.")