import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import joblib

#Load the preprocessed dataset
X_train_scaled = pd.read_csv("data/processed_data/X_train_scaled.csv")
X_test_scaled = pd.read_csv("data/processed_data/X_test_scaled.csv")
y_train = pd.read_csv("data/processed_data/y_train.csv")
y_test = pd.read_csv("data/processed_data/y_test.csv")

# Resampling to overcome class imbalance
#Initialize smote to overcome class imbalance
X_train_smote, y_train_smote = SMOTE().fit_resample(X_train_scaled, y_train)

#Instantiate model with best parameters
rf = RandomForestClassifier(n_estimators=200, max_depth=None, min_samples_leaf=1, min_samples_split=2)

#Training the model
rf.fit(X_train_smote, y_train_smote)

#Save the model
joblib.dump(rf, 'models/random_forest_model.joblib')