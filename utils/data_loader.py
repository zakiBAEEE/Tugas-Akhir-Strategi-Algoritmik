import pandas as pd
import os

def load_dataset(platform: str):
    path = os.path.join('data', 'fix', f'{platform}_cleaned.csv')
    return pd.read_csv(path)

def prepare_knapsack_data(df):
    costs = df['estimated_cost'].values
    values = df['profit_score'].values
    return costs, values
