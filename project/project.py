import argparse
import csv
import os
from datetime import date

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


HISTORY_FILE = "price_history.csv"
OFFICIAL_ANNUAL_INFLATION_RATE = 4.5


def main():
    parser = argparse.ArgumentParser(description="Suivi de prix et impact inflationniste")
    parser.add_argument("product", help="Nom du produit (ex: 'huile_1L')")
    parser.add_argument("url", help="URL de la page produit a scraper")
    parser.add_argument("--selector", default=".price", help="Selecteur CSS du prix")
    parser.add_argument("--plot", action="store_true", help="Genere un graphique d'evolution")
    args = parser.parse_args()

    current_price = fetch_price(args.url, args.selector)
    print(f"Prix actuel de {args.product} : {current_price:.2f}")

    history = load_history(HISTORY_FILE, args.product)
    save_price(HISTORY_FILE, args.product, current_price)

    if history:
        last_price = history[-1][1]
        change = compute_price_change(last_price, current_price)
        print(f"Evolution depuis le dernier releve ({history[-1][0]}) : {change:+.2f}%")
        print(compare_to_official_inflation(change, OFFICIAL_ANNUAL_INFLATION_RATE))
    else:
        print("Aucun historique - c'est le premier releve pour ce produit.")

    if args.plot:
        full_history = load_history(HISTORY_FILE, args.product)
        plot_price_history(full_history, args.product)


def fetch_price(url, selector):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    element = soup.select_one(selector)
    if element is None:
        raise ValueError(f"Selecteur '{selector}' introuvable sur la page")

    text = element.get_text(strip=True)
    text = text.replace("DH", "").replace("MAD", "").replace(",", ".").strip()
    digits = "".join(c for c in text if c.isdigit() or c == ".")
    return float(digits)


def load_history(filename, product):
    if not os.path.exists(filename):
        return []
    rows = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["product"] == product:
                rows.append((row["date"], float(row["price"])))
    return sorted(rows, key=lambda r: r[0])


def save_price(filename, product, price):
    file_exists = os.path.exists(filename)
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "product", "price"])
        writer.writerow([date.today().isoformat(), product, price])


def compute_price_change(old_price, new_price):
    if old_price == 0:
        raise ValueError("Le prix precedent ne peut pas etre 0")
    return ((new_price - old_price) / old_price) * 100


def compare_to_official_inflation(price_change, official_rate):
    diff = price_change - official_rate
    if diff > 0:
        return (f"Ce produit augmente plus vite que l'inflation officielle "
                f"({diff:+.2f} points d'ecart)")
    elif diff < 0:
        return (f"Ce produit augmente moins vite que l'inflation officielle "
                f"({diff:+.2f} points d'ecart)")
    else:
        return "Ce produit suit exactement l'inflation officielle"


def plot_price_history(history, product):
    """Genere un graphique d'evolution des prix et le sauvegarde en PNG."""
    if len(history) < 2:
        print("Pas assez de donnees pour tracer un graphique (minimum 2 releves).")
        return

    dates = [row[0] for row in history]
    prices = [row[1] for row in history]

    plt.figure(figsize=(8, 4))
    plt.plot(dates, prices, marker="o")
    plt.title(f"Evolution du prix - {product}")
    plt.xlabel("Date")
    plt.ylabel("Prix")
    plt.xticks(rotation=45)
    plt.tight_layout()

    filename = f"{product}_trend.png"
    plt.savefig(filename)
    print(f"Graphique sauvegarde : {filename}")


if __name__ == "__main__":
    main()
