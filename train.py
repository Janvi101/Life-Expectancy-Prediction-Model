import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load data
df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()

# Select features
features = ['Schooling', 'Income composition of resources', 'Adult Mortality', 'BMI', 'Alcohol', 'Polio', 'GDP']
target = 'Life expectancy'

# Handle missing values
data = df[features + [target]].copy()
# For robustness, we drop rows with missing values in the selected features
data = data.dropna()

X = data[features]
y = data[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model trained successfully!")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

# Save model
joblib.dump(model, "model.joblib")
print("Model saved to model.joblib")
