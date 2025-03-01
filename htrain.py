import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load preprocessed Hyderabad housing data
df = pd.read_csv("processed_hyderabad_housing.csv")

# Define features (X) and target (y)
X = df.drop(columns=['Price'])  # Drop the target variable
y = df['Price']  # Price is the target

# Save feature names (for later use in API)
feature_order = X.columns.tolist()
pd.Series(feature_order).to_csv("feature_order.csv", index=False)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model performance
score = model.score(X_test, y_test)
print(f"Model R² score: {score:.2f}")

# Save the trained model
joblib.dump(model, 'hyderabad_realestatemodel.pkl')
print("Model saved as hyderabad_realestatemodel.pkl")
