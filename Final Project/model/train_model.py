import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
data_path = 'TrafficDataSample.csv'
df = pd.read_csv(data_path)

# Preprocess the data
# Encode categorical variables
label_encoder = LabelEncoder()
encoded_df = df.apply(label_encoder.fit_transform)

# Fill missing values
encoded_df = encoded_df.fillna(encoded_df.mean())

# Features and target variable
X = encoded_df[['POSTED_SPEED_LIMIT', 'WEATHER_CONDITION', 'LIGHTING_CONDITION', 'FIRST_CRASH_TYPE']].values
y = encoded_df['INJURIES_TOTAL'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Evaluate the model
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the trained model to disk
joblib.dump(clf, 'traffic_model.pkl')
