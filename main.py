import requests
import pandas as pd

def fetch_india_cities():
    url = "https://countriesnow.space/api/v0.1/countries/cities"
    payload = {"country": "India"}
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    data = resp.json()
    if not data.get("error"):
        return data.get("data", [])
    else:
        raise Exception(f"API error: {data.get('msg')}")

def save_to_csv(cities, filename="india_cities.csv"):
    df = pd.DataFrame(cities, columns=["city"])
    df.to_csv(filename, index=False)
    print(f"Saved {len(cities)} cities to {filename}")

if __name__ == "__main__":
    try:
        cities = fetch_india_cities()
        save_to_csv(cities)
    except Exception as e:
        print(f"Error: {e}")
