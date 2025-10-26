import pandas as pd
import os

# ✅ Step 1: Automatically find your raw CSV
raw_folder = r"C:\Users\Kajal Singh\Desktop\Projects\dashboard-task-4\data\raw"
for file in os.listdir(raw_folder):
    if file.endswith(".csv"):
        csv_path = os.path.join(raw_folder, file)
        print("Reading file:", csv_path)
        df = pd.read_csv(csv_path)
        break

# ✅ Step 2: Clean column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# ✅ Step 3: Parse date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# ✅ Step 4: Add year, month, and year-month
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['year_month'] = df['date'].dt.to_period('M').astype(str)

# ✅ Step 5: Handle missing values (drop rows with no date or amount)
df = df.dropna(subset=['date', 'total_amount'])

# ✅ Step 6: Convert numeric columns
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['price_per_unit'] = pd.to_numeric(df['price_per_unit'], errors='coerce')
df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')

# ✅ Step 7: Optional — simulate Profit if not present
if 'profit' not in df.columns:
    df['profit'] = df['total_amount'] * 0.2   # assume 20% profit margin

# ✅ Step 8: Profit Margin
df['profit_margin'] = df['profit'] / df['total_amount']

# ✅ Step 9: Save cleaned data
clean_folder = r"C:\Users\Kajal Singh\Desktop\Projects\dashboard-task-4\data\clean"
os.makedirs(clean_folder, exist_ok=True)
clean_path = os.path.join(clean_folder, "sales_clean.csv")
df.to_csv(clean_path, index=False)

print("\n✅ Cleaned data saved at:", clean_path)
print("Preview of cleaned data:\n", df.head())