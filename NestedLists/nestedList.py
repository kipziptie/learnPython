#!/usr/bin/python3
##########################################
# Date: January  5, 2020
# Purpose: learn how to use a nested list
# Challenge URL: https://www.hackerrank.com/challenges/nested-list/problem
# Strategy: Lists are nested up to 3 times deep in this implementation. 
# The result is one list item per numeric grade
#
# References: https://www.learnbyexample.org/python-nested-list/
##########################################


### 	Function: ConsolidateList
# 	Purpose: Search for students with exactly identical grades and combine
# 		their list entries into a single list item. 
#	Strategy: Consolidated list expects to receive a list sorted by 
#		test scores in descending order. Potential duplicate scores 
#		will be adjacent to each other. 
###
def consolidateList(nestedList):
	i = 0
	# Debug Statement: Shows the total items in list & their values
	# print (len(nestedList), " : ", nestedList);	
	for x in nestedList:
		#print (nestedList[i], nestedList[i+1])
		#prevent an index out of range error by checking for end of list
		if i < (len(nestedList)-1):
			#if current student has same grade as adjacent student
			#then combine student records
			if nestedList[i][1] == nestedList[i+1][1]:
				nestedList[i+1][0].append(nestedList[i][0][0]) 
				nestedList[i][0].sort()
				
				# Delete the duplicate value, which was copied
				nestedList.pop(i)
				
				# Debug Statement
				# print (len(nestedList), " : ", nestedList);
				
				consolidateList(nestedList)
				return	
		i = i+ 1 

### Main ###
# Input Format
# The first line contains an integer representing the number of students.
# The subsequent lines describe each student over 2 lines
# - The first line contains a student's name. Type = String
# - The second line contains their grade. Type = Float
#
# Constraints
#    There will always be one or more students having the second lowest grade.
#
# Output Format
# Print the name(s) of any student(s) having the second lowest grade. If 
# there are multiple students, order their names alphabetically and print 
# each one on a new line.
###

studentCount = int(input())
studentList = []

# Collect input from STDIN about students & grades
for i in range(0,studentCount):
	name = str(input())
	grade = float(input())
	
	# insert student into list (here would be a great to insertion sort..)
	studentList.insert(i, [[name],grade])

# Sort the list by the grade, which is the 2nd element in each entry...
studentList.sort(key=lambda x:x[1], reverse=True)

# Call the function to remove duplicates & tidy the list
consolidateList(studentList)

#sort the names in each nested list alphabetically
for name in studentList:
	name[0].sort()

# Debug Statement
# print (studentList)

# print the solution - this example prints the second-worst grade in the list. 
# Students tied for second worst share the same list entry, so we iterate
# through all stored in this list. 
#studentList[-2][0].sort()

for students in studentList[-2][0]:
	print (students)


	
