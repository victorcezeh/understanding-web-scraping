"""
Web scraper to extract book titles with 2-star ratings from books.toscrape.com

This script scrapes multiple pages of the book catalog website to find all books
that have exactly 2-star ratings and collects their titles.
"""

# Working with multiple pages and items
# Goal: Get the title of every book with a 2 star rating

import requests
import bs4

# Base URL template for pagination - {} will be replaced with page numbers
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# List to store all book titles that have 2-star ratings
title_and_ratings = []

# Loop through pages 1 to 50 of the book catalog
for n in range(1, 51):
    
    # Format the base URL with the current page number
    scraped_data = base_url.format(n)

    # Send GET request to fetch the HTML content of the current page
    res = requests.get(scraped_data)
    
    # Parse the HTML content using BeautifulSoup with lxml parser
    soup = bs4.BeautifulSoup(res.text, "lxml")
    
    # Find all book containers on the page using CSS selector
    books = soup.select(".product_pod")
    
    # Iterate through each book container on the current page
    for book in books:
        # Check if the book has a 2-star rating by looking for elements with both "star-rating" and "Two" classes
        if len(book.select(".star-rating.Two")) != 0:
            # Extract book title from the second anchor tag's title attribute
            # Index [1] is used because [0] is the book cover image link, [1] is the title link
            book_title = book.select("a")[1]["title"]
            # Add the book title to our results list
            title_and_ratings.append(book_title)
            

# Print all collected book titles with 2-star ratings
print(title_and_ratings)