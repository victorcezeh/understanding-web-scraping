"""
Web scraper to extract the top ten tags from quotes.toscrape.com

This script scrapes the quotes website and collects the top ten most popular tags
displayed in the sidebar on the right side of the home page.
"""

# TASK -> Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page

import requests
import bs4

# Base URL template for the quotes website - {} will be replaced with page numbers
base_url = "https://quotes.toscrape.com/page/{}/"

# Send GET request to fetch the first page (page 1) of quotes
res = requests.get(base_url.format(1))

# Parse the HTML content using BeautifulSoup with lxml parser
soup = bs4.BeautifulSoup(res.text, "lxml")

# Select all tag elements from the "Top Ten tags" section using CSS class "tag-item"
tags = soup.select(".tag-item")

# Initialize empty list to store the top 10 tag names
top_10 = []
    
# Iterate through each tag element and extract the text content
for tag in tags:
   # Append the tag text to our list, using strip() to remove any extra whitespace
   top_10.append(tag.text.strip())
    
# Print the list of top 10 tags from the sidebar
print(top_10)