# Inflation Impact Analyzer

![Python](https://img.shields.io/badge/python-3.11-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Automation](https://img.shields.io/badge/automation-GitHub%20Actions-blueviolet)

## Description
A price-tracking pipeline that automatically scrapes a product's price
every week, stores the history in a CSV, generates an evolution chart,
and compares the observed variation to the official inflation rate.

## Features
- Automatic scraping (BeautifulSoup)
- Persistent history in CSV
- Price evolution chart (matplotlib)
- Comparison with the official inflation rate
- Automated weekly execution via GitHub Actions
- Unit tests (pytest)

## Main functions
- `fetch_price(url, selector)` - scrapes the price from a product page
- `load_history(filename, product)` - loads the price history
- `save_price(filename, product, price)` - saves a new price reading
- `compute_price_change(old_price, new_price)` - computes the % variation
- `compare_to_official_inflation(price_change, official_rate)` - compares to official inflation
- `plot_price_history(history, product)` - generates a PNG chart

## Installation
```bash
pip install -r requirements.txt

## Usage
python3 project.py huile_1L "https://site-exemple.com/produit/huile" --selector ".price" --plot

## Automation 
The .github/workflows/scrape.yml file reruns the scraper every Monday
at 9am UTC and automatically commits the updated history - no manual
intervention needed once set up.

## Finding the right CSS selector
Right-click the displayed price -> "Inspect" -> find the element's
class/id -> pass it as --selector.

## Scraping ethics
Check the site's robots.txt, respect the terms of service, don't send
requests too frequently.

## Tests
pytest test_project.py
