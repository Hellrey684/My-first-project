# Book Scraper & Analysis

Hi everyone! This is my first Python project. I'm learning to become a programmer, and I'm documenting my journey here.

I started learning Python a few months ago. So far, I can:
- Write web scrapers with `requests` + `BeautifulSoup`
- Work with data using `pandas` (cleaning, filtering, grouping)
- Save data to CSV and Excel
- Build simple plots with `matplotlib`
- Write Telegram bots (`pyTelegramBotAPI`)
- Build basic web apps with `Flask`

The README you're reading was written with the help of AI, but the code is mine — I wrote it myself, learned from it, and I'm sharing it to get better.

I'd really appreciate any advice, feedback, or suggestions from more experienced developers. Feel free to open an issue or create a pull request. I'm here to learn.

---

## 📫 Contact

- Telegram: @hellreyyy3
- GitHub: [Hellrey684]((https://github.com/Hellrey684))

A simple Python project that scrapes book data from [Books to Scrape](http://books.toscrape.com/) and performs basic statistical analysis on the collected data.

## 📁 Project Structure
project/
├── books_parser.py # Scrapes book data and saves to CSV
├── books_analysis.py # Reads CSV, cleans data, shows statistics
└── README.md # This file

## 🚀 Features

- **Web Scraping**: Extracts book titles, prices, and ratings from all pages of the catalog.
- **Data Cleaning**: Removes currency symbols and converts prices to numeric values.
- **Analysis**: Calculates minimum, maximum, and median prices.
- **Export**: Saves cleaned data to a new CSV file.

## 🛠️ Tech Stack

- **Python 3**
- `requests` – for making HTTP requests
- `BeautifulSoup4` – for parsing HTML
- `pandas` – for data manipulation and analysis
- `re` – for cleaning price strings

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/book-scraper.git
   cd book-scraper
   Install the required dependencies:
   pip install requests beautifulsoup4 pandas
   ▶️ Usage
1. Run the scraper
 python books_parser.py
This will:

Scrape all books from books.toscrape.com

Save the data to all_books.csv
2. Run the analysis
python books_analysis.py
This will:

Read all_books.csv

Clean the price column (remove £ symbols, convert to float)

Output the cheapest, most expensive, and median prices

Save cleaned data to cleaned_books.csvon books_analysis.py
📊 Example Output
Cheapest book: 10.99
Median price: 35.5
Most expensive book: 57.25
📂 Output Files
all_books.csv – raw scraped data (title, price, rating)

cleaned_books.csv – cleaned data with numeric prices
🤝 Contributing
This is a learning project. Feel free to fork, modify, and use it as a template for your own scraping projects.
