#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:43:10 2021

@author: leeeddison
"""
# import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read data from csv file and place in dataframe and array
data_df = pd.read_csv('Malicious_or_criminal_attacks_breakdown-Top_five_industry_sectors_July-Dec-2019.csv', index_col = 0, engine='python')
data = data_df.to_numpy()

# set labels, categories and colors
labels = ['Health service providers', 'Finance', 'Education', 'Legal accounting & management services', 
          'Personal services']

categories = ['Cyber incident', 'Theft of paperwork or data storage device', 'Rogue employee/insider threat', 
              'Social engineering/impersonation']

colors = ['red', 'yellow', 'blue', 'green']

x_pos = np.arange(len(labels))

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 5), dpi=100)

# set width of bars for erach graph
w1 = 0.2
w2 = 0.4

# populate graph 1 and graph 2 with data and information
for i in range(len(data)):
    ax[0].bar(x_pos+w1*i, data[i], width=w1, align='center', label=categories[i], color=colors[i])
    ax[1].bar(x_pos, data[i,:], width=w2, align='center', label=categories[i], color=colors[i],
      bottom = np.sum(data[:i], axis = 0))

# set titles and axis for graph 1
ax[0].set_ylabel("Number of attacks")
ax[0].set_title("Type of attack by top five industry sectors")
ax[0].set_xticks(x_pos+w1)
ax[0].set_xticklabels(labels, rotation=90)
ax[0].legend(loc=0)

# set titles and axis for graph 2
ax[1].set_ylabel("Number of attacks")
ax[1].set_title("Type of attack by top five industry sectors")
ax[1].set_xticks(x_pos)
ax[1].set_xticklabels(labels, rotation=90)
ax[1].legend(loc=0)