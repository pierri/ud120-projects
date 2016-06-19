#!/usr/bin/python

def computeError(pred, age, net_worth):
    return age, net_worth, (pred - net_worth)

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    ### your code goes here
    cleaned_data = map(computeError, predictions, ages, net_worths)
    
    cleaned_data = sorted(cleaned_data, key=lambda tuple:tuple[2]) # error is the third entry in the tuple
    
    index = len(cleaned_data) * 9 / 10
    cleaned_data = cleaned_data[1:index]
        
    return cleaned_data

