# Data Wrangling
import pandas as pd 
# Linear Alegbra
import numpy as np
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
# Pre Processing
from sklearn import preprocessing, svm 
# Models
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
# Evaluation
from sklearn import metrics 
# Statistics
from scipy import stats

# This function will help us out along the way and we will use later

def do_regression(data, X,Y):
    reg = LinearRegression().fit((data[X].values).reshape(-1, 1),data[Y].values)
    reg.get_params()
    R_sqr = reg.score((data[X].values).reshape(-1, 1),data[Y].values)
    data[f"{Y} prediction"] = reg.predict((data[X].values).reshape(-1, 1))
    rmse = metrics.mean_squared_error(data[Y].values,data[f"{Y} prediction"].values, squared=False)
    coef = reg.coef_
    intercept = reg.intercept_
    return [R_sqr,rmse,coef,intercept]
