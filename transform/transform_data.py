import pandas as pd

def standardize_dates(df):
    """Standardize date column to YYYY-MM-DD format"""
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    return df

def transform_naivas_data(input_file, output_file):
    """Transform Naivas data with standardized dates"""
    # Read data
    df = pd.read_csv(input_file)
    
    # Standardize dates
    df = standardize_dates(df)
    
    # Save transformed data
    df.to_csv(output_file, index=False)
    print(f"Transformed data saved to {output_file}")
    
    return df

if __name__ == "__main__":
    transform_naivas_data("../data/naivas_full.csv", "../data/naivas_transformed.csv")