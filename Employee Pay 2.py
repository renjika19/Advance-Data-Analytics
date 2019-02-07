Hours = input('Hours Worked')
PayRate = input('Pay')
Employee = input('Employee Name')



if int(Hours) > 40:
    overtimeRate = (1.5 * int(PayRate))
    overtime = (int(Hours) - 40) * overtimeRate
    Hours = 40
else:
    overtime = 40

regular = int(int(Hours) * int(PayRate))

TotalPay = regular + overtime

print(Employee)
print(Hours)
print(TotalPay)