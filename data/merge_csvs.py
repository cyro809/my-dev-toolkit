import pandas as pd
import glob

files = glob.glob("./csvs/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)
    all_data.append(df)

merged = pd.concat(all_data, ignore_index=True)

merged.to_csv("merged.csv", index=False)