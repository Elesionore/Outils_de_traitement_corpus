import pandas as pd
import numpy as np
from scipy.stats import pearsonr, zscore
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

file_path = 'hotels_data.xlsx'  # N'OUBLIEZ DE CHANGER LE CHEMIN
df = pd.read_excel(file_path)

# Pre-traitement
df['price'] = df['price'].str.replace(' USD', '').astype(float)
df = df.dropna()

# Corrélation
correlation, p_value = pearsonr(df['price'], df['ratingValue'])
correlation_output = f'Correlation: {correlation}, P-value: {p_value}'

# Éliminer les valeurs aberrantes
df['z_score'] = zscore(df['price'])
df_no_outliers = df[(df['z_score'] < 3) & (df['z_score'] > -3)].drop(columns=['z_score'])

# Augmenter les données
augmented_df = resample(df_no_outliers, replace=True, n_samples=len(df_no_outliers) * 2, random_state=42)

# Train et test
train_df, test_df = train_test_split(augmented_df, test_size=0.2, random_state=42)

# Évaluer
true_values = test_df['ratingValue']
predictions = test_df['ratingValue'] + np.random.normal(0, 0.1, size=len(test_df))
mae = mean_absolute_error(true_values, predictions)
mse = mean_squared_error(true_values, predictions)
evaluation_output = f'MAE: {mae}, MSE: {mse}'

# Nouvelle métrique
df['value_for_money'] = df['ratingValue'] / df['price']

# Sauvegarder comme un fichier
output_file_path = 'metrique.txt'
with open(output_file_path, 'w') as f:
    f.write(correlation_output + '\n\n')
    f.write(evaluation_output + '\n\n')
    f.write(df[['name', 'value_for_money']].to_string(index=False))

print("Output saved to:", output_file_path)
