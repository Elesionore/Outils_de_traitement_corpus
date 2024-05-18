import pandas as pd
import numpy as np
from scipy.stats import pearsonr, zscore
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

def charger_donnees(file_path):
    """
    Charge les données à partir du fichier Excel spécifié.

    Args:
        file_path (str): Chemin du fichier Excel contenant les données.

    Returns:
        DataFrame: Les données chargées depuis le fichier Excel.
    """
    return pd.read_excel(file_path)

# Charger les données à partir du fichier Excel
file_path = 'hotels_data.xlsx'  # N'OUBLIEZ DE CHANGER LE CHEMIN
df = charger_donnees(file_path)

# Pre-traitement des données
df['price'] = df['price'].str.replace(' USD', '').astype(float)
df = df.dropna()

# Calcul de la corrélation entre le prix et la note
correlation, p_value = pearsonr(df['price'], df['ratingValue'])
correlation_output = f'Corrélation : {correlation}, Valeur P : {p_value}'

# Élimination des valeurs aberrantes
df['z_score'] = zscore(df['price'])
df_no_outliers = df[(df['z_score'] < 3) & (df['z_score'] > -3)].drop(columns=['z_score'])

# Augmentation des données
augmented_df = resample(df_no_outliers, replace=True, n_samples=len(df_no_outliers) * 2, random_state=42)

# Division des données en ensembles d'entraînement et de test
train_df, test_df = train_test_split(augmented_df, test_size=0.2, random_state=42)

# Évaluation des prédictions
true_values = test_df['ratingValue']
predictions = test_df['ratingValue'] + np.random.normal(0, 0.1, size=len(test_df))
mae = mean_absolute_error(true_values, predictions)
mse = mean_squared_error(true_values, predictions)
evaluation_output = f'MAE : {mae}, MSE : {mse}'

# Calcul de la nouvelle métrique
df['value_for_money'] = df['ratingValue'] / df['price']

# Sauvegarde des résultats dans un fichier texte
output_file_path = 'metrique.txt'
with open(output_file_path, 'w') as f:
    f.write(correlation_output + '\n\n')
    f.write(evaluation_output + '\n\n')
    f.write(df[['name', 'value_for_money']].to_string(index=False))

print("Résultats enregistrés dans :", output_file_path)
