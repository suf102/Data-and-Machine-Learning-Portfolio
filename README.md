# Data and Machine Learning

In this repository I am looking to deepen my knowledge fo machine learning. I will be doing this in a few different ways, the first is to rebuild common machine learning algorithms from scratch. The Second is by putting it to use taking datasets that I can find doing analysis on them, sometimes using my own code sometimes using pre made libraries.

## Regression
To begin with I have written up 4 notebooks that cover creating linear, logistic, multiliniear and polynomial regression algorithms from scratch. In these notebooks I first created synthetic data that followed the same shape as the model with some added noise, them I wrote up a algorithm that uses the gradient decent to close in on the optimal soloution.

## Decision Trees 
Here I put together a classification decision tree algorithm to classify data. In this poject I tried to keep to an object orientated approach. The main reason for the object orientated approach was because it makes creating the tree structure easier as there is then just a tree object rahter than trying to wrangle more primative data structures. 

## Projects

To put the work above to use in this folder I will use the algorithms and pre made libraries to perform data analysis. Thus far I have completed 2 projects:

A mushroom classification project that classifies mushrooms into poisonous and non poisonous. The classification tree was extremely successful, I suspect that is because the categories are very clear cut with every mushroom being either poisonous or not and the feature set being sufficient to totally determine a mushroom. Therefore sufficient layers resulted in almost perfect results.

A credit card fraud detector algorithm, for this project I try tree different models, first a logistic regression model, then a decision tree classifier, and lastly a deep learning model. The deep learning model was found to be the most sucessful. I did try to use my own decision tree code, however it is too inefficient and would take many hours to train, some more work needs to be done to optimise the code. 
