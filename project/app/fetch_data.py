import requests
from app.models import Country

def fetch_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch data")
        return

    countries = response.json()
    for c in countries:
        name = c.get("name", {}).get("common", "Unknown")
        population = c.get("population", 0)
        region = c.get("region", "")
        subregion = c.get("subregion", "")
        capital = c.get("capital", [""])[0] if c.get("capital") else ""

        Country.objects.get_or_create(
            name=name,
            defaults={
                "population": population,
                "region": region,
                "subregion": subregion,
                "capital": capital
            }
        )
    print("Data fetching completed.")
