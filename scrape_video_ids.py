from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



options=Options()
options.add_argument("start-maximized")

# URL of the YouTube channel
channel_url = "https://www.youtube.com/@TheYardPodcast/videos"

# Path to the Chrome WebDriver executable
driver_path = "chromedriver.exe"  # Change this to the actual name of the WebDriver

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Open the channel URL
driver.get(channel_url)

# Wait for the page to load (adjust the wait time as needed)
driver.implicitly_wait(100)

# Scroll down to load more videos (repeat this step as needed)
# You might need to adjust the number of scrolls based on the channel's layout
num_scrolls = 6
for x in range(num_scrolls):

    time.sleep(5)
    height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script("window.scrollTo(0, " + str(height) + ");")
    
    print(x)


# Find video elements by CSS selector
video_elements = driver.find_elements(By.ID, "video-title-link")

# Extract video IDs
video_ids = [video.get_attribute("href").split("v=")[1] for video in video_elements if "v=" in video.get_attribute("href")]

# Path to the output file
output_file_path = "data/video_ids.txt"

# Save the video IDs to a text file
with open(output_file_path, "w") as output_file:
    for video_id in video_ids:
        output_file.write(video_id + "\n")

print("Video IDs saved to", output_file_path)

# Close the WebDriver
driver.quit()
