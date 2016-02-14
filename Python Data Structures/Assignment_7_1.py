# Use words.txt as the file name
# Code to define a file open operation function
def openfile():
    fname = raw_input("Enter file name: ")
    # Code for exception handling in case of file open error
    try:    
        fh = open(fname, 'r')
    except:
        print "Cannot open file with filename: ", fname
        quit() 
    return fh
# Code to define a file content print operation function
def printit(fileName):
    for line in fileName:       
        print line.upper().rstrip() #Trailing comma to avoid adding a newline at the end of print

# Code to call both the file operations
fh = openfile()
printit(fh)