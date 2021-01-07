#!/usr/bin/python3
##########################################
# Date: January  5, 2020
# Purpose:  To convert a space separated list of number characters into a list of integers. 
# 	The integer array is then manupulated with numpy into a 3x3 numpy array 
#
# Challenge URL: https://www.hackerrank.com/challenges/np-shape-reshape/problem
##########################################

import numpy

input = str(input())

# convert the user input string of space separated characters into a list of numbers
array = list(map(int, input.split(' ')))

print (numpy.reshape(array,(3,3)))



