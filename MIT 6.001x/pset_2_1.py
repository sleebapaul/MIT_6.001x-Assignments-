balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
count=0
for month in range(12):
    print 'Month : '+str(month+1)
    minpay=balance*monthlyPaymentRate
    minpay=round(minpay,2)
    count=count+minpay
    print 'Minimum monthly payment: '+str(minpay)
    rem_bal=balance-minpay
    balance=rem_bal+rem_bal*(annualInterestRate/12)
    balance=round(balance,2)
    print 'Remaining balance: '+str(balance)
print 'Total Paid: '+str(count)
print 'Remaining balance: '+str(balance)