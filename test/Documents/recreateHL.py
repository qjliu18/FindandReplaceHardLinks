import sys

in_file = open(sys.argv[1], 'r')

# Keep track of which line we are on, use this to store first line. 
lineCount = 0

currFile = in_file.readline()
currINode = currFile.split('/')[0]
pathToLink = currFile.split(' ')[1]
currName = currFile.split('/')[-1]

print('split with "/": ' + currINode)
print('split with " ": ' + pathToLink, end="")
print(currName)

while True:
	currFile = in_file.readline()
	if currFile == "":
		break

	currFile = currFile.split('/')
	
	if lineCount == 0:
		# need to take path and create a hardlink in this directory

		prevINode = currINode[0]
		lineCount += 1
	
	#currName = currFile[-1]
	#print('current iNode num: ' + currINode)
	#print('current hard link name: ' + currName)

