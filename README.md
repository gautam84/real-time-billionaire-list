# 🤑 Real-Time Billionaire List Scraper

This Python script uses **Selenium** and **BeautifulSoup** to scrape the names of the top 200 billionaires from [Forbes Real-Time Billionaires](https://www.forbes.com/real-time-billionaires/).

## 🚀 Features

- Uses `Selenium` to render dynamic JavaScript content
- Parses and extracts names using `BeautifulSoup`
- Scrapes up to the top 200 billionaires in real-time

## 📦 Requirements

- Python 3.7+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gautam84/real-time-billionaire-list.git
   cd real-time-billionaire-list
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```


3. **Download ChromeDriver:**
   - Download from: https://sites.google.com/a/chromium.org/chromedriver/downloads
   - Make sure the ChromeDriver executable is in your system's PATH or in the project folder.

## 🧪 Usage

Run the scraper script:

```bash
python scraper.py
```

It will print the names of the top 200 billionaires to your terminal.

## 📁 File Structure

```
real-time-billionaire-list/
├── scraper.py         # Main scraper script
└── README.md          # Project documentation
```

## 📝 Notes

- This script relies on the structure of the Forbes website. If the site changes, the scraper may need updates.
- Make sure to comply with the website's terms of use.

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify!

---

Happy scraping! 😄