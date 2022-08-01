income = int(input("Your income: $"))
remainder = income - 20000
renance = income - 10000
tax = 0
if income > 20000:
    tax += ((10000*0) + (10000*0.1)+(remainder*0.2))
    print("your tax payable is " + "$" + str(tax))
elif income > 10000:
    tax += ((10000*0)+(renance * 0.1))
    print("your tax payable is " + "$" + str(tax))
else:
    print("Since you earn less than $10000 you are Exempted from paying taxes.")
