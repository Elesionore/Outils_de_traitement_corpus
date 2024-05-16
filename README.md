# Etape 1. Quel corpus me plaît ? Sa carte.

J’ai trouvé un corpus qui m’a inspiré ici : https://www.kaggle.com/datasets/aladzuzamar/hotels-accommodation-prices-dataset 

<b>Pourquoi ce corpus ?</b>
<br>Il y a 3 ans que je travaille sur la localisation du website qui s'occupe de réservation d'hôtels.


* Nom : Hotels
* Auteur : Amar Aladžuz
* Taille : 1224 mots, 14,9 KiB
* Format : xlsx
* Langue : Anglais
* Categories : ID, Hotel name, Price, Hotel star rating, Distance, Customer rating, Rooms, Squares, City
* Source : www.booking.com
* Mis à jour : 2021
* Modalité : ecrit
* Licence : Data files © Original Authors

# Etape 2. Organiser les dossiers. Scrapper le Web.

Dossiers qui seront sur mon repo :

* scripts
	* extract_information.py
	* tranform_to_table.py
* data
	* corpus brut
	* corpus nettoyé
* figures
	* fichier csv
* src
	* graphiques
* LICENSE
* README.md

Peut-etre, je vais changer quelque chose plus tard.

J’ai fait un script scrape_all.py pour récupérer tout le contenu du 5 liens. J’ai scrappé le contenu du site booked.net, concrètement https://www.booked.net/hotels/france/paris, https://www.booked.net/hotels/us/ny/new-york, https://www.booked.net/hotels/china/shanghai, https://www.booked.net/hotels/spain/barcelona, https://www.booked.net/hotels/philippines/manila. Les fichiers txt obtenus j'ai sauvegardé dans le dossier data >> corpus brut.

Et encore deux scripts python pour obtenir le corpus nettoyé et le transformer en xlsx: extract_information.py en utilisant BeautifulSoup et tranform_to_table.py. Les fichiers seront dans le dossier corpus nettoyé.

Il y  certaines différences entre les catégories extraites par moi et par l’auteur du corpus pré-existant.

Ses categories : ID, Hotel name, Price(BAM), Hotel star rating,	Distance, Customer rating, Rooms, Squares, City

Mes categories : name, stars, price, description, city, country, ratingValue, ratingCount

Pourquoi ? Car le corpus de référence ont utilisé booking.com, et j’ai utilisé booked.net. Les informations sur 2 sites se diffèrent.

Aussi j'ai rédigé LICENSE selon le modèle trouvé sur Internet.
