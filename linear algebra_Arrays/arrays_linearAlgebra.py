#!/usr/bin/python3
##########################################
# Date: January  5, 2020
# Purpose:  To learn how to use the linear algebra library
# Problem URL: https://www.hackerrank.com/challenges/np-linear-algebra/problem
##########################################
import numpy

### 	Function: getLine() 
# 	Purpose: Collects user input of space separated integers and returns a list
###		of integers
def getLine():
	x=str(input())
	return(list(map(float,x.split(' '))))

### 	Function: getLine(index) 
# 	Purpose: Builds an array from STDIN when given the number of lines to read (index)  
# 		
#	Strategy: Appends small lists provided by getLine() to an empty list. This represents
#		 a larger array composed of small identically sized lists
#		 
###
def getArray(index):
	val = []
	for i in range(0,index):
		#x=str(input())
		#val.append(list(map(int,x.split(' '))))
		val.append(getLine())
	return (val)

### Main ###
# Input Format
# The first line read represents the number (N) of rows & columns for the incoming array
# The next N lines are the contents of the array
# - 
#
# Output Format
#  The output is the determinant of the input array
#  
###

x = getLine()
y = getArray(x[0])

# DEBUG
#print (x)
#print (y)

### RESULT ###
print (numpy.linalg.det(y))


