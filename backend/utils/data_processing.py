import pandas as pd

def load_data(file_path):
    """Load data from a CSV or JSON file."""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Please use .csv or .json.")

def preprocess_data(df):
    """Perform preprocessing on the DataFrame, like handling missing values."""
    return df.fillna(method='ffill')  # Example: forward fill for missing values
