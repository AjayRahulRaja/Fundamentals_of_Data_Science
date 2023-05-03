# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:10:56 2023

@author: Ajay
"""

import numpy as np
import matplotlib.pyplot as plt

# reading data from the datafile, located at same dir as the .Py code
# and storing it in an array
arr = np.genfromtxt('data1.csv', delimiter = ',')
type(arr)

# creating another array, representing the distribution of newborn weights in a given dataset
counts, bins = np.histogram(arr, bins = 40, range = [2.0, 5.0])
print("The counts are", counts.size)
print("Bin range are", bins.size)

# arr.max() = 4.63233
# arr.min() = 2.23214

#calculating bincenter and binwidth from the histogram distribution
bincenter = 0.5 * (bins[1:] + bins[:-1])
binwidth = bins[1:] - bins[:-1]

#normalising the counts before plotting the histogram
counts_norm = counts / np.sum(counts)
print("bincenter is ", bincenter.size)
print("Normalised count is ",counts_norm.size)

cum_sum = np.cumsum(counts_norm)
print("The cummulative sum is :", cum_sum)

# calculating the average weight of newborn babies in the given region
W = np.sum(counts_norm * bincenter)

# using the distribution to calculate another value, X
# The value of X is such that 33% of newborns from the distribution are born with a weight above X
X = np.argmin(np.abs(cum_sum - 0.67))
X = bincenter[X]

print("Mean value is: ", W)
print("X value is: ", X)

x_bar = counts_norm * (bincenter >= X)

plt.figure(figsize = (6, 4))
# plotting the array as a histogram
plt.style.use("ggplot")
plt.gca().set_facecolor('lightgrey')

#distribution
plt.bar(bincenter, counts_norm, width = 0.88 * binwidth, color = "royalblue", label = "New born babies distribution")

#mean value
plt.plot([W, W], [0, np.max(counts_norm) + 0.002], 'k--', c = "black")
plt.text(W + 0.05, 0.081, "Mean value is 3.3921", c = "black", fontsize = 10)

#X value
plt.bar(bincenter, x_bar, width = 0.88 * binwidth, alpha = 0.5, color = "limegreen", label = "33% of newborns are born with a weight above X")
plt.text(X+0.35, 0.055, "<-- X value is 3.6125", c = "black", fontsize = 10)

plt.title("Distribution of weight of new born babies in certain regions of Europe", fontsize = 10)
plt.xlabel("Weight of newborn babies", fontsize = 10)
plt.ylabel("Probability", fontsize = 10)
plt.xlim(2.0, 5.0, 0.5)
plt.ylim(0.00, 0.09, 0.01)
leg = plt.legend(bbox_to_anchor = (1.01, 0.99), fontsize = 10)
leg.get_frame().set_facecolor('lightgrey')
plt.savefig('plot.png', dpi = 300, bbox_inches = 'tight')
plt.show()
