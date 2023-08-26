from pytube import YouTube

# URL of the YouTube video
video_url = "https://www.youtube.com/watch?v=UI0n7ElZkHY"

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest quality audio stream
audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

# Set the path where you want to save the audio file
output_path = "audio/"

# Download the audio stream
audio_stream.download(output_path)

print("Audio download completed.")