import os

# Set up find command
print('Hard links found in this directory:')
os.system("find /c/Users/jqLiu/Dropbox/Projects/Work/FindandReplaceHardLinks/test/Documents -type f -links +1 -exec ls -i {} \';'")

print('Storing found hard links in results.txt')
os.system("find /c/Users/jqLiu/Dropbox/Projects/Work/FindandReplaceHardLinks/test/Documents -type f -links +1 -exec ls -i {} \';' > results.txt")

print('Sorting results.txt and storing in sortedResults.txt')
os.system('sort results.txt > sortedResults.txt')

print('Output of sortedResults:')
os.system('cat sortedResults.txt')