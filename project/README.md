Inflation Impact Analyzer

Description

A price tracking pipeline that automatically scrapes the price of a
product every week, records the history in a CSV, generates a
price evolution chart, and compares the observed change to the
official inflation rate.

Features

* Automatic scraping (BeautifulSoup)
* Persistent history in CSV
* Price evolution chart (matplotlib)
* Comparison with the official inflation rate
* Automated execution every week via GitHub Actions
* Unit tests (pytest)

Main Functions

* fetch_price(url, selector) - scrapes the price from a product page
* load_history(filename, product) - loads the price history
* save_price(filename, product, price) - records a new entry
* compute_price_change(old_price, new_price) - calculates the change in %
* compare_to_official_inflation(price_change, official_rate) - compares with official inflation
* plot_price_history(history, product) - generates a PNG chart

Installation

pip install -r requirements.txt

Usage

python3 project.py huile_1L "https://site-exemple.com/produit/huile" --selector ".price" --plot

Automation

The .github/workflows/scrape.yml file reruns the scraper every Monday
at 9 AM UTC and automatically commits the updated history - no
manual intervention is required once configured.

Finding the Right CSS Selector

Right-click on the displayed price -> “Inspect” -> locate the class/id of
the element -> pass it to --selector.

Scraping Ethics

Check the site’s robots.txt, respect the terms of service, and do not make requests too frequently.

Tests

pytest test_project.py