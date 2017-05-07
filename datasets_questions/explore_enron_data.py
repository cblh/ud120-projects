#!/usr/bin/python

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

print len(enron_data)
print enron_data['ALLEN PHILLIP K']['poi']
print enron_data['ALLEN PHILLIP K']
print len(enron_data['ALLEN PHILLIP K'])

keys = enron_data.keys()
print keys
poi_data = filter(
    lambda x:
    enron_data[x]['poi'],
    enron_data)

print poi_data

print 'len(poi_data)'
print len(poi_data)
import os

os.system('say "your program has finished"')
