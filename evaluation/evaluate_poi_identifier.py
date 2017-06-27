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

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here
from sklearn.cross_validation import train_test_split

# with split data
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30,
                                                                            random_state=42)

### Decision tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

pred_poi_num = len(filter(lambda x: x == 1, pred))
pred_label_num = len(pred)

True_positive_num = len(filter(lambda x: x == 1, pred))

print "pred_poi_num:", pred_poi_num
print "pred_label_num:", pred_label_num
print "accuracy:", accuracy_score(labels_test, pred)

true_positives = 0
for actual, predicted in zip(labels_test, pred):
    if actual == 1 and predicted == 1:
        true_positives += 1

print "true positives:", true_positives

from sklearn.metrics import precision_score, recall_score

print "precision score:", precision_score(labels_test, pred)
print "recall score:", recall_score(labels_test, pred)

pred_2 = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
labels_test_2 = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

true_positives_2 = 0
true_negative_2 = 0
false_positives_2 = 0
false_negatives_2 = 0
for actual, predicted in zip(labels_test_2, pred_2):
    if actual == 1 and predicted == 1:
        true_positives_2 += 1
    if actual == 0 and predicted == 0:
        true_negative_2 += 1
    if actual == 0 and predicted == 1:
        false_positives_2 += 1
    if actual == 1 and predicted == 0:
        false_negatives_2 += 1
print true_positives_2, true_negative_2,false_positives_2,false_negatives_2
print "precision score:", precision_score(labels_test_2, pred_2)
print "recall score:", recall_score(labels_test_2, pred_2)
