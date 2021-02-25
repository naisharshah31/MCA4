#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install apyori


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
import pyfpgrowth
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix 


# In[9]:


dataset = pd.read_csv('dataset.csv', header = None)
print("Dataset Length : ", len(dataset))
print("Dataset shape : ", dataset.shape)

print("Pre-processing the Dataset ..... ")

print(dataset.isnull().sum()) 
#df['columnName'].fillna(value=df['columnName'].mean()) # if there are missing values. then execute this code
print("In this case, there are no missing values")
dataset=dataset.drop(dataset.columns[[0, 1, 2,4,5]], axis = 1 ) # taking only the relevant columns 


# In[13]:


X=dataset[dataset.columns[1:13]] 
Y=dataset[3]
print(X)


X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.3, random_state=100)
print("Length of X_train : ", len(X_train))
print("Length of X_test : ", len(X_test))


# In[11]:


def aprioriAlgorithm():
    print (" Apriori Algorithm ")
    
    records = []
    for i in range(0, 829):
        records.append([str(dataset.values[i,j]) for j in range(0,6 )])
    association_rules=apriori(records, min_support=0.0045,min_confidence=0.2, min_lift=3, min_length=2)
    association_results = list(association_rules)
    print(len(association_results))
    for i in range(0,5):
        print(association_results[i])
    print("________________________________________")

    for item in association_results:
        pair = item[0]
        items = [x for x in pair]
    print("Rule: " + items[0] + "-->" + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("________________________________________")
    return

def decisionTree():
    X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.3, random_state=100)
    print("Length of X_train : ", len(X_train))
    print("Length of X_test : ", len(X_test))
    print("___________________Result using Entropy__________________")

    clf_entropy=DecisionTreeClassifier(criterion="entropy",random_state=100, max_depth=3, min_samples_leaf=5)
    clf_entropy.fit(X_train,y_train) # fitting the data

    print("This tree would have 3 layers and 5 leaf nodes")
    y_pred_en=clf_entropy.predict(X_test)
    print(y_pred_en)
    print("Accuracy : ", accuracy_score(y_test,y_pred_en)*100)

    print("Confusion Matrix with size ",confusion_matrix(y_test, y_pred_en).shape)
    print( confusion_matrix(y_test, y_pred_en))  

    print("___________________Result using Gini_____________________")

    clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,max_depth=3, min_samples_leaf=5) 
    clf_gini.fit(X_train, y_train) 
    y_pred_gini=clf_gini.predict(X_test)
    print(y_pred_gini)
    print("Accuracy : ", accuracy_score(y_test,y_pred_gini)*100)
    print("Confusion Matrix with size ",confusion_matrix(y_test, y_pred_gini).shape)
    print( confusion_matrix(y_test, y_pred_gini)) 


choice = 0
while choice!=3:
    
    print("1.Apriori Algorithm")
    print("2.Decision Tree")
    print("3.Exit")
    choice = int(input("Enter the choice : "))
    if(choice == 1):
        aprioriAlgorithm()
        
        break
    elif(choice == 2):
        decisionTree()
        
        break
    elif(choice == 3):
        break
    else:
        print("Invalid Choice")


# In[ ]:




