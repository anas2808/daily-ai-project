# Hey everyone! I'm a fresher and I built a super basic web scraper!
# This script will visit a website, grab some text, and print it out.

# First, we need some tools!
# You'll need to install 'requests' and 'BeautifulSoup4'.
# Open your terminal/command prompt and type:
# pip install requests beautifulsoup4

import requests # This library helps us download web pages from the internet
from bs4 import BeautifulSoup # This library helps us easily read and navigate HTML content

# 1. Define the website we want to scrape
# I picked a website that's specifically designed for practicing web scraping!
target_url = "http://quotes.toscrape.com/"

print(f"Starting the scraper for: {target_url}")
print("-" * 40)

try:
    # 2. Make a request to the website
    # This is like opening a web browser and going to the URL.
    # The 'requests.get()' function tries to fetch the page content.
    response = requests.get(target_url)

    # Check if the request was successful (status code 200 means everything is OK!)
    if response.status_code == 200:
        print("Successfully fetched the page content!")
        
        # 3. Parse the HTML content
        # We use BeautifulSoup to turn the raw HTML text into a Python object
        # that we can easily search through using its methods.
        soup = BeautifulSoup(response.text, 'html.parser')

        # Now, let's find the data we want!
        # On this 'quotes.toscrape.com' site, each quote is wrapped in a <div> tag
        # that has a specific class called "quote".
        # We use 'find_all()' to get a list of all such <div> elements.
        all_quotes_divs = soup.find_all('div', class_='quote')

        print(f"Found {len(all_quotes_divs)} quotes on this page.")
        print("-" * 40)

        # 4. Loop through each found quote and extract the specific text and author
        quote_number = 1
        for quote_div in all_quotes_divs:
            # Inside each 'quote_div', the actual quote text is usually in a <span> tag
            # with the class "text". We find it and use '.get_text()' to grab its content.
            quote_text = quote_div.find('span', class_='text').get_text()
            
            # The author's name is typically in a <small> tag with the class "author".
            # Again, we find it and extract its text.
            author = quote_div.find('small', class_='author').get_text()

            # Print out what we found for each quote!
            print(f"Quote #{quote_number}:")
            print(f"  Text: {quote_text}")
            print(f"  Author: {author}")
            print("-" * 40)
            quote_number += 1

    else:
        # If the status code is not 200, something went wrong with fetching the page.
        print(f"Oops! Couldn't retrieve the page. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # This 'try-except' block helps us handle potential errors.
    # 'RequestException' catches common network errors, like no internet connection,
    # or if the website is unavailable.
    print(f"An error occurred while trying to connect to the website: {e}")
except Exception as e:
    # This is a general catch-all for any other unexpected errors that might occur.
    print(f"An unexpected error occurred during scraping: {e}")

print("\nScraping process finished!")
print("Hope you learned something cool about web scraping!")