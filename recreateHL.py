import sys
import os

in_file = open(sys.argv[1], 'r')

# Line Count, checks if on first line
lineCount = 0

# Reads first line and stores information
currFile = in_file.readline()
currINode = currFile.split('/')[0]
pathToLink = currFile.split(' ')[1] + ' '
firstName = currFile.split('/')[-1]

# print(pathToLink)
# print(currFile)
# print('split with "/": ' + currINode)
# print('split with " ": ' + pathToLink, end="")
# print(currName)

while True:
	# Reads subsequent lines in file
	nextFile = in_file.readline()
	# print(nextFile)
	if nextFile == "":
		break

	if lineCount == 0:
		print("Linking " + pathToLink + "as : " + firstName)
		cmd = 'ln ' + pathToLink + firstName
		os.system(cmd)
		lineCount += 1
	
	nextINode = nextFile.split('/')[0]
	nextName = nextFile.split('/')[-1]
	pathToLink = nextFile.split(' ')[1] + ' '
	if currINode == nextINode:
		print('Linking ' + pathToLink + 'as : ' + nextName)
		cmd = 'ln ' + pathToLink + nextName
		os.system(cmd)
		#print('Entered if statement')
	else: 
		print('Linking ' + pathToLink + 'as : ' + nextName)
		cmd = 'ln ' + pathToLink + nextName
		os.system(cmd)
		currINode == nextINode
		#print('Entered else statement')
