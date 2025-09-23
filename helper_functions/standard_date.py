import pandas as pd

def standardize_dates(df):
    """Standardize date column to YYYY-MM-DD format"""
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    return df