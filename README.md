# Etape 1. Quel corpus me plaît ? Sa carte.

J’ai trouvé un corpus qui m’a inspiré ici : https://www.kaggle.com/datasets/aladzuzamar/hotels-accommodation-prices-dataset 

<b>Pourquoi ce corpus ?</b>
<br>Il y a 3 ans que je travaille sur la localisation du website qui s'occupe de réservation d'hôtels, concrètement booked.net.

Carte du corpus de référence :

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
	* scrape_all.py
	* extract_information.py
	* tranform_to_table.py
	* xlsx_to_csv.py
	* create_datasets.ipynb
* data
	* corpus brut
	* corpus nettoyé
* figures
	* métriques, statistiques
* src
	* données de Docker
* LICENSE
* README.md

Peut-etre, je vais changer quelque chose plus tard. (oui, j'ai changé le contenu en ajoutant les nouveaux fichiers)

J’ai fait un script scrape_all.py pour récupérer tout le contenu brut du 5 liens.

J’ai scrappé le contenu du site booked.net, concrètement https://www.booked.net/hotels/france/paris, https://www.booked.net/hotels/us/ny/new-york, https://www.booked.net/hotels/china/shanghai, https://www.booked.net/hotels/spain/barcelona, https://www.booked.net/hotels/philippines/manila. Les fichiers txt obtenus j'ai sauvegardé dans le dossier data >> corpus brut.

Et encore deux scripts python pour scrapper seulement les colonnes qui m'intèressent et les transformer en xlsx: extract_information.py en utilisant BeautifulSoup et tranform_to_table.py. Les fichiers seront dans le dossier corpus nettoyé.

Il y  certaines différences entre les catégories extraites par moi et par l’auteur du corpus pré-existant.

Ses categories : ID, Hotel name, Price(BAM), Hotel star rating,	Distance, Customer rating, Rooms, Squares, City

Mes categories : name, stars, price, description, city, country, ratingValue, ratingCount

Pourquoi ? Car le corpus de référence ont utilisé booking.com, et j’ai utilisé booked.net. Les informations sur 2 sites se diffèrent un peu.

Aussi j'ai rédigé LICENSE selon le modèle trouvé sur Internet.

Enfin j'ai créé le script xlsx_to_csv.py pour pouvoir traiter mes données dans les formats différents.

# Etape 3. Création de datasets. Carte de mon corpus.

J’ai lancé un petit code nommé create_datasets.ipynb sur Notebook :

```
import pandas as pd
df = pd.read_csv('hotels_data.csv')
from datasets import Dataset
dataset = Dataset.from_pandas(df)
output_directory = "/home/miya/Downloads/"
dataset.save_to_disk(output_directory)
```

Comme résultat, j’ai obtenu 3 fichiers :
state.json
dataset_info.json
data-00000-of-00001.arrow

Je les ai sauvegardés dans un dossier src.

Carte de mon corpus:

* Nom : hotels_data
* Auteur : Solomiia Korol
* Taille : 25439 mots, 174,1 KiB
* Format : txt, xlsx, csv
* Langue : Anglais
* Categories : name, stars, price, description, city, country, ratingValue, ratingCount
* Source : http://booked.net
* Mis à jour : 2024
* Modalité : ecrit
* Licence : CC BY-NC-SA (Attribution-NonCommercial-ShareAlike)

# Etape 4. Installer et essayer Docker

J’ai installé docker avoir lancé ces commandes :

```
sudo apt update
sudo apt upgrade -y
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce -y
sudo systemctl status docker
sudo usermod -aG docker $USER
```

Puis j’ai crée Dockerfile en utilisant l’image Ubuntu selon les instructions des cours et de notre chat de groupe.

Commandes utiles :

```
sudo docker build -t my_ubuntu_ssh .
sudo docker run -d -p 2222:22 my_ubuntu_ssh
ssh root@localhost -p 2222
sudo docker ps     #ici on peut voir CONTAINER ID
sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id>
```

J’ai trouvé et testé plusieurs commandes quoi faire dans docker :

```
# Vérifier l'état du service SSH
service ssh status

# Redémarrer le service SSH
service ssh restart

# Vérifier les logs SSH pour des erreurs
cat /var/log/auth.log

# Vérifier la configuration du serveur SSH
cat /etc/ssh/sshd_config

# S'assurer que le mot de passe root est défini correctement
echo 'root:root' | chpasswd

# Quitter le conteneur
exit
```

Conclusion 1: Il fallait de sauvegarder Container ID, key fingerprint, my_ubuntu _ssh !!!!

Conclusion 2: Sans sudo les commandes ne marchent pas, il faut être superuser. :)

Conclusion 3: Docker c'est pas facile.



