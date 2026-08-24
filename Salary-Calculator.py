Basic_Salary = float(input("enter the salary:"))
HR = float(input("enter the salary:"))
DA = float(input("enter the salary:"))
Deduction = float(input("enter the deduction:"))
Gross_Salary = Basic_Salary + HR + DA
Net_Salary = Gross_Salary - Deduction
print("Basic_Salary",Basic_Salary)
print("HR Salary",HR)
print("DA Salary",DA,)
print("Deduction",Deduction)
print("Gross_Salary",Gross_Salary)
print("Net_Salary",Net_Salary)
if Net_Salary >= 50000:
    print("more salary")
else:
    print("less salary")
