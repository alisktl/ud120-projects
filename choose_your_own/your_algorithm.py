#!/usr/bin/python

import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################

### Initializing AdaBoostClassifier
#clf = AdaBoostClassifier(n_estimators=50, learning_rate=1.0, random_state=0)

### Initializing RandomForestClassifier
clf = RandomForestClassifier(max_depth=4, random_state=0)

### Fitting classifier
clf.fit(features_train, labels_train)

### Predicting
pred = clf.predict(features_test)

### Accuracy score
acc_score = accuracy_score(labels_test, pred)
print("Accuracy Score", acc_score);

### Plotting graph
try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
