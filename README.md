# Books Data Scraper

## Overview
This repository contains a Python script that performs web scraping on the Books to Scrape website to collect book details. The scraper extracts information like book titles, prices, availability, and more. This data is then stored in a structured format (books_data.csv), which can be used for further analysis or integration with other projects.

## Features

-**Web Scraping**: Scrapes book data from all pages of the Books to Scrape website.

-**Data Collection**: Extracts book titles, prices, availability, and other relevant information.

-**CSV Export**: Saves the extracted data in a CSV file (books_data.csv).

-**Efficient**: Handles multiple pages of data extraction.

## Installation

To get started with the project, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/mitali-ops/web-scraping.git
cd web-scraping
```

Make sure you have the following Python packages installed:

```bash
pip install requests beautifulsoup4 pandas
```
## Usage
**1. Clone the repository**:

```bash
git clone https://github.com/mitali-ops/web-scraping.git
cd web-scraping
```

**2. Run the scraper**:

After setting up the environment, you can run the books_scraper.py script to start scraping the data:

```bash
python books_scraper.py
```

**3. Check the output**:

Once the script completes, the scraped data will be saved in a CSV file (books_data.csv).

## Files in this Repository

books_scraper.py: The Python script used for scraping book data from the website.

books_data.csv: The CSV file that contains the scraped data (titles, prices, availability, etc.).

## Technologies Used

**Python**

**BeautifulSoup**: For parsing HTML and scraping content.

**Requests**: For making HTTP requests to fetch web pages.

**Pandas**: For handling and saving the scraped data in CSV format.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. Please make sure to follow good practices by writing clean and maintainable code.

1. Fork the repository
2. Create your feature branch (git checkout -b feature-name)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature-name)
5. Open a pull request
