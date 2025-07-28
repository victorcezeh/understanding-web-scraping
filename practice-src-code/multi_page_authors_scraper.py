"""
Web scraper to extract all unique authors from all pages of quotes.toscrape.com

This script demonstrates two different approaches to scrape multiple pages:
1. Fixed range approach (when you know the total number of pages)
2. Dynamic approach (when you don't know how many pages exist)
"""

# TASK -> There is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what I know about for loops and string concatenation (I used a string format instead) to loop through all the pages and get all the unique authors on the website.
# There are two ways to solve this.

import requests
import bs4

# Step 1 -> This assumes you know how many pages are on the website.

# Base URL template for pagination - {} will be replaced with page numbers
base_url = "https://quotes.toscrape.com/page/{}/"

# Initialize empty set to store unique author names across all pages
authors = set()

# Loop through pages 1 to 10 (assuming we know there are 10 pages total)
for page in range(1, 11):
    # Format the URL with the current page number
    page_url = base_url.format(page)
    
    # Send GET request to fetch the current page
    res = requests.get(page_url)
    
    # Parse the HTML content using BeautifulSoup with lxml parser
    soup = bs4.BeautifulSoup(res.text, "lxml")
    
    # Select all author name elements on the current page
    author_list = soup.select(".author")
    
    # Extract each author name and add to our set (duplicates automatically ignored)
    for name in author_list:
        authors.add(name.text)
    
# Print all unique authors in alphabetical order
print(sorted(authors))


# Step 2 -> This assumes you do not know how many pages are on the website. This is more robust.

# Flag to control the while loop - continues until no more valid pages
page_still_valid = True
# Start from page 1
page = 1

# Continue looping until we reach a page with no quotes
while page_still_valid:
    
    # Format the URL with the current page number
    page_url = base_url.format(page)
    
    # Send GET request to fetch the current page
    res = requests.get(page_url)
    
    # Check if we've reached the end (page with no quotes shows "No quotes found!")
    if "No quotes found!" in res.text:
        break
    
    # Parse the HTML content using BeautifulSoup with lxml parser
    soup = bs4.BeautifulSoup(res.text, "lxml")
    
    # Select all author name elements on the current page
    author_list = soup.select(".author")
    
    # Extract each author name and add to our set
    for name in author_list:
        authors.add(name.text)
        
    # Move to the next page
    page += 1

# Print all unique authors in alphabetical order
print(sorted(authors))