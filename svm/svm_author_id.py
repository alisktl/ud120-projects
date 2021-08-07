#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from collections import Counter
from time import time
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

### creating SVM classifier
clf = SVC(kernel="rbf", C=10000)

### slicing the training dataset down to 1% of its original size
features_train = features_train[:int(len(features_train)/100)]
labels_train = labels_train[:int(len(labels_train)/100)]

t0 = time()
clf.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print("Predicting Time:", round(time()-t0, 3), "s")

acc_score = accuracy_score(labels_test, pred)
print("Accuracy Score:", acc_score)

print("Predictions:")
print("10:", pred[10])
print("26:", pred[26])
print("50:", pred[50])

c = Counter(pred)
print("Number of predictions for Chris:", c[1])
print("Number of predictions for Sara:", c[0])