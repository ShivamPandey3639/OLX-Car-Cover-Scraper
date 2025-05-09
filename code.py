import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import random

def scrape_olx_car_covers(num_pages=3):
    """
    Scrape car cover listings from OLX and return as a list of dictionaries
    """
    base_url = "https://www.olx.in/items/q-car-cover"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    all_results = []
    
    for page in range(1, num_pages + 1):
        try:
            url = f"{base_url}?page={page}"
            print(f"Scraping page {page}...")
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise exception for 4XX/5XX responses
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all item listings
            item_cards = soup.select('li.EIR5N')
            
            for item in item_cards:
                try:
                    # Extract data from each listing
                    title_elem = item.select_one('span.fcMouD')
                    price_elem = item.select_one('span._2Ks63')
                    location_elem = item.select_one('span._2VQu4')
                    date_elem = item.select_one('span._2DGqt')
                    url_elem = item.select_one('a')
                    
                    title = title_elem.text.strip() if title_elem else "N/A"
                    price = price_elem.text.strip() if price_elem else "N/A"
                    location = location_elem.text.strip() if location_elem else "N/A"
                    date = date_elem.text.strip() if date_elem else "N/A"
                    url = "https://www.olx.in" + url_elem['href'] if url_elem and 'href' in url_elem.attrs else "N/A"
                    
                    # Add to results list
                    all_results.append({
                        'title': title,
                        'price': price,
                        'location': location,
                        'date': date,
                        'url': url
                    })
                    
                except Exception as e:
                    print(f"Error parsing item: {e}")
            
            # Add a small delay to be respectful to the website
            time.sleep(random.uniform(1.0, 2.0))
            
        except Exception as e:
            print(f"Error scraping page {page}: {e}")
    
    return all_results

def save_to_json(data, filename="olx_car_covers.json"):
    """Save scraped data to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

def save_to_csv(data, filename="olx_car_covers.csv"):
    """Save scraped data to a CSV file"""
    if not data:
        print("No data to save")
        return
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    print("Starting OLX car cover scraper...")
    
    # Ask user how many pages to scrape
    try:
        pages = int(input("How many pages to scrape (default is 3): ") or 3)
    except ValueError:
        print("Invalid input, using default of 3 pages")
        pages = 3
    
    # Scrape the data
    results = scrape_olx_car_covers(pages)
    print(f"Found {len(results)} car cover listings")
    
    # Ask user for file format preference
    file_format = input("Save as JSON or CSV? (j/c): ").lower()
    
    if file_format == 'j' or file_format == 'json':
        save_to_json(results)
    else:
        save_to_csv(results)
