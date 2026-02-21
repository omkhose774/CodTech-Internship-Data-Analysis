import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data.csv') 

# Show basic info
print(df.head())
print(df.info())

# Drop datetime and unused columns
df = df.drop(columns=[
    'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'store_and_fwd_flag'
])

# Drop any missing values just to simplify (optional)
df = df.dropna()

# Define features (X) and target (y)
X = df.drop(columns=['total_amount'])  # Features
y = df['total_amount']                 # Target

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model Training
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n✅ Mean Squared Error: {mse:.2f}")
print(f"✅ R² Score: {r2:.2f}")
