import os, pandas as pd

# Automatically detect file inside the raw folder
base = r"C:\Users\Kajal Singh\Desktop\Projects\dashboard-task-4\data\raw"
for file in os.listdir(base):
    if file.endswith(".csv"):
        csv_path = os.path.join(base, file)
        print("Reading file:", csv_path)
        df = pd.read_csv(csv_path, nrows=1000)
        print(df.head())
        break