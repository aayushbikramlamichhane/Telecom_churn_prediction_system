import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score


#data collection and Analysis
dataset=pd.read_excel('trial2.xlsx')
#dataset.describe()


#seperating data and labels
X=dataset.drop(columns=['ID','Married','Churn'],axis=1)
Y=dataset['Churn']

#data standardiztion
scaler=StandardScaler()
scaler.fit(X)
X_std=scaler.transform(X)

#oversampling
from imblearn import over_sampling,under_sampling
ros=over_sampling.RandomOverSampler(random_state=0)
X_re,Y_re=ros.fit_resample(X_std,Y)


#train test split
X_train,X_test,Y_train,Y_test=train_test_split(X_re,Y_re, test_size=0.2, stratify=Y_re, random_state=15)
#train model
decision=svm.SVC(kernel='linear')
decision.fit(X_train,Y_train)


y_pred = decision.predict(X_train)
distances = decision.decision_function(X_train)

# filter the distances to include only the positive and negative ones
positive_distances = distances[y_pred == 0]
negative_distances = distances[y_pred == 1]

# compute the highest and lowest positive distances
max_positive_distance = np.max(positive_distances)
min_positive_distance = np.min(positive_distances)

# compute the highest and lowest negative distances
max_negative_distance = np.max(negative_distances)
min_negative_distance = np.min(negative_distances)

print('Highest positive distance:', max_positive_distance)
print('Lowest positive distance:', min_positive_distance)
print('Highest negative distance:', max_negative_distance)
print('Lowest negative distance:', min_negative_distance)

y_pred = decision.predict(X_train)
distances = decision.decision_function(X_train)

# filter the distances to include only the positive and negative ones
positive_distances = distances[y_pred == 0]
negative_distances = distances[y_pred == 1]

# compute the highest and lowest positive distances
max_positive_distance = np.max(positive_distances)
min_positive_distance = np.min(positive_distances)

# compute the highest and lowest negative distances
max_negative_distance = np.max(negative_distances)
min_negative_distance = np.min(negative_distances)

print('Highest positive distance:', max_positive_distance)
print('Lowest positive distance:', min_positive_distance)
print('Highest negative distance:', max_negative_distance)
print('Lowest negative distance:', min_negative_distance)

#model evaluation
#training data
X_prediction=decision.predict(X_train)
accuracy1=accuracy_score(X_prediction,Y_train)
print('Accuracy is : ',accuracy1)
#test data
X_testprediction=decision.predict(X_test)
accuracy2=accuracy_score(X_testprediction,Y_test)
print('Accuracy is : ',accuracy2)
print('confusion matrix : \n',confusion_matrix(X_testprediction,Y_test))
precision = precision_score(X_testprediction,Y_test)
recall = recall_score(X_testprediction,Y_test)
f1_score = f1_score(X_testprediction,Y_test)

# print the results
print('Precision:', precision)
print('Recall:', recall)
print('F1 Score:', f1_score)



from joblib import dump
dump(scaler,'savedmodels/scaler.joblib')
from joblib import dump
dump(decision,'savedmodels/model.joblib')




