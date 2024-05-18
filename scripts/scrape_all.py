import requests
from bs4 import BeautifulSoup
import os

def scrape_all_content_as_text(urls, output_dir):
    """
    Récupère tout le contenu texte à partir des URL fournies et l'enregistre dans des fichiers texte.

    Args:
        urls (list): Liste des URL à partir desquelles récupérer le contenu texte.
        output_dir (str): Répertoire de sortie où enregistrer les fichiers texte.

    Returns:
        None
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extraire le titre de la page et le formater comme nom de fichier
            title = soup.title.string if soup.title else 'no_title'
            safe_title = ''.join(e for e in title if e.isalnum() or e in (' ', '_')).rstrip()
            filename = f"{safe_title}.txt"
            filepath = os.path.join(output_dir, filename)

            # Extraire tout le contenu texte de la page
            text_content = soup.get_text(separator='\n')

            # Enregistrer le contenu texte dans un fichier
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(text_content)

            print(f"Le contenu texte de {url} a été enregistré sous {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"Impossible de récupérer {url} : {e}")

if __name__ == "__main__":
    urls = [
        "https://www.booked.net/hotels/france/paris",
        "https://www.booked.net/hotels/us/ny/new-york",
        "https://www.booked.net/hotels/china/shanghai",
        "https://www.booked.net/hotels/spain/barcelona",
        "https://www.booked.net/hotels/philippines/manila"
    ]
    output_directory = "scraped_text_content"

    scrape_all_content_as_text(urls, output_directory)
