import pandas as pd

def xlsx_to_csv(input_file, output_file):
    try:
        df = pd.read_excel(input_file)

        df.to_csv(output_file, index=False)

        print(f"Conversion successful. CSV file saved as '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = "hotels_data.xlsx"  
    output_file = "hotels_data.csv"  

    xlsx_to_csv(input_file, output_file)
