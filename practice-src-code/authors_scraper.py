"""
Web scraper to extract all unique author names from the first page of quotes.toscrape.com

This script scrapes the quotes website and collects all author names
from the first page, using a set to ensure only unique names are stored.
"""

# TASK -> Get the names of all the authors on the first page

import requests
import bs4

# Base URL template for the quotes website - {} will be replaced with page numbers
base_url = "https://quotes.toscrape.com/page/{}/"

# Send GET request to fetch the first page (page 1) of quotes
res = requests.get(base_url.format(1))

# Parse the HTML content using BeautifulSoup with lxml parser
soup = bs4.BeautifulSoup(res.text, "lxml")

# Select all author name elements using the CSS class "author"
author_list = soup.select(".author")

# Initialize empty set to store unique author names (sets automatically remove duplicates)
authors = set()

# Iterate through each author element and extract the text content
for name in author_list:
    # Add the author name to our set (duplicates will be automatically ignored)
    authors.add(name.text)
    
# Print the set of unique author names from the first page
print(authors)