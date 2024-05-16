#extract_information.py
import requests
from bs4 import BeautifulSoup
import json

def extract_hotels_data(urls):
    all_hotels = []

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        hotels = []
        hotel_scripts = soup.find_all('script', type='application/ld+json')

        for script in hotel_scripts:
            hotel_data = {}
            data = json.loads(script.text)
            hotel_data['name'] = data.get('name')
            hotel_data['starRating'] = data.get('starRating')
            hotel_data['priceRange'] = data.get('priceRange')
            hotel_data['description'] = data.get('description')

            address = data.get('address')
            if address:
                hotel_data['addressLocality'] = address.get('addressLocality')
                hotel_data['addressCountry'] = address.get('addressCountry')

            aggregate_rating = data.get('aggregateRating')
            if aggregate_rating:
                hotel_data['ratingValue'] = aggregate_rating.get('ratingValue')
                hotel_data['ratingCount'] = aggregate_rating.get('ratingCount')

            hotels.append(hotel_data)

        all_hotels.extend(hotels)

    return all_hotels


if __name__ == "__main__":
    # N'OUBLIEZ PAS DE METTRE ICI LES LIENS ACTUELS
    urls = [
        "https://www.booked.net/hotels/france/paris",
        "https://www.booked.net/hotels/us/ny/new-york",
        "https://www.booked.net/hotels/china/shanghai",
        "https://www.booked.net/hotels/spain/barcelona",
        "https://www.booked.net/hotels/philippines/manila"
    ]

    hotels_data = extract_hotels_data(urls)
    for hotel in hotels_data:
        print(hotel)
