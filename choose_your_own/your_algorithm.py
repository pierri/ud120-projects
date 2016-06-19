#!/usr/bin/python

import matplotlib.pyplot as plt
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
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from time import time

from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB() # Accuracy: 0.884

from sklearn import svm
#clf = svm.SVC(kernel="linear") # Accuracy: 0.92
#clf = svm.SVC(kernel="rbf") # Accuracy: 0.92
#clf = svm.SVC(kernel="rbf", C=1000) # Accuracy: 0.924
#clf = svm.SVC(kernel="rbf", C=100000) # Accuracy: 0.944

from sklearn import tree
#clf = tree.DecisionTreeClassifier(min_samples_split=36) # Accuracy: 0.912

from sklearn.ensemble import AdaBoostClassifier
#clf = AdaBoostClassifier(n_estimators = 100) # Accuracy: 0.924

from sklearn.ensemble import RandomForestClassifier
#clf = RandomForestClassifier(n_estimators = 10) # Accuracy: 0.916

print "Fitting...",
t0 = time()
clf.fit(features_train, labels_train)
print "Done in", round(time()-t0, 3), "s"

print "Predicting...",
t0 = time()
pred = clf.predict(features_test)
print "Done in", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
print "Accuracy:", accuracy_score(labels_test, pred)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
