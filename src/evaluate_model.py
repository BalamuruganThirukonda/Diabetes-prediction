import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import joblib
import matplotlib.pyplot as plt

#Load the preprocessed dataset
X_train_scaled = pd.read_csv("data/processed_data/X_train_scaled.csv")
X_test_scaled = pd.read_csv("data/processed_data/X_test_scaled.csv")
y_train = pd.read_csv("data/processed_data/y_train.csv")
y_test = pd.read_csv("data/processed_data/y_test.csv")

# Resampling to overcome class imbalance
#Initialize smote to overcome class imbalance
X_train_smote, y_train_smote = SMOTE().fit_resample(X_train_scaled, y_train)

#Load model
rf_loaded = joblib.load('models/random_forest_model.joblib')

#Model Prediction
y_pred = rf_loaded.predict(X_test_scaled)

#Accuracy of prediction
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Classifier Accuracy Score:{accuracy}")

#F1 score of prediction
f1score = f1_score(y_test, y_pred)
print(f"F1 score : {f1score}")

#Classification report
classificationreport =  classification_report(y_test, y_pred)
print(f"Classification Report : {classificationreport}")

#Confusion matrix
rf_classifier_matrix = confusion_matrix(y_test, y_pred)
rf_classifier_matrix_display = ConfusionMatrixDisplay(rf_classifier_matrix)
fig, ax = plt.subplots(figsize=(10,10))
rf_classifier_matrix_display.plot(cmap=plt.cm.Blues, ax=ax)

# Ensure y_test and y_pred are 1-dimensional
y_test_flat = y_test.values.flatten() if hasattr(y_test, "values") else y_test
y_pred_flat = y_pred.values.flatten() if hasattr(y_pred, "values") else y_pred

# Create a DataFrame for predictions
predictions_df = pd.DataFrame({
    'Actual': y_test_flat,
    'Predicted': y_pred_flat
})

# Save the DataFrame to a CSV file
predictions_df.to_csv('predictions.csv', index=False)

#Feature importance
feature_importances = rf.feature_importances_

# Create a DataFrame to display feature importance with their corresponding feature names
importance_df = pd.DataFrame({
    'Feature': X_train_smote.columns,  # Replace with feature names
    'Importance': feature_importances
})

# Sort features by importance
importance_df = importance_df.sort_values(by='Importance', ascending=False)

#Save the feature importance
importance_df.to_csv('metrics/feature_importance.csv', index=False)

# Plot feature importance
plt.figure(figsize=(10, 8))
plt.barh(importance_df['Feature'], importance_df['Importance'], color='skyblue')
plt.xlabel('Feature Importance')
plt.ylabel('Features')
plt.title('Feature Importance for Random Forest')
plt.gca().invert_yaxis()  # Reverse the order for better visualization
plt.savefig('metrics/feature_importance_plot.png', bbox_inches='tight')
plt.show()