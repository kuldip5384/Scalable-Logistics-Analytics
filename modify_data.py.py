import pandas as pd
import numpy as np

df = pd.read_excel("logistics_dataset.xlsx")

df["ETA"] = np.random.randint(1, 10, len(df))
df["ATA"] = df["ETA"] + np.random.randint(0, 5, len(df))
df["Quantity"] = np.random.randint(1, 100, len(df))

df["Date"] = pd.date_range(start="2023-01-01", periods=len(df), freq="D")

df.to_excel("logistics_dataset.xlsx", index=False)

print("✅ Dataset modified successfully!")