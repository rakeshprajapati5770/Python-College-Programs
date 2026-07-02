customer_id=int(input("Enter the Customer id : "))
name = input("Enter Customer Name: ").title()
bill_month=input("Enter billing month: ").capitalize()
units = int(input("Enter Units Consumed: "))
pending_months = int(input("Enter Pending Months: "))

if units<=50:
    rate=3.50
elif units>50 or units<=100:
    rate=6.00
elif units>100 or units<=200:
    rate=7.50
else:
    rate=9.50    
    
bill=units*rate


print("\n=======================================")
print("    ELECTRICITY BILL SYSTEM")
print("=======================================")
print("Customer ID: ",customer_id)
print("Customer name: ",name)
print("Billing Month: ",bill_month)
print("Units consumed: ",units)
print("Total Bill: ",bill)
if pending_months > 0:
    print("Status          : Previous Bills Pending")
else:
    print("Status          : No Pending Bills")
print("=======================================")

