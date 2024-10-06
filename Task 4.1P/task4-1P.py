#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:37:21 2021

@author: leeeddison
"""
# import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import attack data from csv file
data_df = pd.read_csv('attack-type-frequency.csv', index_col=0, engine='python')

# set labels and colors
labels = ['DOS', 'PROBE', 'R21', 'U2R']
colors = ['blue', 'red', 'green', 'yellow']

# group by category information
attack_counts = (data_df.groupby(['category']).size())

fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
# set positions to length of labels
x_pos = np.arange(len(labels))

# populate graph with data
ax.barh(x_pos, attack_counts, align='center', color=colors)
# set titles and axis for graph 
ax.set_ylabel("Attack categories")
ax.set_xlabel("Number of attack types in each category")
ax.set_title("Attack categories and num of attack types in Cyber Security")
ax.set_yticks(x_pos)
ax.set_yticklabels(labels)

# pie chart
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(attack_counts, labels=labels, colors=colors, autopct='%1.1f')