largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    #Code to stop the user input
    if num == "done" : break
    #Code to catch the invalid input
    try:
        input_num = float(num)
    except:
        print "Invalid input"
        continue
    #Code to find the minimum and maximum from user input
    if (smallest is None):
        smallest = input_num
    if (input_num > largest):
        largest = input_num
    if (input_num < smallest):
        smallest = input_num
#Code to print the largest and smallest numbers
print "Maximum is", int(largest)
print "Minimum is", int(smallest)