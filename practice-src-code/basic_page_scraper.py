"""
Web scraper to extract page title and paragraph content from example.com

This script demonstrates basic web scraping by fetching the page title
and first paragraph from example.com, along with showing data types.
"""

# Grabbing a page title

import requests
import bs4

# Send GET request to example.com and store the response object
result = requests.get("https://example.com/")
print(result.status_code)

# Parse the HTML content using BeautifulSoup with lxml parser
soup = bs4.BeautifulSoup(result.text, "lxml")
#print(soup)

# Extract and print the page title
# Select the first (and usually only) title element and get its text content
print(soup.select("title")[0].getText())

# Select all paragraph elements on the page
site_paragraph = soup.select("p")

# Print the text content of the first paragraph
print(site_paragraph[0].get_text())

# Print the data type of the first paragraph element (shows it's a BeautifulSoup Tag object)
print(type(site_paragraph[0]))