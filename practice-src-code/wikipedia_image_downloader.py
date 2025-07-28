"""
Web scraper to extract and download images from Wikipedia

This script scrapes the Deep Blue chess computer Wikipedia page,
extracts image information, and downloads an image to the local directory.
"""

# Grabbing and saving an image
import requests
import bs4

# URL of the Wikipedia page to scrape
url = "https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)"

# Send GET request to fetch the HTML content of the page
res = requests.get(url)

# Parse the HTML content using BeautifulSoup with lxml parser
soup = bs4.BeautifulSoup(res.text, "lxml")

# Select all image elements with class "mw-file-element" (Wikipedia's image wrapper class)
img_info = soup.select(".mw-file-element")

# Get the second image element (index 1) from the page
computer = img_info[1]

# Print the source URL of the selected image
print(computer["src"])

# Send GET request to download the image from the extracted URL
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/250px-Deep_Blue.jpg")

# Open a new file in write-binary mode to save the image
f = open("my_computer_image.jpg", "wb")

# Write the binary content of the image to the file
f.write(image_link.content)

# Close the file to ensure data is saved properly
f.close()