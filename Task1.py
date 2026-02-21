import dask.dataframe as dd

# ✅ Load CSV file (use your file name here)
df = dd.read_csv('data.csv', assume_missing=True)

# ✅ Show column names
print("📌 Columns in the dataset:")
print(df.columns)

# ✅ Approximate row count (Dask works lazily)
print("\n📌 Approximate number of rows:")
print(len(df))

# ✅ Basic statistics
print("\n📊 Dataset Description:")
print(df.describe().compute())

# ✅ Check null values
print("\n🔍 Missing Values in each column:")
print(df.isnull().sum().compute())

# ✅ Example: Value counts for 'payment_type' (edit column name as needed)
if 'payment_type' in df.columns:
    print("\n📈 Value counts for 'payment_type':")
    print(df['payment_type'].value_counts().compute())

# ✅ Example: Average fare_amount (edit column name as needed)
if 'fare_amount' in df.columns:
    print("\n💵 Average Fare Amount:")
    print(df['fare_amount'].mean().compute())

# ✅ Example: Trip Distance summary
if 'trip_distance' in df.columns:
    print("\n🚕 Trip Distance Summary:")
    print("Max:", df['trip_distance'].max().compute())
    print("Min:", df['trip_distance'].min().compute())
    print("Mean:", df['trip_distance'].mean().compute())
