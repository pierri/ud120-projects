#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

import numpy
print "Number of POIs predicted in the test set:", numpy.count_nonzero(pred) # 4
print "People total in test set:", len(labels_test) # 29


from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(labels_test, pred)
print "Number of true positives:", conf_mat[1][1]

from sklearn.metrics import recall_score, precision_score, f1_score
print "Precision score:", precision_score(labels_test, pred)
print "Recall score:", recall_score(labels_test, pred)

print
print "MADE UP PREDICTIONS"
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
conf_mat = confusion_matrix(true_labels, predictions)
print "Number of true positives:", conf_mat[1][1] # 6
print "Number of true negatives:", conf_mat[0][0] # 9
print "Number of false positives:", conf_mat[0][1] # 3
print "Number of false negatives:", conf_mat[1][0] # 2
print "Precision score:", precision_score(true_labels, predictions)
print "Recall score:", recall_score(true_labels, predictions)
print "F1 score:", f1_score(true_labels, predictions)
