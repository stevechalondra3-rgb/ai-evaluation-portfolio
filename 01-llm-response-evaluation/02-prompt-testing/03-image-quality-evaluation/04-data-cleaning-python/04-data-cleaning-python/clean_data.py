import pandas as pd

df = pd.read_csv("sample_data.csv")

df = df.drop_duplicates()
df = df.dropna(how="all")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

df.to_csv("cleaned_data.csv", index=False)

print("Data cleaning completed.")
