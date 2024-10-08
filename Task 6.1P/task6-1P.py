#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:03:55 2021

@author: leeeddison
Task 6.1P
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import Series, DataFrame
import csv
from sklearn import neighbors
from matplotlib.colors import ListedColormap

#To switch to seaborn defaults, simply call the set() function.
sns.set()

weights='uniform'

# read in data from csv file
data = pd.read_csv('task6_1_dataset.csv', names=["x1", "x2", "y"], header=0)

# place x1, x2, and y data values based on class
class_1 = data[data['y'] == 0]
class_2 = data[data['y'] == 1]
class_3 = data[data['y'] == 2]

# split x and y graph values from x1 and x2 columns
X11 = class_1['x1'].tolist()
X12 = class_1['x2'].tolist()
X21 = class_2['x1'].tolist()
X22 = class_2['x2'].tolist()
X31 = class_3['x1'].tolist()
X32 = class_3['x2'].tolist()

# set n_per_class to 50
n_per_class = 50
colors = ['green', 'blue', 'magenta']
# set scale and alpha
scale = 75
alpha = 0.6

# plot graph with 3 classes
fig, ax  = plt.subplots(figsize=(7, 7), dpi=100)
ax.scatter(X11, X12, alpha=alpha, color=colors[0], s=scale)
ax.scatter(X21, X22, alpha=alpha, color=colors[1], s=scale)
ax.scatter(X31, X32, alpha=alpha, color=colors[2], s=scale)
ax.set_title("synthesized data for 3 classes")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
# place test point at [-4, 8]
ax.annotate("(-4, 8), test point", (-3.5, 8), c='r')
ax.scatter(-4, 8, marker="x", s=scale, lw=2, c='r')

# second graph
#concatenate all the arrays along row axis  
x1 = np.r_[X11, X21, X31]
x2 = np.r_[X12, X22, X32]
#concatenate x1 and x2 into x_train
x_train = np.c_[x1, x2]
y_train = np.r_[0*np.ones(n_per_class), 1*np.ones(n_per_class), 2*np.ones(n_per_class)]
k = 15
knn = neighbors.KNeighborsClassifier(k, weights=weights)
knn.fit(x_train, y_train)
#create an input to predict its label
x_test = [[-2, 5]]
y_pred = knn.predict(x_test)

# step size in the mesh
h = 0.05
# Create colour maps
cmap_light = ListedColormap(['#AAFFAA', '#AAAAFF', '#FFAAAA'])
cmap_bold = ListedColormap(['green', 'blue', 'magenta'])
x1_min, x1_max = x_train[:, 0].min() - 1, x_train[:, 0].max() + 1
x2_min, x2_max = x_train[:, 1].min() - 1, x_train[:, 1].max() + 1
xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, h), np.arange(x2_min, x2_max, h))

Z = knn.predict(np.c_[xx1.ravel(), xx2.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx1.shape)

#create the subplot for graph two
fig,ax1 = plt.subplots(figsize=(7, 7))
ax1.pcolormesh(xx1, xx2, Z, cmap=cmap_light)
ax1.set_title("3-Class classification (k = {})\n test point is predicted as class {}".format(k, colors[y_pred.astype(int)[0]]))
# plot training points
ax1.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap=cmap_bold, alpha=alpha, s=scale)
# place 2nd test point at [-2, 5] and annotate
ax1.annotate('(-2,5) test point', xy=(-1.5, 5), c='r')
ax1.scatter(x_test[0][0], x_test[0][1], marker="x", s=scale, lw=2, c='r')