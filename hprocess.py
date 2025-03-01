import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load Hyderabad dataset
df = pd.read_csv("hyderabad_housing_data.csv")

# Debug: Print columns
print("Columns in DataFrame:", df.columns)

# Fill missing numeric values using the median for numeric columns only
numeric_cols = ['Price', 'BHK', 'Square Feet']
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Optionally, fill missing categorical values (if any) with a placeholder or the mode
categorical_cols = ['Title', 'Location']
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# One-Hot Encode only the categorical columns
df = pd.get_dummies(df, columns=['Title', 'Location'])

# Debug: Check data after encoding
print("Data after encoding:")
print(df.head())

# Normalize numeric features: BHK and Square Feet (Price is likely your target)
scaler = StandardScaler()
df[['BHK', 'Square Feet']] = scaler.fit_transform(df[['BHK', 'Square Feet']])

# Save the preprocessed dataset
df.to_csv("processed_hyderabad_housing.csv", index=False)
print("Preprocessing complete. Data saved to processed_hyderabad_housing.csv.")
