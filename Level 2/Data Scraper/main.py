from scraper import SimpleScraper

def main():
    print("=== Data Scraper ===\n")

    url = input("Enter website URL to scrape: ").strip()
    
    scraper = SimpleScraper(url)
    html = scraper.fetch_page()
    
    if html:
        scraper.parse_page(html)
        scraper.save_to_csv()

    print("\n🎉 Scraping completed!")

if __name__ == "__main__":
    main()