#!/usr/bin/python3
##########################################
# Date: January  7, 2020
# Purpose:  To convert a space separated list of number characters into a list of integers. 
# 	The integer array is then manupulated with numpy into a 3x3 numpy array 
#
# Challenge URL: https://www.hackerrank.com/challenges/np-concatenate/problem
##########################################
import numpy

### 	Function: getLine() 
# 	Purpose: Collects user input of space separated integers and returns a list
###		of integers
def getLine():
	x=str(input())
	return(list(map(int,x.split(' '))))

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
# Given two integer arrays; concatenate the arrays using numpy
#
#-Input Format
#The first line contains space separated integers representing the dimensions of the input arrays
#The next lines contains the space separated elements of the columns.
#After that, the next lines contains the space separated elements of the columns.
#
# Output Format
# Print the concatenated array
###
arrayDimensions = getLine()

array1 = getArray(arrayDimensions[0])
array2 = getArray(arrayDimensions[1])

#Debug
#print (array1)
#print (array2)

### RESULT ###
newarray = numpy.concatenate((array1, array2), axis = 0)
print (newarray)


