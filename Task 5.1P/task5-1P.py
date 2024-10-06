#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 07:54:57 2021

@author: leeeddison
"""
import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.stats
import pandas as pd

# read data from csv file and place in dataframe
df = pd.read_csv('data_correlation.csv')
# store columns in indivdual arrays
a = df['a']
b = df['b']
c = df['c']
d = df['d']

# Pearson's-r coefficient and corrcoef() for a and b
pearson_r_a = np.cov(a, b)[0, 1] / (a.std() * b.std())
print("a and b pearson_r:", pearson_r_a)
print("a and b corrcoef: ", np.corrcoef(a,b))
# Pearson's-r coefficient and corrcoef() for a and c
pearson_r_b = np.cov(a, c)[0, 1] / (a.std() * c.std())
print("a and c pearson_r:", pearson_r_b)
print("a and c corrcoef: ", np.corrcoef(a,c))
# Pearson's-r coefficient and corrcoef() for a and d
pearson_r_c = np.cov(a, d)[0, 1] / (a.std() * d.std())
print("a and d pearson_r:", pearson_r_c)
print("a and d corrcoef: ", np.corrcoef(a,d))

# plotting for a and b
fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
#s: marker size; color: marker color; alpha: marker opacity.
ax.scatter(a,b, alpha=0.6, edgecolor='none', s=100)
# set axis labels
ax.set_xlabel('a')
ax.set_ylabel('b')

#Fit a polynomial p(x) = p[0] * x**deg + ... + p[deg] of degree deg to points (x, y). 
line_coef = np.polyfit(a, b, 1)
xx = np.arange(0, 50, 0.1)
yy = line_coef[0]*xx + line_coef[1]
# check if coefficient is strong, if not then don't plot line
if abs(pearson_r_a) > 0.5:
    ax.plot(xx, yy, 'r', lw=2)

# plotting for a and c
fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
#s: marker size; color: marker color; alpha: marker opacity.
ax.scatter(a,c, alpha=0.6, edgecolor='none', s=100)
# set axis labels
ax.set_xlabel('a')
ax.set_ylabel('c')

#Fit a polynomial p(x) = p[0] * x**deg + ... + p[deg] of degree deg to points (x, y). 
line_coef = np.polyfit(a, c, 1)
xx = np.arange(0, 50, 0.1)
yy = line_coef[0]*xx + line_coef[1]
# check if coefficient is strong, if not then don't plot line
if abs(pearson_r_b) > 0.5:
    ax.plot(xx, yy, 'g', lw=2)

# plotting for a and c
fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
#s: marker size; color: marker color; alpha: marker opacity.
ax.scatter(a,d, alpha=0.6, edgecolor='none', s=100)
# set axis labels
ax.set_xlabel('a')
ax.set_ylabel('d')

#Fit a polynomial p(x) = p[0] * x**deg + ... + p[deg] of degree deg to points (x, y). 
line_coef = np.polyfit(a, d, 1)
xx = np.arange(0, 50, 0.1)
yy = line_coef[0]*xx + line_coef[1]
# check if coefficient is strong, if not then don't plot line
if abs(pearson_r_c) > 0.5:
    ax.plot(xx, yy, 'g', lw=2)