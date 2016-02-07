#Code for variable initialization
hrs = raw_input("Enter Hours:")
h = float(hrs)
rate_pr_hrs = raw_input("Enter Rate Per Hour:")
rph = float(rate_pr_hrs)
normal_pay = 0
enhanced_pay = 0
total_pay = 0
#Code for condition checking
if (h > 40):
    normal_pay = 40 * rph
    enhanced_pay = (h-40) * (rph*1.5)
    total_pay = normal_pay + enhanced_pay
else:
    normal_pay = h * rph
    total_pay = normal_pay
#Code to print out the total pay    
print total_pay 