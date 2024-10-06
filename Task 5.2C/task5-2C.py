#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:51:27 2021
Task 5.2C
@author: leeeddison
"""
import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.stats
import pandas as pd
from sklearn import linear_model

# read csv into dataframe
data = pd.read_csv('admission_predict.csv')

# split the imported data between training and testing data
train_data = data[0:300]
test_data = data[300:400]

# build linear regression model for “TOEFL Score” and “Chance of Admit”
train_X = train_data['TOEFL Score'].values
train_X = np.c_[train_X]
train_Y = train_data['Chance of Admit'].tolist()
test_X = test_data['TOEFL Score'].values
test_X = np.c_[test_X]
test_Y = test_data['Chance of Admit'].tolist()
lr = linear_model.LinearRegression()
lr.fit(train_X, train_Y)
# build linear regression model for “CGPA” and “Chance of Admit”
train_X2 = train_data['CGPA'].values
train_X2 = np.c_[train_X2]
train_Y2 = train_data['Chance of Admit'].tolist()
test_X2 = test_data['CGPA'].values
test_X2 = np.c_[test_X2]
test_Y2 = test_data['Chance of Admit'].tolist()
lr2 = linear_model.LinearRegression()
lr2.fit(train_X2, train_Y2)

# specify plot area
fig,ax = plt.subplots(nrows=2, ncols=2, figsize=(14,10),dpi=100)

# plot regression line and predicted points along prediction line for TOEFL Score and Chance of Admit
scales = 20*np.ones(len(train_Y))
ax[0,0].scatter(train_X,train_Y,color='b',s=scales,alpha=0.7,edgecolor='r')
ax[0,0].set_xlabel('$X$ (TOEFL score)')
ax[0,0].set_ylabel('$Y$ (Chance of Admit)')
ax[0,0].set_title('Linear regression with TOEFL Score and Chance of Admit')
# plot the regression line
train_Yhat = lr.predict(train_X)
ax[0,0].plot(train_X,train_Yhat)

# plot regression line and predicted points along prediction line for CGPA
# and Chance of Admit
scales = 20*np.ones(len(train_Y2))
ax[1,0].scatter(train_X2,train_Y2,color='b',s=scales,alpha=0.7,edgecolor='r')
ax[1,0].set_xlabel('$X$ (CGPA)')
ax[1,0].set_ylabel('$Y$ (Chance of Admit)')
ax[1,0].set_title('Linear regression with CGPA and Chance of Admit')
# plot the regression line
train_Yhat2 = lr2.predict(train_X2)
ax[1,0].plot(train_X2,train_Yhat2)

# predict for unseen data
yhat_test = lr.predict(test_X)
yhat_test2 = lr2.predict(test_X2)

# plot the true values from testing set and the residual line for TOEFL Score and Chance of Admit
# plot the predicted points along the prediction line
scales = 30*np.ones(len(test_X))
ax[0,1].scatter(test_X,yhat_test,s=scales,color='b',edgecolor='r') #predicted points
ax[0,1].set_xlabel('$X$ (TOEFL)')
ax[0,1].set_ylabel('$Y$ (Chance of Admit)')
ax[0,1].set_title('TOEFL Score vs Chance of Admit: true value and residual')
ax[0,1].plot(test_X,yhat_test,color='b',linewidth=.2) #prediction line
# plot the true values
scales = 30*np.ones(len(test_X))
ax[0,1].scatter(test_X,test_Y,s=scales,color='g',edgecolor='b') #test y: true value
# plot the residual line
# get all the x coordinate (test_X) from the test dataset
tmp = np.reshape(test_X,[1,len(test_X)])[0]
tmp_x = []
tmp_y = []
for i in range(len(test_X)): #for each x in test set
    tmp_x = np.append(tmp_x,tmp[i]) #get x coordinate
    tmp_y = np.append(tmp_y,yhat_test[i]) #get predicted y coordinate
    tmp_x = np.append(tmp_x,tmp[i]) #get x coordinate again
    tmp_y = np.append(tmp_y,test_Y[i]) #get test y coordinate
    ax[0,1].plot(tmp_x,tmp_y,color='red',linewidth=0.5) #draw the vertical residual line (x,yhat), (x,test_y)
    tmp_x = []
    tmp_y = []

# plot the true values from testing set and the residual line for CGPA and Chance of Admit
# plot the predicted points along the prediction line
scales = 30*np.ones(len(test_X2))
ax[1,1].scatter(test_X2,yhat_test2,s=scales,color='b',edgecolor='r') #predicted points
ax[1,1].set_xlabel('$X$ (CGPA)')
ax[1,1].set_ylabel('$Y$ (Chance of Admit)')
ax[1,1].set_title('CGPA vs Chance of Admit: true value and residual')
ax[1,1].plot(test_X2,yhat_test2,color='b',linewidth=.2) #prediction line
# plot the true values
scales = 30*np.ones(len(test_X2))
ax[1,1].scatter(test_X2,test_Y2,s=scales,color='g',edgecolor='b') #test y: true value
# plot the residual line
# get all the x coordinate (test_X) from the test dataset
tmp = np.reshape(test_X2,[1,len(test_X2)])[0]
tmp_x = []
tmp_y = []
for i in range(len(test_X2)): #for each x in test set
    tmp_x = np.append(tmp_x,tmp[i]) #get x coordinate
    tmp_y = np.append(tmp_y,yhat_test2[i]) #get predicted y coordinate
    tmp_x = np.append(tmp_x,tmp[i]) #get x coordinate again
    tmp_y = np.append(tmp_y,test_Y2[i]) #get test y coordinate
    ax[1,1].plot(tmp_x,tmp_y,color='red',linewidth=0.5) #draw the vertical residual line (x,yhat), (x,test_y)
    tmp_x = []
    tmp_y = []



