import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

#Load raw dataset
df = pd.read_csv("data/raw/raw.csv") 

#Preprocessing the categorical variable
# Label encoding gender, 
le = LabelEncoder()
df['gender'] = le.fit_transform(df1['gender'])
df'smoking_history'] = le.fit_transform(df1['smoking_history'])
df['age_range'] = le.fit_transform(df1['age_range'])

#Selecting dependent and target variable
X = df.drop(columns=['diabetes'], axis=1)
y = df['diabetes']

#Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#Preprocessing the numerical variable using MinMaxScaler
scaler = MinMaxScaler()
columns_to_scale = ['bmi', 'blood_glucose_level', 'HbA1c_level']
columns_not_to_scale = ['gender', 'hypertension', 'heart_disease', 'smoking_history', 'age_range']

#Fit the scaler
X_train_scaled_numeric = scaler.fit_transform(X_train[columns_to_scale])
X_test_scaled_numeric = scaler.transform(X_test[columns_to_scale])

#Conver teh scaled numeric arrays back to dataframe
X_train_scaled = pd.DataFrame(X_train_scaled_numeric, columns=columns_to_scale)
X_test_scaled = pd.DataFrame(X_test_scaled_numeric, columns=columns_to_scale)

#Reattach non-numeric columns to the scaled data
X_train_scaled = pd.concat([X_train_scaled, X_train[columns_not_to_scale].reset_index(drop=True)], axis=1)
X_test_scaled = pd.concat([X_test_scaled, X_test[columns_not_to_scale].reset_index(drop=True)], axis=1)

#saving the data into processed directory
X_train_scaled.to_csv("data/processed_data/X_train_scaled.csv", index=False)
X_test_scaled.to_csv("data/processed_data/X_test_scaled.csv", index=False)
y_train.to_csv("data/processed_data/y_train.csv", index=False)
y_test.to_csv("data/processed_data/y_test.csv", index=False)

