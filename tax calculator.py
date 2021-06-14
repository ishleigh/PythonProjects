income = float(input("Enter the annual income: "))

#tax calculator
if income< 85528 :
    tax= ((income*0.18)-556.02)

elif income>85528:
    tax=(((income-85528)*0.32)+14839)
    
if tax>0:
    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")
else:
    tax=0.0
    print("The tax is: ", tax, "thalers")
