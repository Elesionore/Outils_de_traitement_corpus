import extract_information
import pandas as pd

# Liste de liens
urls = [
    "https://www.booked.net/hotels/france/paris",
    "https://www.booked.net/hotels/us/ny/new-york",
    "https://www.booked.net/hotels/china/shanghai",
    "https://www.booked.net/hotels/spain/barcelona",
    "https://www.booked.net/hotels/philippines/manila"
]

# appel de extract_information.py
hotels_data = extract_information.extract_hotels_data(urls)

# convertir en DataFrame
df = pd.DataFrame(hotels_data)

# renommer les colonnes
df.rename(columns={'starRating': 'stars', 'priceRange': 'price', 'addressLocality': 'city', 'addressCountry': 'country'}, inplace=True)
output_file_path = "hotels_data.xlsx"
df.to_excel(output_file_path, index=False)

print(f"Data has been successfully saved to {output_file_path}")
