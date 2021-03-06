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
        if line.startswith('(y)') or line.startswith('(n)'):
            poi_count += 1
print "How many POIs are there in the E+F dataset?(35) ", \
    poi_count

total_stock_value_of_james = enron_data["PRENTICE JAMES"]["total_stock_value"]
print "What is the total value of the stock belonging to James Prentice?(1095040) ", \
    total_stock_value_of_james

mail_count = 0

for person in enron_data:
    if person == "COLWELL WESLEY" and enron_data[person]["from_this_person_to_poi"]:
        mail_count += enron_data[person]["from_this_person_to_poi"]

print "How many email messages do we have from Wesley Colwell to persons of interest?(11) ", \
    mail_count
print "What is the value of stock options exercised by Jeffrey K Skilling?(19250000) ", \
    enron_data['SKILLING JEFFREY K']["exercised_stock_options"]

print "the most money"

for name, data in enron_data.iteritems():
    if 'lay' in name.lower():
        print name
        print data['exercised_stock_options']
        print data['total_payments']

print 'a'
for name, data in enron_data.iteritems():
    if 'jeffrey' in name.lower() and 'skilling' in name.lower():
        print name
        print data['total_payments']

print 'a'
for name, data in enron_data.iteritems():
    if 'fastow' in name.lower():
        print name
        print data['exercised_stock_options']
        print data['total_payments']
import numpy as np

total_payments_unavailable = 0
total_payments_unavailable_poi = 0
for name, data in enron_data.iteritems():
    if np.isnan(float(data['total_payments'])):
        total_payments_unavailable += 1
print "NaN for total payment and percentage:", \
    total_payments_unavailable, float(total_payments_unavailable)/len(enron_data)*100
for name, data in enron_data.iteritems():
    if np.isnan(float(data['total_payments'])) and data['poi']:
        total_payments_unavailable_poi += 1
print "NaN for total payment of POI and percentage:", \
    total_payments_unavailable_poi, float(total_payments_unavailable_poi)/len(enron_data)*100


# How is an unfilled feature denoted?
print "How is an unfilled feature denoted?(11) ", \
    enron_data['FASTOW ANDREW S']['deferral_payments']
# How many folks in this dataset have a quantified salary?
# What about a known email address?
count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary += 1
    if enron_data[key]['email_address'] != 'NaN':
        count_email += 1
print "How many folks in this dataset have a quantified salary?(95) ", \
    count_salary
print "What about a known email address?(111) ", \
    count_email

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
