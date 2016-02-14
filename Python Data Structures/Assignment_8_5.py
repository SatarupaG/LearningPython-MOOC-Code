fname = raw_input("Enter file name: ")
# Code for variable initialization   
count = 0
# Code for exception handling in case of file open error
try:
    if len(fname) < 1 : fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print "Cannot open file with filename: ", fname
    exit()
# Code to parse the From line using split() and print out the second word in the line
for l in fhandle:
    if not l.startswith("From") or l.startswith("From:") : continue
    # Code to count number of occurences
    count = count + 1
    # Code to split and print out the email 
    lst = l.split()
    email = lst[1]
    print email
# Code to print out the count
print "There were", count, "lines in the file with From as the first word"