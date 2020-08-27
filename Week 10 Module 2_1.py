employees=[]

for num in range(6):
    print("Enter the hours worked by employee", num+1, end='')
    hours = float(input(": "))
    employees.append(hours)

print()
payRate = float(input("Enter the hourly pay rate: "))
print()

for num in range(6):
    grossPay = employees[num] * payRate
    print("Gross pay for employee ", num+1 ,": $", grossPay)
