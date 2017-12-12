#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 01:12:09 2016

@author: owais
"""

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if not title == None:
        pylab.title(title)
    pylab.show()   
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    trials = []
    for i in range(numTrials):
        l = []
        for j in range(numRolls):
            l.append(die.roll())
        mx = 1
        ln = len(l)
        for i in range(ln):
            m = 1
            for j in range(1,ln - i):
                if l[i] == l[i+j]:
                    m+=1
                else:
                    break
            if m > mx:
                mx = m
        trials.append(mx)
    makeHistogram(trials,10,'Longest Run','Frequency')
    return getMeanAndStd(trials)[0]
        
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))