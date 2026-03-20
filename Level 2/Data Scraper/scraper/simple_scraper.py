"""Simple scraper implementation used by the top-level package API."""

import time
import requests
from bs4 import BeautifulSoup

from .file_handler import FileHandler


class SimpleScraper:
    """Basic web scraper.

    The class is intentionally small and designed to work with the sample
    `main.py` script in this repository.
    """

    def __init__(self, url: str, selector: str = "a", max_pages: int = 1, delay: float = 1.0):
        self.url = url
        self.selector = selector
        self.max_pages = max_pages
        self.delay = delay
        self.data = []

    def fetch_page(self, url: str | None = None) -> str | None:
        """Download a page and return the HTML content."""
        if url is None:
            url = self.url

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as exc:
            print(f"❌ Error fetching {url}: {exc}")
            return None

    def parse_page(self, html: str) -> None:
        """Parse the given HTML and extract items matching `self.selector`."""
        soup = BeautifulSoup(html, "html.parser")
        elements = soup.select(self.selector)
        for el in elements:
            text = el.get_text(strip=True)
            link = el.get("href") if el.has_attr("href") else ""
            self.data.append({"text": text, "link": link})

    def save_to_csv(self, filename: str = "scraped_data.csv") -> None:
        """Save scraped data to a CSV file."""
        FileHandler.save_to_csv(self.data, filename)

    def save_to_json(self, filename: str = "scraped_data.json") -> None:
        """Save scraped data to a JSON file."""
        FileHandler.save_to_json(self.data, filename)

    # Backwards compatibility
    def save_data(self, csv_file: str = "scraped_data.csv", json_file: str = "scraped_data.json") -> None:
        self.save_to_csv(csv_file)
        self.save_to_json(json_file)
