# To replace some of the more useful SKlearn functions I have written my own versions here

import numpy as np 

# This function will work out the accuracy as a percentage of the predictions of a model. 

def accuracy_score(Y_pred, Y_true):
    acc = np.sum(np.equal(Y_true.flatten(), Y_pred)) / len(Y_true)
    return acc

# This function works as a label encoder, taking categorical data and converting it to an enumerated dataset, useful for classification

def labelencoder(data):
    dict = {}
    list = [x for x in data.unique()]
    for enum in range(len(list)):
        dict[list[enum]] = enum
    data = data.apply(lambda x: dict[x])
    return data