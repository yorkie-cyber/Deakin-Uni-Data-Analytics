#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:34:34 2021

@author: leeeddison
"""
# import numpy and pandas
import numpy as np
import pandas as pd

# load results.csv and place into dataframe
csv_df = pd.read_csv('result_withoutTotal.csv', index_col = 0)
csv_df.head()

# find and print out the average, minimum and maximum from assessment 1
print("---------------------------------------------------------------------")
print("Assessment 1 Average", csv_df.Ass1.mean())
print("Assessment 1 Minimum", csv_df.Ass1.min())
print("Assessment 1 Maximum", csv_df.Ass1.max())
# find and print out the average, minimum and maximum from assessment 2
print("---------------------------------------------------------------------")
print("Assessment 2 Average:", csv_df.Ass2.mean())
print("Assessment 2 Minimum:", csv_df.Ass2.min())
print("Assessment 2 Maximum:", csv_df.Ass2.max())
# find and print out the average, minimum and maximum from assessment 3
print("---------------------------------------------------------------------")
print("Assessment 2 Average:", csv_df.Ass3.mean())
print("Assessment 2 Minimum:", csv_df.Ass3.min())
print("Assessment 2 Maximum:", csv_df.Ass3.max())
# find and print out the average, minimum and maximum from assessment 4
print("---------------------------------------------------------------------")
print("Assessment 3 Average:", csv_df.Ass4.mean())
print("Assessment 3 Minimum:", csv_df.Ass4.min())
print("Assessment 3 Maximum:", csv_df.Ass4.max())
# find and print out the average, minimum and maximum from exam
print("---------------------------------------------------------------------")
print("Exam Average:", csv_df.Exam.mean())
print("Exam Minimum:", csv_df.Exam.min())
print("Exam Maximum:", csv_df.Exam.max())

# find and print student(s) with highest assessment 1 mark
print("---------------------------------------------------------------------")
highestMarks_df = csv_df[csv_df['Ass1'] == csv_df.Ass1.max()]
print ("Student(s) with highest Assessment 1 mark:")
print(highestMarks_df)
# find and print student(s) with highest assessment 2 mark
print("---------------------------------------------------------------------")
print ("Student(s) with highest Assessment 2 mark:")
highestMarks_df = csv_df[csv_df['Ass2'] == csv_df.Ass2.max()]
print(highestMarks_df)
# find and print student(s) with highest assessment 2 mark
print("---------------------------------------------------------------------")
print ("Student(s) with highest Assessment 3 mark:")
highestMarks_df = csv_df[csv_df['Ass3'] == csv_df.Ass3.max()]
print(highestMarks_df)
# find and print student(s) with highest assessment 2 mark
print("---------------------------------------------------------------------")
print ("Student(s) with highest Assessment 4 mark:")
highestMarks_df = csv_df[csv_df['Ass4'] == csv_df.Ass4.max()]
print(highestMarks_df)
# find and print student(s) with highest exam mark
print("---------------------------------------------------------------------")
print ("Student(s) with highest Exam mark:")
highestMarks_df = csv_df[csv_df['Exam'] == csv_df.Exam.max()]
print(highestMarks_df)