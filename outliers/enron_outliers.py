#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )


# Find which point has salary > 2.5 * 1e7
big_salaries = {name: features for name, features in data_dict.iteritems() if (features["salary"] != "NaN" and features["salary"] > 25000000)} 
outlier_key = big_salaries.keys()[0]
print outlier_key, "has a pretty big salary"

# Remove TOTAL outlier
data_dict.pop(outlier_key, 0)


bandits = {name: features for name, features in data_dict.iteritems() if (features["salary"] != "NaN" and features["salary"] > 1000000 and features["bonus"] != "NaN" and features["bonus"] > 5000000)}
print bandits.keys()[0], "and", bandits.keys()[1], "made out like bandits" 


features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
#matplotlib.pyplot.show()
