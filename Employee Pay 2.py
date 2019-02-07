Hours = input('Hours Worked')
PayRate = input('Pay')
Employee = input('Employee Name')


regular = int(Hours) * int(PayRate)

if int(Hours) <= 40:
    TotalPay = regular
else:
    if int(Hours) > 40:
        overtimeRate = (1.5 * int(PayRate))
        overtime = (int(Hours) - 40) * overtimeRate
        TotalPay = regular + overtime



print(Employee)
print(Hours)
print(TotalPay)
