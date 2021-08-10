#!/usr/bin/python3

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

import joblib

enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))

### Number of data points (people) in the dataset
print("Number of data points:", len(enron_data))

### Number of features of each data point
print("Number of features for each person:", len(enron_data[list(enron_data.keys())[0]]))

### Count the number of people with 'poi' == 1
poi_count = 0
for key in enron_data:
    poi_count += (enron_data[key]["poi"] == 1)
print("Number of POI:", poi_count)
