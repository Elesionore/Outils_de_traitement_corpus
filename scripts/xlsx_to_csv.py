import pandas as pd

def xlsx_to_csv(input_file, output_file):
    """
    Convertit un fichier Excel (.xlsx) en fichier CSV (.csv).

    Args:
        input_file (str): Chemin du fichier Excel à convertir.
        output_file (str): Chemin du fichier CSV de sortie.

    Raises:
        Exception: Si une erreur survient lors de la conversion.

    Returns:
        None
    """
    try:
        df = pd.read_excel(input_file)
        df.to_csv(output_file, index=False)
        print(f"Conversion réussie. Fichier CSV enregistré sous '{output_file}'.")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    input_file = "hotels_data.xlsx"  
    output_file = "hotels_data.csv"  

    xlsx_to_csv(input_file, output_file)

