fname = raw_input("Enter file name: ")
# Code for variable initialization
bigCount = None
bigWord = None
# Code for exception handling in case of file open error
try:
    if len(fname) < 1 : fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print "Cannot open file with filename: ", fname
    exit()
    
email_dic = dict()
# Code to create dictionary that maps the sender's mail address to a count of the number of times they appear in the file
for line in fhandle:
    if not line.startswith("From") or line.startswith("From:") : continue
    lst = line.split()
    mail = lst[1]
    email_dic[mail] = email_dic.get(mail,0) + 1
# Code to parse through the dictionary using a maximum loop to find the most prolific committer
for word,count in email_dic.items():
	if bigCount is None or count > bigCount:
		bigWord = word
		bigCount = count
# Code to print out the most prolific committer with the count
print bigWord,bigCount