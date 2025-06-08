import pandas as pd
import os

# Setup paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'sample_general_ledger.xlsx')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data
def load_data(path):
    print(f"📂 Loading data from: {path}")
    return pd.read_excel(path)

# Anomaly detection functions
def detect_duplicates(df):
    return df[df.duplicated()]

def detect_large_round_values(df, column='Amount', threshold=10000):
    return df[(df[column] % 1000 == 0) & (df[column].abs() >= threshold)]

def detect_small_splits(df, column='Amount', limit=5000):
    return df[df[column].abs() < limit]

def detect_manual_entries(df):
    return df[df['EntryType'].str.lower() == 'manual']

# Save to Excel
def export_to_excel(df, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    df.to_excel(path, index=False)
    print(f"✅ Exported: {filename}")

if __name__ == "__main__":
    df = load_data(DATA_PATH)

    df_duplicates = detect_duplicates(df)
    df_large_rounds = detect_large_round_values(df)
    df_small_values = detect_small_splits(df)
    df_manual = detect_manual_entries(df)

    export_to_excel(df_duplicates, "duplicates.xlsx")
    export_to_excel(df_large_rounds, "large_rounds.xlsx")
    export_to_excel(df_small_values, "small_values.xlsx")
    export_to_excel(df_manual, "manual_entries.xlsx")