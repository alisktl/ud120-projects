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
import re

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

### Number of all POI
poi_all = 0
with open("../final_project/poi_names.txt") as file:
    content = file.readlines()
for line in content:  
    if re.match(r'\((y|n)\)', line):
        poi_all += 1
        
print("Number of all POI:", poi_all)

### Total value of the stock belonging to James Prentice
print("Total value of the stock belonging to James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"])

### Wesley Colwell's number of email messages to persons of interest?
print("Wesley Colwell's number of email messages to persons of interest:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

### Total value of stock options exercised by Jeffrey Skilling
print("Total value of stock options exercised by Jeffrey Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

### Of these three individuals (Lay, Skilling and Fastow), who took home the most money?
persons_execs = [person for person in enron_data if ("LAY" in person) or ("SKILLING" in person) or ("FASTOW" in person)]
person_max_payment = max([(enron_data[person]["total_payments"], person) for person in persons_execs])
print(person_max_payment[1], "took home $", person_max_payment[0])

### How many folks in this dataset have a quantified salary? What about a known email address?
quant_sal_count = len([person for person in enron_data if enron_data[person]["salary"] != 'NaN'])
print("Number of quantified salaries:", quant_sal_count)
