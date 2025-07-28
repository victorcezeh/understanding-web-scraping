"""
Wikipedia scraper to extract elements from a specific CSS class

This script scrapes a Wikipedia page (Grace Hopper) and extracts text content
from elements with the "vector-toc-text" class.
"""

# Grab all elements of a class

import requests
import bs4

# URL of the Wikipedia page to scrape
url = "https://en.wikipedia.org/wiki/Grace_Hopper"

# Send GET request to fetch the HTML content of the page
result = requests.get(url)

# Parse the HTML content using BeautifulSoup with lxml parser
soup = bs4.BeautifulSoup(result.text, "lxml")

# Select the second element (index 1) from elements with class "vector-toc-text"
# This targets a specific table of contents item. Removing the (index 1) prints all the table of content.
first_item = soup.select(".vector-toc-text")[1]


# Alternative method using get_text() with strip=True to remove whitespace
# for item in first_item:
#     print(item.get_text(strip=True))
    

# Iterate through the selected element and print the text content
for item in first_item:
    print(item.text)