fname = raw_input("Enter file name: ")
# Code for exception handling in case of file open error
try:
    if len(fname) < 1 : fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print "Cannot open file with filename: ", fname
    exit()
dic = dict()
# Code to pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon
for line in fhandle:
    if not line.startswith("From") or line.startswith("From:") : continue
    time = line.split()[5]
    hour = time.split(":")[0]
    dic[hour] = dic.get(hour,0) + 1
lst = list()
# Code to use the bulit-in function sorted() in tuple
for key, val in sorted(dic.items()):
    # Code to print out the hour and its count
	print key,val