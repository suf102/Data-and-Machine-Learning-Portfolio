This is the online portfolio of Sufyan, a dedicated explorer in the realm of numbers, probabilities, and patterns. My journey through the vast world of data and statistics has been filled with fascinating discoveries and rich insights.

Here, you will find a collection of my work, where I've applied my statistical and programming skills to tackle real-world problems. My portfolio and underlying repositories are split into two sections:

The first consists of applied projects where I have taken various datasets and performed analyses on them. I have worked through the entire process, from data cleaning and processing to the implementation of several models, to find the one that works best.

The second section contains projects where I have been rebuilding common machine learning and statistical algorithms from scratch, aiming to enhance my understanding of these models.
## Projects


### [Diabetes Detection](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Projects/Diabeties_detection)
In this project, I experimented with different methods of predicting whether someone would have diabetes depending on other factors, including gender, age, BMI, smoking history, blood glucose, and historical blood glucose levels. The process went as follows: first, I collected and visualized the data. During the clean-up process, I found some peculiarities, namely, a lot of information was missing in the smoking history category. I eventually chose to "interpolate" the data as a compromise, assuming that historical smoking would impact current health. There was insufficient data to claim otherwise due to the presence of many confounding factors.

In the end, I implemented four models and compared their performance. The first was a basic logistic regression, the second was a decision tree, the third was a deep learning model, and the last was a random forest. The random forest was found to be the best performing, which is not surprising given the non-linearity of the data. The deep learning model was close but had the significant downside of a lengthy training period. This project also includes a writeup. 

### [Excise rates and RTD Consumption](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Projects/RTD_Consumption)

In this project, I focused on determining whether the excise rate on Ready to Drink alcoholic beverages in Australia impacts the rate of consumption. I have included a short writeup PDF summarizing my findings that non-inflation-indexed increases have an impact, while those indexed to inflation have little effect.

### [Credit Card Fraud Detection](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Projects/Credit_Card_Fraud_detection)

A credit card fraud detection algorithm was developed for this project. I tried three different models: first, a logistic regression model, then a decision tree classifier, and finally, a deep learning model. The deep learning model was found to be the most successful, although the margins were close. However, it came with the downside of a significantly longer training time than the logistic regression and decision tree models, and compared their performance.

### [Mushrooms, Poisonous or Not?](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Projects/Mushroom_project)

This project involves a mushroom classification system that categorizes mushrooms into poisonous and non-poisonous categories. The classification tree was extremely successful, probably due to the clear categories (every mushroom is either poisonous or not) and the feature set being sufficient to accurately identify a mushroom. Therefore, sufficient layers resulted in almost perfect results.
## Machine Learning from Scratch

### [Regression](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Machine_Learning_from_Scratch/Regression_From_Scratch)
I have compiled 4 notebooks that cover creating linear, logistic, multilinear, and polynomial regression algorithms from scratch. In these notebooks, I first created synthetic data that followed the same pattern as the model with some added noise. Then, I developed an algorithm that uses gradient descent to zero in on the optimal solution.

### [Decision Trees](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Machine_Learning_from_Scratch/Decision_Trees) 
Here, I assembled a classification decision tree algorithm to classify data. In this project, I endeavored to adhere to an object-oriented approach. I used the IRIS dataset as a dummy dataset to aid with development, and later applied this project in the 'Mushrooms, Poisonous or Not?' project mentioned above, which proved to be quite successful, albeit a bit slow.
### [Clustering](https://github.com/suf102/Sufyan-Portfolio/tree/master/Machine_Learning_from_Scratch/Clustering)
Thus far I have put together a Kmeans++ clustering algorithm, I used synthetic data and built a clustering algorithm around it. I chose the Kmeans++ version because it is much quicker than just picking random points to start with. 
## Hackathons

### [MEV Hackathon](https://github.com/suf102/Data-and-Machine-Learning-Portfolio/tree/master/Hackathons/MEV_Hackathon)
In 2022, I competed in a MEV hackathon. You can find the full project, including its writeup, in the Hackathon folder.