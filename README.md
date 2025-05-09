# OLX Car Cover Scraper

A Python-based web scraper that extracts car cover listings from OLX India and exports the data to JSON or CSV format.

## 📋 Overview

This tool automates the process of searching for car covers on OLX India (`www.olx.in`), extracting important details from product listings including title, price, location, date listed, and product URL. The data can be exported to either JSON or CSV format for further analysis or processing.

## ✨ Features

- Multi-page scraping capability
- Customizable number of pages to scrape
- Extracts key listing information:
  - Product title
  - Price
  - Location
  - Date posted
  - Product URL
- Export options:
  - JSON format (for data processing)
  - CSV format (for spreadsheet analysis)
- Built-in rate limiting to respect the website's servers
- Error handling for robust operation

## 🔧 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/olx-car-cover-scraper.git
   cd olx-car-cover-scraper
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the script using Python:

```bash
python olx_scraper.py
```

Follow the interactive prompts:
1. Enter the number of pages to scrape (default is 3)
2. Choose your preferred output format (JSON or CSV)

The results will be saved in the current directory as either `olx_car_covers.json` or `olx_car_covers.csv`.

## 📄 Sample Output

### JSON Format
```json
[
    {
        "title": "Universal Car Body Cover",
        "price": "₹1,499",
        "location": "Delhi, Delhi",
        "date": "Today",
        "url": "https://www.olx.in/item/universal-car-body-cover-ID2nXXX"
    },
    {
        "title": "Premium Car Cover for Maruti Suzuki Swift",
        "price": "₹899",
        "location": "Mumbai, Maharashtra",
        "date": "Yesterday",
        "url": "https://www.olx.in/item/premium-car-cover-for-maruti-suzuki-swift-ID2mYYY"
    }
]
```

### CSV Format
The CSV file will contain columns for title, price, location, date, and URL.

## ⚠️ Disclaimer

This scraper is for educational purposes only. Before scraping any website, please review their Terms of Service. Use this tool responsibly and consider the following:

- Set reasonable delays between requests
- Don't overload the server with too many requests
- Be mindful of the website's robots.txt file
- Consider using the official OLX API if available

## 📦 Dependencies

- Python 3.6+
- requests
- beautifulsoup4

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
