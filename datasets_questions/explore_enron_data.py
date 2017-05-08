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
print "How many data points (people) are in the dataset?(146) ", \
        len(enron_data.keys())

print "For each person, how many features are available?(21) ", \
        len(enron_data[enron_data.keys()[0]].keys())


poi_data = filter(
    lambda x:
    enron_data[x]['poi'],
    enron_data)
print "How many POIs are there in the E+F dataset?(18) ", \
    len(poi_data)

import sys
sys.path.append("../final_project/")


poi_count = 0
with open("../final_project/poi_names.txt") as names_file:
    for line in names_file:
        if line.startswith('(y)') or line.startswith('(n)') :
            poi_count += 1
print "How many POIs are there in the E+F dataset?(35) ", \
    poi_count

# filter_poi_data = filter(
#     lambda x:
#     operator.indexOf(poi_emails, poi_data[x]['email_address']),
#     poi_data
# )
# filter_poi_data = reduce(
#     lambda x:
#     poi_data[x]['email_address'],
#     poi_data
# )
# print len(filter_poi_data)
import os

os.system('say "your program has finished"')
