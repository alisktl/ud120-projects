#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    temp_data = []

    pred_count = len(predictions)

    for i in range(pred_count):
        temp_error = abs(predictions[i] - net_worths[i])
        temp_tuple = (ages[i], net_worths[i], temp_error)
        temp_data.append(temp_tuple)

    temp_data.sort(key = lambda data: data[2])
    cleaned_data = temp_data[0:int(len(temp_data)*0.9)]

    return cleaned_data
