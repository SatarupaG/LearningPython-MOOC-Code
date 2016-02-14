#Function computepay to compute the total pay
def computepay(h,r):
    #Code for variable initialization
    normal_pay = 0
    enhanced_pay = 0
    total_pay = 0
    #Code for condition checking
    if (h > 40):
        normal_pay = 40 * r
        enhanced_pay = (h-40) * (r*1.5)
        total_pay = normal_pay + enhanced_pay
    else:
        normal_pay = h * r
        total_pay = normal_pay
	#Code to return the total pay    
    return total_pay 
#Main program
hrs = raw_input("Enter Hours:")
h = float(hrs)
rate_pr_hrs = raw_input("Enter Rate Per Hour:")
r = float(rate_pr_hrs)
p = computepay(h,r)
#Code to print the total pay  
print p