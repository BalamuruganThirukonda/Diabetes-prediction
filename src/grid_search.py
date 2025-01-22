import pandas as pd
from sklearn.model_selection import GridSearchCV

#Load the preprocessed dataset
X_train_scaled = pd.read_csv("data/processed_data/X_train_scaled.csv")
X_test_scaled = pd.read_csv("data/processed_data/X_test_scaled.csv")
y_train = pd.read_csv("data/processed_data/y_train.csv")
y_test = pd.read_csv("data/processed_data/y_test.csv")

# Resampling to overcome class imbalance
#Initialize smote to overcome class imbalance
X_train_smote, y_train_smote = SMOTE().fit_resample(X_train_scaled, y_train)

#Instantiate the model
model = RandomForestClassifier(random_state=42)

# Minimal parameter grid for RandomForestClassifier
param_grid = {
    'n_estimators': [100, 200],               # Number of trees in the forest
    'max_depth': [None, 10],                   # Maximum depth of trees
    'min_samples_split': [2, 10],              # Minimum samples required to split an internal node
    'min_samples_leaf': [1, 2]                 # Minimum samples required at a leaf node
}

# Initialize the GridSearchCV object
grid_search = GridSearchCV(estimator=model, 
                           param_grid=param_grid, 
                           cv=5,                              # 5-fold cross-validation
                           verbose=2,                         # To display the progress
                           n_jobs=-1,                         # Use all CPU cores
                           scoring='accuracy')                # The metric to optimize

# Fit the model with grid search
grid_search.fit(X_train_smote, y_train_smote)

# Get the best parameters and the best score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print(f"Best parameters found: {best_params}")
print(f"Best cross-validation accuracy: {best_score * 100:.2f}%")