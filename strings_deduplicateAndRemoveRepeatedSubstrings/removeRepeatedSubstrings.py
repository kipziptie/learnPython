#!/usr/bin/python3
##########################################
# Date: January  13, 2020
# Purpose:  To split a long string into substrings composed of unique characters
# Problem URL: https://www.hackerrank.com/challenges/merge-the-tools/problem 
##########################################

### 	Function: deDuplicate
# 	Purpose: Removes duplicate characters in a given string. This function returns 
#		a string of UNIQUE characters
# 		
#	Strategy: Utilizes the set() library to generate a hash table of every character in the #		string. To preserve character ordering, the result is assembled by iterating
#		over the original input string. Characters in the input string are hashed and
#		compared against the set to determine if it is unique. Unique Characters are
#		assembled in the same precedence that they were given - duplicates omitted.  
#		 
#		NOTE: This function is a good candidate for recursion 
###
def deDuplicate(line):
	arr = []
	ret = ""
	#print(line)
	x = set(line)
	#print("DeDupe: ", line, x)
	for i in range(0, len(line)):
		# val is the current character to test 
		val = set(line[i])
		
		# rightSubset is the string that occurs forward of the tested char
		rightSubset = set(line[i+1:])
		
		#DEBUG
		#print("test: ", val, "&", rightSubset, "Length: ", len(rightSubset))
		
		# Determine if current char occurs anywhere forward from it
		if (val.issubset(rightSubset)):
			#DEBUG
			#print("DUPLICATE FOUND")
			
			# check if this is the first instance of a duplicate
			if (not val.issubset(set(arr))):
				arr+=line[i]
		# If the character is unique 		
		elif (not val.issubset(set(arr))):
			arr+=line[i]
	
	#convert result array to a string	
	for i in arr:
		ret+=i		
	return (ret)			

### 	Function: deRepeat
# 	Purpose: Removes consecutively repeated characters in a string. 
#		Does NOT ensure uniqueness
# 		
#	Strategy:  Iterates over each character in a string and checks the adjacent 
#		character looking forward. If duplicate character is observed, skip
#		over it and check the next character. 
#		 
#		 
###

def deRepeat(line):
	i = 0
	
	#Store first char int result array. It's safe to assume unique array is empty. 
	ret = line[0]
	
	
	for i in range(0,len(line)):
		#Check the character next to current character - looking forward only
		# If adjacent is duplicate, skip over it
		if ret[len(ret)-1] == line[i]:
			# skip over this value
			#print("true")
			i= i+1	
		
		# Else adjacent char is not a duplicate. So save it in result array
		else:
			ret+=line[i]
	return(ret)
### Main ###
# Input Format
# The first line - A string of N characters
# The second line - A integer (K), where N / K = a WHOLE number 
# - The input line is split into N/K substrings
# - 
#
# Constraints
#  It is guaranteed that N is a multiple of K  
#
# Output Format
#  Substrings of length N/K composed of unique characters presented in order of precedence
#  
# 
###

arr = []
x = str(input())
k = int(input())
i = 0

# for every character in input string (x), break it into a chunk of size N/K, THEN 
# remove duplicate values from that chunk
for i in range(0,len(x),k):
	# DEBUG
	#print("(",i,",", i+k, ")")
	
	y = x[i:i+k]
	arr.append(deDuplicate(y))
	i= i+1

# Return the result to STDOUT
for i in arr:
	print (i)
