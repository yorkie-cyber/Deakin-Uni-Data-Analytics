#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:30:22 2021

@author: leeeddison
"""
# import numpy and pandas
import numpy as np
import pandas as pd

fail_df = pd.DataFrame

# load results.csv and place into dataframe
csv_df = pd.read_csv('result_withoutTotal.csv', index_col = 0)
csv_df.head()

# calculate total column for each student
csv_df['Total'] = 0.05*(csv_df['Ass1']+csv_df['Ass3']) + 0.15*(csv_df['Ass2']+csv_df['Ass4']) + 0.6*csv_df['Exam']
csv_df['Total'] = csv_df['Total'].round(decimals=3)
# check if total is greater than 100 and reduce to 100 if it is
csv_df.loc[csv_df['Total'] > 100, 'Total'] = 100

# calculate final column
csv_df['Final'] = csv_df['Total'].round(decimals=0).astype(int)

# add in hurdle marking
# check if hurdle achieved and if final is greater than 44
csv_df.loc[(csv_df['Exam'] < 48) & (csv_df['Final'] >44), 'Final'] = 44
# create grade column based on final result
grades = [
    (csv_df['Final'] <= 49.45),
    (csv_df['Final'] > 49.45) & (csv_df['Final'] <= 59.45),
    (csv_df['Final'] > 59.45) & (csv_df['Final'] <= 69.45),
    (csv_df['Final'] > 69.45) & (csv_df['Final'] <= 79.45),
    (csv_df['Final'] > 79.45)]
choices = ['N','P','C', 'D', 'HD']
csv_df['Grade'] = np.select(grades, choices, default='')

# create dataframe containing students with exam score less than 48
fail_df = csv_df[csv_df['Exam'] < 48]


# write all students new columns and values to result_updated csv and txt files
csv_df.to_csv('result_updated.csv')
csv_df.to_csv('result_updated.txt')
# write students with exam below 48 to failedhurdle csv and txt files
fail_df.to_csv('failedhurdle.csv')
fail_df.to_csv('failedhurdle.txt')

# display data file with 3 new columns
print(csv_df)
# display the students with exam score <48
print("\nStudents with exam score < 48")
print(csv_df[csv_df['Exam'] < 48])
# display the students with exam score >100
print("\nStudents with exam score > 100")
print(csv_df[csv_df['Exam'] > 100])
