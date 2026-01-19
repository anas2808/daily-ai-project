import requests
from bs4 import BeautifulSoup
import logging


def fetch_webpage(url):
    """
    Fetches the content of a webpage.
    
    :param url: URL of the webpage to scrape
    :return: HTML content of the webpage if successful, None otherwise
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching the webpage: {e}")
        return None


def parse_html(html_content):
    """
    Parses HTML content and extracts data.
    
    :param html_content: HTML content of a webpage
    :return: Extracted data (for example, all text from <p> tags)
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')
    return [p.get_text() for p in paragraphs]


def main():
    """
    Main function to execute the web scraping.
    """
    logging.basicConfig(level=logging.INFO)
    url = 'https://www.example.com'  # Replace with the target website
    logging.info(f"Fetching webpage: {url}")
    
    html_content = fetch_webpage(url)
    if html_content:
        logging.info("Parsing HTML content")
        data = parse_html(html_content)
        
        if data:
            logging.info("Extracted data:")
            for paragraph in data:
                logging.info(paragraph)
        else:
            logging.warning("No data extracted from the HTML content.")
    else:
        logging.error("Failed to retrieve the webpage content.")


if __name__ == "__main__":
    main()