#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:03:25 2016

@author: owais
"""

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    import numpy as np
    #compute all combinations
    combs = []
    N = len(choices)
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(1)
            else:
                combo.append(0)
        combs.append(np.array(combo))

    choices = np.array(choices)
    #find best combinations
    found = False
    goodcombs = []
    for item in combs:
        if sum(item*choices) == total:
            goodcombs.append(item)
    if len(goodcombs) > 0:
        found = True
    else:
        for item in combs:
            if sum(item*choices) <= total:
                goodcombs.append(item)
    goodcombs = np.array(goodcombs)

    counts=[]
    for item in goodcombs:
        mx = 0
        for i in range(len(item)):
            if item[i] == 1:
                mx+=1
        counts.append(mx)

    if found:
        return goodcombs[counts.index(min(counts))]
    else:
        return goodcombs[counts.index(max(counts))]

