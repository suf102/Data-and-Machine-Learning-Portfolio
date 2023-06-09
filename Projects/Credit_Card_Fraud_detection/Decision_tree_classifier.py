import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os 

#First the nodes 
class node():
    def __init__(self, feature_index=None, threshold=None, left=None,right=None,info_gain=None,value=None):
        
        #for decision nodes
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.info_gain = info_gain 
        
        #for the leaves 
        
        self.value = value
        
#Then the tree itself 
class Tree_classifier():
    def __init__(self,min_samples_split =2 ,max_depth = 2):
        
        #initializing the tree itself
        
        self.root = None 
        
        # Stopping conditions
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth 
        
    def build_tree(self,dataset, curr_depth = 0):
        #building the tree recursively itterating through the levels ensuring at each level there is a left and right split
        X = dataset[:,:-1]
        Y = dataset[:,-1]
        num_samples, num_features = np.shape(X)
        
        # Making sure the tree only runs while there are enough samples or we are above the max depth
        
        
        if num_samples >=self.min_samples_split and curr_depth<=self.max_depth:
            # then we want to find the best split for the data we have at the level we are at
            best_split = self.get_best_split(dataset,num_samples,num_features,)
            #Make sure that the split that we do make increases the amount of information we have
            if best_split["info_gain"]>0:
                #Building the left and right subtrees 
                left_subtree = self.build_tree(best_split["dataset_left"],curr_depth+1 )
                right_subtree = self.build_tree(best_split["dataset_right"],curr_depth+1 )
                # Returning the node as a object from above
                return node(best_split["feature_index"], best_split["threshold"], left_subtree, right_subtree, best_split["info_gain"])
                
        # if on the other hand we are at out final depth, instead we will create the leaf nodes
        leaf_value = self.calculate_leaf_value(Y)
        # Then calling the plotting function after all of the plots have been made
        plt.show
        return node(value= leaf_value)
    
    def get_best_split(self, dataset,num_samples, num_features):
        # for each non leaf node, finding out what the best thresholds are to split the data
        # First make somewhere to store the best split 
        best_split = {}
        max_info_gain = -float("inf")
        
        
        # Loop over all of the features to find the best split
        for feature_index in range(num_features):
            # grab just the features from the set
            feature_values = dataset[:,feature_index]
            #next isolate the possible thesholds by pulling out just the unique values from the dataset
            possible_thesholds = np.unique(feature_values)
            # Looping over the various thresholds to find the best one
            for threshold in possible_thesholds:
                dataset_left , dataset_right = self.split(dataset,feature_index, threshold)
                # Check that children aren't null if it is then we are done we dont need to go any further if they are not we need to split the dataset further
                if len(dataset_left)>0 and len(dataset_right)>0:
                    # Splitting the dataset into the labels for the  left and right branches  
                    y  = dataset[:,-1] 
                    left_y = dataset_left[:,-1]
                    right_y =  dataset_right[:,-1]
                    # Compute the gini coefficient to see if it is a improvement 
                    curr_info_gain = self.information_gain(y,left_y,right_y,"gini")
                    # Check to see if this is the best split and if it is update all of our values 
                    if curr_info_gain > max_info_gain:
                        best_split["feature_index"] = feature_index
                        best_split["threshold"] = threshold
                        best_split["dataset_left"] = dataset_left
                        best_split["dataset_right"] = dataset_right
                        best_split["info_gain"] = curr_info_gain
                        max_info_gain = curr_info_gain
                        
        # # Return a plot of the best way to partition the data, making sure we dont consider the leaf nodes that don't have any information gain
        # if max_info_gain != 0:
        #     data = np.copy(dataset)
        #     index_of_feature = best_split["feature_index"]
        #     x = data[:,index_of_feature]
        #     colours = data[:,-1]
        #     y_0 = np.delete(data, index_of_feature , axis=1)
        #     y_1 = np.delete(y_0, np.shape(y_0)[1]-1 , axis=1)
        #     random_column = np.random.choice(np.shape(y_1)[1])
        #     y = y_1[:,random_column]
        #     target_data = df.columns[index_of_feature -1]
        #     plt.xlabel(target_data)
        #     plt.ylabel(df.columns[random_column])
        #     plt.scatter(x=x,y=y,c =colours)
        #     plt.axvline(x = best_split["threshold"], color = 'b', label = 'Best split threshold')
        #     save_dir = '../Decision_Trees/Decision_Tree_Classification_plots/'
        #     plt.savefig(save_dir+f'Threshold_on_the_{target_data}_splitting_the_data_with_info_gain_of_{max_info_gain}.png')
        #     plt.clf()
        # Return the data 
        
        return best_split
    
    def split(self,dataset,feature_index,threshold):
        # the function to actually split the data according to the possible different thresholds
        dataset_left = np.array([row for row in dataset if row[feature_index]<=threshold])
        dataset_right = np.array([row for row in dataset if row[feature_index]>threshold])
        return dataset_left , dataset_right
    
    def information_gain(self, parent, l_child, r_child, mode="entropy"):
            # computing the information gain 
        weight_l = len(l_child)/ len(parent)
        weight_r = len(r_child)/ len(parent)
        if mode == "gini":
            gain = self.gini_index(parent) - (weight_l*self.gini_index(l_child)+weight_r*self.gini_index(r_child))
        else:
            gain = self.entropy(parent) - (weight_l*self.entropy(l_child)+weight_r*self.entropy(r_child))
        return gain
    
    def entropy(self, y):
        # a function that will compute entropy of the information sate
        # pull all the different possible labels so we know how many different objects we are classifying. 
        class_labels = np.unique(y)
        
        entropy = 0 
        # iterating through the different class labels
        for cls in class_labels:
            p_cls = len(y[y==cls])/len(y)
            # This number will be closer to one the better the classification 
            entropy += - p_cls * np.log(p_cls)
        return entropy

    def gini_index(self, y):
        #This method will work out the gini index of the tree
        # pull all the different possible labels so we know how many different objects we are classifying. 
        class_labels = np.unique(y)
        
        gini = 0 
        for cls in class_labels:
            p_cls = len(y[y == cls]) / len(y)
            gini += p_cls**2
            return 1 - gini 
        
    def calculate_leaf_value(self, Y):
        # work out the value of each leaf
        
        Y = list(Y)
        return max(Y, key=Y.count)
    
    def print_tree(self, tree=None, indent=" "):
        #Print out the tree
        
        if not tree:
            tree = self.root

        if tree.value is not None:
            print(tree.value)

        else:
            print("X_"+str(tree.feature_index), "<=", tree.threshold, "?", tree.info_gain)
            print("%sleft:" % (indent), end="")
            self.print_tree(tree.left, indent + indent)
            print("%sright:" % (indent), end="")
            self.print_tree(tree.right, indent + indent)  
            
    def fit(self, X, Y):
        # actually fit the tree
        # put the x and y sections of the data set together
        dataset = np.concatenate((X,Y), axis=1)
        #build the tree
        self.root = self.build_tree(dataset)
    
    def predict(self, X):
        predictions = [self.make_prediction(x,self.root) for x in X]
        return predictions
        
    def make_prediction(self, x, tree):
        # take our out of sample dataset and use it to make a prefiction to evaluate the model
        if tree.value != None:
            return tree.value
        feature_value = x[tree.feature_index]
        if feature_value <= tree.threshold:
            return self.make_prediction(x,tree.left)
        else: 
            return self.make_prediction(x, tree.right)
        