import numpy as np 
def accuracy_score(Y_pred, Y_true):
    acc = np.sum(np.equal(Y_true.flatten(), Y_pred)) / len(Y_true)
    return acc