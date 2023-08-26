import requests
from bs4 import BeautifulSoup

# URL of the YouTube channel
channel_url = "https://www.youtube.com/c/@TheYardPodcast/videos"

# Send an HTTP GET request to the channel URL
response = requests.get(channel_url)
print(response)
print(response.text)

# Parse the HTML content of the response
soup = BeautifulSoup(response.text, "html.parser")

# Find all video elements using their class name
video_elements = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-grid-video-renderer")

# Extract video IDs from the href attribute
video_ids = [video["href"].split("v=")[1] for video in video_elements if "v=" in video["href"]]

# Path to the output file
output_file_path = "video_ids.txt"

# Save the video IDs to a text file
with open(output_file_path, "w") as output_file:
    for video_id in video_ids:
        output_file.write(video_id + "\n")

print("Video IDs saved to", output_file_path)
