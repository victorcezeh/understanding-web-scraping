"""
Web scraper to extract all quotes from the first page of quotes.toscrape.com

This script scrapes the quotes website and collects all quote texts
from the first page into a list for display.
"""

# TASK -> Create a list of all the quotes on the first page

import requests
import bs4

# Base URL template for the quotes website - {} will be replaced with page numbers
base_url = "https://quotes.toscrape.com/page/{}/"

# Send GET request to fetch the first page (page 1) of quotes
res = requests.get(base_url.format(1))

# Parse the HTML content using BeautifulSoup with lxml parser
soup = bs4.BeautifulSoup(res.text, "lxml")

# Select all quote text elements using the CSS class "text"
quote_list = soup.select(".text")

# Initialize empty list to store the extracted quote texts
quotes = []

# Iterate through each quote element and extract the text content
for quote in quote_list:
    # Append the text content of each quote to our list
    quotes.append(quote.text)
    
# Print the complete list of quotes from the first page
print(quotes)