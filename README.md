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
	* evaluation.py
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

# Etape 4. Installer et essayer Docker.

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

# Etape 5. Script pour évaluer, mesurer, faire une métrique.

Le script evaluation.py est dans le dossier ‘scripts’, le output est dans le dossier ‘figures’.

Ce script a pris une éternité a accomplir. J’ai reçu bcp d’erreurs et tous que j’ai fait comme ‘pré-traitement’ était fait comme la résolution pourquoi je vois ‘TypeError: unsupported operand type(s) for +: 'float' and 'str' ou ‘ValueError: array must not contain infs or NaNs’ ou ‘TypeError: ufunc 'isinf' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''.

## Pré-traitement
 J'ai commencé par charger les données depuis un fichier hotels_data.xlsx. Ensuite, j'ai nettoyé les données en supprimant la devise "USD" de la colonne des prix et en convertissant ces valeurs en type numérique (float). J'ai également supprimé les lignes contenant des valeurs manquantes (NaN) pour éviter des erreurs dans les analyses.

## Corrélation
Je voudrais comprendre la relation entre les prix des chambres d'hôtel et les notes attribuées par les clients. Pour déterminer si une relation significative existe entre cles prix et les notes, j'ai mesuré la corrélation entre ces deux variables en utilisant la fonction pearsonr de la bibliothèque scipy (vues en cours).

## Éliminez les données aberrantes
Je souviens qu’il faut éliminer les valeurs aberrantes, donc j'ai conservé uniquement les prix dont le score z était compris entre -3 et 3.

## Augmenter
Afin de renforcer mon jeu de données, j'ai utilisé la méthode de rééchantillonnage pour doubler le nombre de lignes sans valeurs aberrantes.

## Test et train
J'ai divisé les données augmentées en deux ensembles : un ensemble d'entraînement et un ensemble de test. J'ai utilisé la fonction train_test_split avec un ratio de 80% pour l'entraînement et 20% pour le test.

## Evaluation
Pour évaluer mes données, j'ai généré des prédictions d'exemple en ajoutant une petite perturbation normale aux notes réelles des clients. J'ai ensuite calculé l'erreur absolue moyenne (MAE) et l'erreur quadratique moyenne (MSE) entre les valeurs réelles et les prédictions.

## Nouvelle metrique
Enfin, j'ai proposé une nouvelle métrique appelée "value_for_money" (rapport qualité-prix). Cette métrique est le rapport entre la note des clients et le prix de la chambre. Elle permet de comparer la satisfaction des clients par rapport au coût de leur séjour.

## Interprétations des résultats

Bien, le coefficient de corrélation entre les colonnes 'price' (prix) et 'ratingValue' (note) est d'environ 0,134. C’est une corrélation positive faible, donc quand le prix des hôtels augmente, il y a tendance à ce que les notes augmentent légèrement également.

La valeur p associée à ce coefficient de corrélation est d'environ 0,003. Cela suggère que la corrélation est statistiquement significative, ce qui signifie qu'il est peu probable qu'elle se soit produite par hasard.

Erreur absolue moyenne (MAE) est d'environ 0,084. Il mesure la différence absolue moyenne entre les valeurs prédites et réelles. Erreur quadratique moyenne (MSE) est 0,011. Le MSE montre la moyenne des carrés des erreurs.

La colonne 'value_for_money' représente une mesure de la valeur perçue pour l'argent de chaque hôtel. On peux l’obtenir en divisant la note par le prix. Des valeurs plus élevées indiquent une meilleure valeur perçue pour l'argent.

Bonne nouvelle ! Je peux voir quels hôtels pourraient offrir meilleur rapport qualité-prix. Et je vais l’utiliser cet info pour planifier les vacances. :)

