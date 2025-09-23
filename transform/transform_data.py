import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from helper_functions.standard_date import standardize_dates
from helper_functions.branches import branch_normalize

def transform_naivas_data(input_file, output_file):
    """Transform Naivas data with standardized dates"""
    # Read data
    df = pd.read_csv(input_file)
    
    # Standardize dates
    df = standardize_dates(df)
    # Normalize branch names
    df = branch_normalize(df)
    # Replace ANON customer IDs with Guest
    full_df['customer_id'] = full_df['customer_id'].replace('ANON', 'Guest')
    
    # Save transformed data
    df.to_csv(output_file, index=False)
    # print(f"Transformed data saved to {output_file}")
    
    return df

if __name__ == "__main__":
    transform_naivas_data("../data/raw_data.csv", "../data/naivas_transformed.csv")