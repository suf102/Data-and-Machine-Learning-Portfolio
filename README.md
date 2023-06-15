In this repository I am looking to deepen my knowledge fo machine learning. I will be doing this in a few different ways, the first is to rebuild common machine learning algorithms from scratch. The Second is by putting it to use taking datasets that I can find doing analysis on them, sometimes using my own code sometimes using pre made libraries.

## Projects

To put the work above to use in this folder I will use the algorithms and pre made libraries to perform data analysis. Thus far I have completed 4 projects:

### [Diabetes Detection](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Projects/Diabeties_detection)

In this project, I experimented with different methods of predicting whether someone would have diabetes depending on other factors, including gender, age, BMI, smoking history, blood glucose, and historical blood glucose levels. The process went as follows: first, I pulled in and visualized the data. Then, during the clean-up process, I found there were some peculiarities, namely, there was a lot of information missing in the smoking history category. I eventually chose to "interpolate" the data as a compromise, making the assumption that historical smoking would have an impact on current health. There was insufficient data to make a claim otherwise because of the many other confounding factors. In the end, I chose to implement four models to compare their performance. The first was a basic logistic regression, the second was a decision tree, third a deep learning model, and lastly a random forest. In terms of performance, it was found that the random forest was the best performing, which is not surprising given the non-linearity of the data. The deep learning model came close, however, it also had the significant downside of a very long training period.

### [Excise rates and RTD Consumption](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Projects/RTD_Consumption)

In this project I focus on trying to determine if the excise rate on Ready to Drink Alcoholic beverages has an impact on the rate of consumption. I have included a short writeup pdf that summarizes my findings that increases that are not indexed to inflation have a impact, but increases that are indexed to inflation have little impact. 

### [Credit Card Fraud](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Projects/Credit_Card_Fraud_detection)

A credit card fraud detector algorithm was developed for this project. I tried three different models: first, a logistic regression model, then a decision tree classifier, and lastly, a deep learning model. The deep learning model was found to be the most successful, however, the margins were close. It also comes with the downside of a much longer training time than the logistic regression and decision tree models. I did try to use my own decision tree code, however, it was too inefficient and would take many hours to train. Some more work needs to be done to optimise the code.

### [Mushrooms, Poisonous or Not?](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Projects/Mushroom_project)

A mushroom classification project that classifies mushrooms into poisonous and non-poisonous. The classification tree was extremely successful, I suspect this is because the categories are very clear cut with every mushroom being either poisonous or not and the feature set being sufficient to totally determine a mushroom. Therefore, sufficient layers resulted in almost perfect results.

## Machine Learning from Scratch

### [Regression](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Machine_Learning_from_Scratch/Regression_From_Scratch)
To begin with I have written up 4 notebooks that cover creating linear, logistic, multiliniear and polynomial regression algorithms from scratch. In these notebooks I first created synthetic data that followed the same shape as the model with some added noise, them I wrote up a algorithm that uses the gradient decent to close in on the optimal soloution.

### [Decision Trees](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Machine_Learning_from_Scratch/Decision_Trees) 
Here I put together a classification decision tree algorithm to classify data. In this project I tried to keep to an object orientated approach. The main reason for the object orientated approach was because it makes creating the tree structure easier as there is then just a tree object rather than trying to wrangle more primitive data structures. 
## Hackathons

### [MEV Hackathon](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Hackathons/MEV_Hackathon)
In 2022 I competed in a MEV hackathon, I have included the full project including its writeup under the Hackathon folder. 
