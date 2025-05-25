import pandas as pd
import os

def load_dataset(platform):
    filename_map = {
        "Instagram": "instagram_cleaned.csv",
        "Threads": "threads_cleaned.csv",
    }

    filename = filename_map.get(platform)
    if filename is None:
        raise ValueError(f"Platform '{platform}' tidak dikenali.")

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "fix"))
    full_path = os.path.join(base_dir, filename)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Dataset untuk platform '{platform}' tidak ditemukan di path: {full_path}")

    return pd.read_csv(full_path)


def filter_by_niche(df, niche):
    return df[df["TOPIC_CATEGORY"] == niche]


def prepare_knapsack_data(df):
    value = df["BENEFIT_SCORE"].tolist()
    cost = df["ESTIMATED_COST"].tolist()
    return value, cost
