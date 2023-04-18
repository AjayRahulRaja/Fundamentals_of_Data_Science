# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:58:27 2023

@author: Ajay
"""

import numpy as np
import matplotlib.pyplot as plt

# reading the data from a datafile located at the same directory as the Python code, and storing it in an array;
url = 'https://raw.githubusercontent.com/AjayRahulRaja/Fundamentals_of_Data_Science/main/coding_project/data1.csv'
arr = np.genfromtxt(url, delimiter=',')
type(arr)

# creating another array, representing the distribution of newborn weights in a given dataset
counts, bins = np.histogram(arr, bins=400)

# using the distribution to calculate W, the average weight of newborn babies in the given region
W = np.mean(bins)
# using the distribution to calculate another value, X
# The value of X should be such that 33% of newborns from the distribution are born with a weight above X.
X = np.percentile(bins, 100-33)

# finding the cumulative counts (y-axis)
cum_sum = np.cumsum(counts)
#adding 0 to the cumulative sum as it's size does not match the distribution's size
cum_sum = np.append(cum_sum, 0)

# plotting the array as a histogram
plt.figure(figsize=(6,4))
plt.style.use('ggplot')
new_arr = np.vstack((bins, cum_sum))
plt.axvline(X, ls='--', color='green', label='new born babies above 33%')
plt.text(X, 300, f' {np.round(X, 4)}', c='black')
plt.axvline(W, ls='--', color='blue', label='average weigth of newborn babies')
plt.text(W-.45, 100, f' {np.round(W, 4)}', c='black')
plt.bar(new_arr[0], new_arr[1])
plt.title("Distribution of new born babies in certain regions of Europe", fontsize=10)
plt.xlabel("Distribution", fontsize=10)
plt.ylabel("Cummulative counts", fontsize=10)
plt.legend(bbox_to_anchor=(1.02, 0.99))
plt.xlim(1.5, 5.0, 0.5)
plt.ylim(0, 410, 50)
# plt.savefig('C:/Users/Lenovo/Desktop/UK/Hertfordshire/SEM 01/Fundamentals of Data Science/coding project/plot.png', dpi=300, bbox_inches='tight')
plt.show()
