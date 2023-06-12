# Data and Machine Learning

In this repository I am looking to deepen my knowledge fo machine learning. I will be doing this in a few different ways, the first is to rebuild common machine learning algorithms from scratch. The Second is by putting it to use taking datasets that I can find doing analysis on them, sometimes using my own code sometimes using pre made libraries.

## Machine Learning from Scratch

### Regression
To begin with I have written up 4 notebooks that cover creating linear, logistic, multiliniear and polynomial regression algorithms from scratch. In these notebooks I first created synthetic data that followed the same shape as the model with some added noise, them I wrote up a algorithm that uses the gradient decent to close in on the optimal soloution.

### Decision Trees 
Here I put together a classification decision tree algorithm to classify data. In this project I tried to keep to an object orientated approach. The main reason for the object orientated approach was because it makes creating the tree structure easier as there is then just a tree object rather than trying to wrangle more primitive data structures. 

## Projects

To put the work above to use in this folder I will use the algorithms and pre made libraries to perform data analysis. Thus far I have completed 2 projects:

### Mushrooms, poisonous or not?

A mushroom classification project that classifies mushrooms into poisonous and non poisonous. The classification tree was extremely successful, I suspect that is because the categories are very clear cut with every mushroom being either poisonous or not and the feature set being sufficient to totally determine a mushroom. Therefore sufficient layers resulted in almost perfect results.

### Credit card Fraud

A credit card fraud detector algorithm, for this project I try tree different models, first a logistic regression model, then a decision tree classifier, and lastly a deep learning model. The deep learning model was found to be the most successful, however the margins were close, it also comes with the downside of a much longer training time than the logistic regression and decision tree. I did try to use my own decision tree code, however it is too inefficient and would take many hours to train, some more work needs to be done to optimise the code. 

### Diabetes detection

In this project I looked to try different methods of predicting if someone would have diabetes depending on other factors, including, gender, age, bmi, smoking history, blood glucose and historical blood glucose. The process went as follows, first I pulled in and visualized the data. Then onto the clean up process I found there were some peculiarities, namely that there was a lot of information missing in the smoking history category. I eventually chose to "interpolate" the data as a compromise, making the assumption that historical smoking would have an impact on current health. There was insufficient data to make a claim otherwise because of the many other confounding factors. In the end I chose to implement 4 models to compare their performance, the first was a basic logistic regression, the second was a decision tree, third a deep learning model and lastly a random forest. In terms of performance it was found that the random forest was the best performing, which is not surprising given the non linearity of the data, the deep learning model came close, however it also had the significant downside of a very long training period.
