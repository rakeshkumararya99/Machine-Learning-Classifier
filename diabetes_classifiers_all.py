# -*- coding: utf-8 -*-
"""Diabetes_Classifiers_All.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UgnWt0oFHKUmisHtNcW5M43wdJcrreOZ
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix

# Load the data
df = pd.read_csv('diabetes.csv')

df

df.head()

# Split the data into features and target
X = df.drop('Outcome', axis=1) # This code creates a new DataFrame X by dropping the 'Kyphosis' column from the original DataFrame df.
# The axis=1 argument specifies that we want to drop a column instead of a row. 
#The resulting DataFrame X will contain all the other columns except 'Kyphosis'.
y = df['Outcome']

X

y

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train

X_test

y_train

y_test

# Decision Tree Classifier
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred1 = dt.predict(X_test)
print(classification_report(y_test,y_pred1))

"""**Precision**: the ratio of true positives to the sum of true positives and false positives. In other words, how many of the positive predictions were actually correct.
For class 0, the precision is 0.83, which means that 83% of the instances predicted as class 0 are actually class 0. For class 1, the precision is 0.65, indicating that 65% of the instances predicted as class 1 are actually class 1.
**Recall**: the ratio of true positives to the sum of true positives and false negatives. In other words, how many of the actual positive cases were correctly identified.Also known as sensitivity or true positive rate, measures the proportion of correctly predicted positive instances out of the actual positive instances. For class 0, the recall is 0.79, meaning that 79% of the actual class 0 instances are correctly identified as class 0. For class 1, the recall is 0.71, indicating that 71% of the actual class 1 instances are correctly identified as class 1.
**F1-score**: The F1-score is the harmonic mean of precision and recall, providing a balanced measure that considers both precision and recall. It combines both metrics into a single value. For class 0, the F1-score is 0.79, while for class 1, it is 0.67. Higher values of the F1-score indicate better performance.the harmonic mean of precision and recall.
**Support**: the number of instances of each class in the test set.In this case, there are 99 instances of class 0 and 55 instances of class 1.

The accuracy of the model is reported as 0.75, which means that 75% of the instances in the test set were classified correctly.

The macro average of precision, recall, and F1-score is calculated by averaging the scores for each class without considering class imbalance. In this case, the macro average precision is 0.74, the macro average recall is 0.75, and the macro average F1-score is 0.74.

The weighted average of precision, recall, and F1-score is calculated by weighting each class's score by its support (the number of instances in each class) and then averaging them. In this case, the weighted average precision is 0.77, the weighted average recall is 0.76, and the weighted average F1-score is 0.76.
"""

#Predict New Case
New_Patient =[[2,146,70,38,360,28.0,0.337,29]] 
# The Values are of Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
Predict_New_Patient_dt = dt.predict(New_Patient)

Predict_New_Patient_dt

"""The new patient y (outcome) is 0 , ie will not have diabetes as per Decison Tree"""

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred2 = lr.predict(X_test)
print(classification_report(y_test,y_pred2))

#Predict New Case
New_Patient =[[2,146,70,38,360,28.0,0.337,29]] 
# The Values are of Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
Predict_New_Patient_lr = lr.predict(New_Patient)

Predict_New_Patient_lr

#Gaussian Naive Bayes
nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)
print(classification_report(y_test,y_pred2))

#Predict New Case
New_Patient =[[2,146,70,38,360,28.0,0.337,29]] 
# The Values are of Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
Predict_New_Patient_nb = nb.predict(New_Patient)

Predict_New_Patient_nb

# Random Forest Classifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred3 = rf.predict(X_test)
print(classification_report(y_test,y_pred3))

#Predict New Case
New_Patient =[[2,146,70,38,360,28.0,0.337,29]] 
# The Values are of Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
Predict_New_Patient_rf = rf.predict(New_Patient)

Predict_New_Patient_rf

# Support Vector Machine
svm = SVC()
svm.fit(X_train, y_train)
y_pred4 = svm.predict(X_test)
print(classification_report(y_test,y_pred4))

#Predict New Case
New_Patient =[[2,146,70,38,360,28.0,0.337,29]] 
# The Values are of Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
Predict_New_Patient_svm = svm.predict(New_Patient)

Predict_New_Patient_svm

# AdaBoost Classifier
ada = AdaBoostClassifier()
ada.fit(X_train, y_train)
y_pred5 = ada.predict(X_test)
print(classification_report(y_test,y_pred5))

#Predict New Case
New_Patient =[[2,146,70,38,360,28.0,0.337,29]] 
# The Values are of Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
Predict_New_Patient_ada= ada.predict(New_Patient)

Predict_New_Patient_ada

# XGBoost Classifier
from xgboost import XGBClassifier
xgb = XGBClassifier()
xgb.fit(X_train, y_train)
y_pred6 = xgb.predict(X_test)
print(classification_report(y_test,y_pred6))

#Predict New Case

New_Patient = [[2, 146, 70, 38, 360, 28.0, 0.337, 29]]  

# Make the prediction
Predict_New_Patient_xgb = xgb.predict(New_Patient)

"""XGBoost classifier (xgb) expects the training data to have specific field names. To resolve this issue,  modify the New_Patient input to match the field names used in the training data

"""

# Create a new instance with features for prediction
New_Patient = [[2, 146, 70, 38, 360, 28.0, 0.337, 29]]  # Replace with the actual features of the new case

# Convert the new case into a DataFrame with field names
import pandas as pd
new_patient_df = pd.DataFrame(New_Patient, columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

# Make the prediction
Predict_New_Patient_xgb = xgb.predict(new_patient_df)

print("Predicted Class:", Predict_New_Patient_xgb)



"""Classification Metrics for Diabetes suggests Decision Tress & SVM both perform the best thought all classifiers have predicted the same outcome (o) except Gaussian Naive Bayes which predicted 1
XGBoost is the worst performer
"""





new_patient_df

