#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_train[:len(labels_train) / 100]

from sklearn import svm

clf = svm.SVC(kernel='rbf', C=10000.0)
# 0.892491467577
# clf = svm.SVC(kernel='rbf', C=1000.0)
# 0.821387940842
# clf = svm.SVC(kernel='rbf', C=100.0)
# 0.616040955631
# clf = svm.SVC(kernel='rbf', C=10.0)
# 0.616040955631

t0 = time()

clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"
t0 = time()

predictions = clf.predict(features_test)
result = filter(lambda x: x == 1, predictions)
print len(result)
print predictions[10]
print predictions[26]
print predictions[50]
print "predict time:", round(time() - t0, 3), "s"

accuracy = clf.score(features_test, labels_test)
print accuracy
import os
os.system('say "your program has finished"')
#########################################################
