#!/usr/bin/python3

import joblib
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = joblib.load( open("../final_project/final_project_dataset.pkl", "rb") )

### Removing outlier
data_dict.pop("TOTAL", 0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

max_bonus = data.max()

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

max_bonus_person = [person for person in data_dict if(data_dict[person]["bonus"] == max_bonus)]
#print("Outlier entry:", max_bonus_person)

### Identifying two more outliers
max_bonus_persons = [person for person in data_dict.keys() if(type(data_dict[person]["bonus"]) == type(5000000)) and (data_dict[person]["bonus"] > 5000000) and (data_dict[person]["salary"] > 1000000)]
print("Outlier entry:", max_bonus_persons)
