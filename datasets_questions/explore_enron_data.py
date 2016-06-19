#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people in the dataset:", len(enron_data)

print "Number of features:",
first_person = enron_data.keys()[0]
first_set_of_features = enron_data[first_person]
print len(first_set_of_features)

print "Number of POIs:",
pois = {name: features for name, features in enron_data.iteritems() if features["poi"]} # filter using a dict comprehension
print len(pois)

print "Total value of stock belonging to James Prentice:",
print enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Email messages from Wesley Colwell to POIs:",
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Value of stock options exercised by Jeffrey Skilling:",
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Total payments for Lay:",
print enron_data["LAY KENNETH L"]["total_payments"]
print "Total payments for Skilling:",
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Total payments for Fastow:",
print enron_data["FASTOW ANDREW S"]["total_payments"]

print "No of folks with quantified salary:",
with_salary = {name: features for name, features in enron_data.iteritems() if features["salary"] != "NaN"}
print len(with_salary)

print "No of folks with known email address:",
with_email_address = {name: features for name, features in enron_data.iteritems() if features["email_address"] != "NaN"}
print len(with_email_address)

# We’ve written some helper functions (featureFormat() and targetFeatureSplit() in tools/feature_format.py) that can take a list of feature names and the data dictionary, and return a numpy array.
# In the case when a feature does not have a value for a particular person, this function will also replace the feature value with 0 (zero).

def printPartPercentage(part, whole):
    print part, "i.e.", 
    percentage = float(part)/float(whole) * 100.0
    print("{0:.2f}".format(percentage)), "%"

print "No of people having “NaN” for their total payments:",
without_total_payments = {name: features for name, features in enron_data.iteritems() if features["total_payments"] == "NaN"}
printPartPercentage(len(without_total_payments), len(enron_data))

print "No of POIs having “NaN” for their total payments:",
pois_without_total_payments = {name: features for name, features in pois.iteritems() if features["total_payments"] == "NaN"}
printPartPercentage(len(pois_without_total_payments), len(pois))

def without_nan(enron_data, feature):
    return {name: features for name, features in enron_data.iteritems() if name != "TOTAL" and features[feature] != "NaN"}

def minimum_feature(enron_data, feature):
    minimum_feature = lambda memo,current: memo if (enron_data[memo][feature] < enron_data[current][feature]) else current
    min_index = reduce(minimum_feature, without_nan(enron_data, feature))
    print "Minimum value for", feature, ":", enron_data[min_index][feature], "for",  min_index

def maximum_feature(enron_data, feature):
    maximum_feature = lambda memo,current: memo if (enron_data[memo][feature] > enron_data[current][feature]) else current
    max_index = reduce(maximum_feature, without_nan(enron_data, feature))
    print "Maximum value for", feature, ":", enron_data[max_index][feature], "for",  max_index
      
minimum_feature(enron_data, "exercised_stock_options")
maximum_feature(enron_data, "exercised_stock_options")

minimum_feature(enron_data, "salary")
maximum_feature(enron_data, "salary")