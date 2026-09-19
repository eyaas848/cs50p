# Analyseur d'Impact Inflationniste

![Python](https://img.shields.io/badge/python-3.11-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Automation](https://img.shields.io/badge/automation-GitHub%20Actions-blueviolet)

## Description
Un pipeline de suivi de prix qui scrape automatiquement le prix d'un
produit chaque semaine, enregistre l'historique dans un CSV, genere un
graphique d'evolution, et compare la variation observee au taux
d'inflation officiel.

## Fonctionnalites
- Scraping automatique (BeautifulSoup)
- Historique persistant en CSV
- Graphique d'evolution des prix (matplotlib)
- Comparaison avec le taux d'inflation officiel
- Execution automatisee chaque semaine via GitHub Actions
- Tests unitaires (pytest)

## Fonctions principales
- `fetch_price(url, selector)` - scrape le prix d'une page produit
- `load_history(filename, product)` - charge l'historique des prix
- `save_price(filename, product, price)` - enregistre un nouveau releve
- `compute_price_change(old_price, new_price)` - calcule la variation en %
- `compare_to_official_inflation(price_change, official_rate)` - compare a l'inflation officielle
- `plot_price_history(history, product)` - genere un graphique PNG

## Installation
```bash
pip install -r requirements.txt
```

## Utilisation
```bash
python3 project.py huile_1L "https://site-exemple.com/produit/huile" --selector ".price" --plot
```

## Automatisation
Le fichier `.github/workflows/scrape.yml` relance le scraper chaque lundi
a 9h UTC et commit automatiquement l'historique mis a jour - aucune
intervention manuelle necessaire une fois configure.

## Trouver le bon selecteur CSS
Clic droit sur le prix affiche -> "Inspecter" -> repere la classe/id de
l'element -> passe-la en `--selector`.

## Ethique du scraping
Verifie le `robots.txt` du site, respecte les CGU, ne fais pas de requetes trop frequentes.

## Tests
```bash
pytest test_project.py
```
