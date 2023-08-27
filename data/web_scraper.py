# scraper.py

import requests
from bs4 import BeautifulSoup


def scrape_amazon_ir_page():
    url = "https://ir.aboutamazon.com/annual-reports-proxies-and-shareholder-letters/default.aspx"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        print(soup.prettify())

        # Extract all the links from the page
        links = [a["href"] for a in soup.find_all("a", href=True) if a.text]

        # Print the links
        for link in links:
            print(link)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


if __name__ == "__main__":
    scrape_amazon_ir_page()
