#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:24:11 2021

@author: leeeddison
"""
import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.stats
import pandas as pd
from sklearn import linear_model
from sklearn import neighbors
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# tree plotting function
def plot_feature_importances_fraud(model):
    #plot2 = plt.figure(2)
    n_features = x.shape[1]
    plt.figure(figsize=(7,7), dpi=100)
    plt.barh(np.arange(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), x.columns.tolist())
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)
    plt.show()

# read in data from csv file
df = pd.read_csv('payment_fraud.csv')
df = pd.get_dummies(df, columns=['paymentMethod'])

# split data in to training and test using 0.33
y = df['label']
x = df.drop('label', axis=1)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# build logistic regression models and print test scores
logreg = LogisticRegression().fit(X_train, y_train)
print("--- C=1 ---")
print("Training set score: {:.3f}".format(logreg.score(X_train, y_train)))
print("Test set score: {:.3f}".format(logreg.score(X_test, y_test)))
logreg10 = LogisticRegression(C=10).fit(X_train, y_train)
print("--- C=10 ---")
print("Training set score: {:.3f}".format(logreg10.score(X_train, y_train)))
print("Test set score: {:.3f}".format(logreg10.score(X_test, y_test)))
logreg100 = LogisticRegression(C=100).fit(X_train, y_train)
print("--- C=100 ---")
print("Training set score: {:.3f}".format(logreg100.score(X_train, y_train)))
print("Test set score: {:.3f}".format(logreg100.score(X_test, y_test)))
logreg001 = LogisticRegression(C=0.01).fit(X_train, y_train)
print("--- C=0.01 ---")
print("Training set score: {:.3f}".format(logreg001.score(X_train, y_train)))
print("Test set score: {:.3f}".format(logreg001.score(X_test, y_test)))
logreg0001 = LogisticRegression(C=0.001).fit(X_train, y_train)
print("--- C=0.001 ---")
print("Training set score: {:.3f}".format(logreg0001.score(X_train, y_train)))
print("Test set score: {:.3f}".format(logreg0001.score(X_test, y_test)))

# plot logistic regression graph
plt.figure(figsize=(7,7), dpi=100)
plt.plot(logreg.coef_.T, 'o', label="C=1")
plt.plot(logreg10.coef_.T, '<', label="C=10")
plt.plot(logreg100.coef_.T, '^', label="C=100")
plt.plot(logreg001.coef_.T, 'v', label="C=0.001")
plt.plot(logreg0001.coef_.T, '>', label="C=0.0001")
xlims = plt.xlim()
plt.xticks(range(x.shape[1]), x.columns.tolist(), rotation=90)
plt.hlines(0, xlims[0], xlims[1])
plt.xlim(xlims)
plt.ylim(-5, 5)
plt.xlabel("Feature")
plt.ylabel("Coefficient magnitude")
plt.legend()
plt.show()

# Decision tree work
tree = DecisionTreeClassifier(max_depth=4, random_state=0)
tree.fit(X_train, y_train)
# print decision tree depth, training and test set, feature importances
print("\nDecision tree depth: {:.0f}".format(tree.max_depth))
print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))
print("Feature importances: ", tree.feature_importances_)

# call tree plot function
plot_feature_importances_fraud(tree)