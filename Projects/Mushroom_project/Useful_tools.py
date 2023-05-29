import numpy as np 
def accuracy_score(Y_pred, Y_true):
    acc = np.sum(np.equal(Y_true.flatten(), Y_pred)) / len(Y_true)
    return acc

def labelencoder(data):
    col = df.columns[0]
    dict = {}
    list = [x for x in data.unique()]
    for enum in range(len(list)):
        dict[list[enum]] = enum
    for label in list:
        data = data.apply(lambda x: dict[label] if x == label else x)
    return data