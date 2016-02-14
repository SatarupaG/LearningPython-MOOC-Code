# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
# Code for variable initialization    
total = 0
count = 0
# Code for exception handling in case of file open error
try:
    fhandle = open(fname)
except:
    print "Cannot open file with filename: ", fname
    exit()
# Code to search for specific portion in the file
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # Code to extract out the portion of the text required
    pos = line.find(":")
    number = line[pos+1:]   
    number = float(number)
    # Code to compute the average
    count = count + 1
    total = total + number
    average = total / count
# Code to print out the average spam confidence      
print "Average spam confidence:" , average