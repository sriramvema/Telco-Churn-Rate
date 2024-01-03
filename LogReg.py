import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
# Step 3: Preprocess the data
# Drop unnecessary columns
df = df.drop(['customerID'], axis=1)
print(df.head())
# Convert categorical variables to numeric using one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Split the dataset into training and testing sets
X = df.drop('Churn_Yes', axis=1)  # Features (all columns except Churn_Yes)
y = df['Churn_Yes']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create and train the logistic regression model
model = LogisticRegression(max_iter=1000)  # Increase the maximum number of iterations
model.fit(X_train, y_train)

# Step 5: Make predictions on the test set
feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': model.coef_[0]})
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Step 6: Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
top_reasons_churning = feature_importances.sort_values(by='Importance', ascending=False)


churn_rate = sum(y_pred) / len(y_pred)
print("Churn rate:", churn_rate)

print("Top Reasons for Churning:")
print(top_reasons_churning)


# Step 8: Calculate the churn rate for each customer service
services = df.loc[X_test.index]  # Extract the services data corresponding to the test set
services['Churn'] = y_pred  # Add predicted churn labels to the services data
churn_rate_by_service = services.mean().sort_values(ascending=False)

print("Churn rate by customer service:")
print(churn_rate_by_service)


