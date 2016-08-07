balance = 4773
annualInterestRate = 0.2
minpay=10
bal_old=balance
while balance>0:
    for month in range(12):
            rem_bal=balance-minpay
            rem_bal=rem_bal+(rem_bal*annualInterestRate/12)
            balance=rem_bal
    if balance>0:
            balance=bal_old
            minpay+=10
    else :
            break
print 'Lowest Payment: '+str(minpay)

