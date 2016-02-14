fname = raw_input("Enter file name: ")
# Code for exception handling in case of file open error
try:
    fhandle = open(fname)
except:
    print "Cannot open file with filename: ", fname
    exit()
    
lst = list()
# Code to split the line into a list of words 
for line in fhandle:
	split_line = line.rstrip().split()
    # Code to check each line to see if the word is already in the list and if not append it to the list
	for word in split_line:
		if word not in lst:
            # Code to add word to the list
			lst.append(word)
    # Code to sort the list
	lst.sort()
# Code to print out the list of words in alphabetical order
print lst