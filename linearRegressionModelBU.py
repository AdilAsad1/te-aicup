import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor

# Read the CSV file
data = pd.read_csv('bu2_appliances.csv')
# Encode categorical columns
labelencoder = LabelEncoder()
data['business_unit_group_name'] = labelencoder.fit_transform(data['business_unit_group_name'])
data['company_region_name_level_1'] = labelencoder.fit_transform(data['company_region_name_level_1'])
data['product_line_code'] = labelencoder.fit_transform(data['product_line_code'])
data['product_line_name'] = labelencoder.fit_transform(data['product_line_name'])

# Create dummy variables for categorical columns
data = pd.get_dummies(data, columns=['business_unit_group_name', 'company_region_name_level_1', 'product_line_code', 'product_line_name'])

# Split the data into training and testing sets
X = data.drop(['sales_amount'], axis=1)
y = data['sales_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = HistGradientBoostingRegressor()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Evaluate the model
score = model.score(X_test, y_test)
print('R-squared:', score)
