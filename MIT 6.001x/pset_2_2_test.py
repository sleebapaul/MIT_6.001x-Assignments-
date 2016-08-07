balance = 999999
annualInterestRate = 0.18
import timeit
start = timeit.default_timer()
bal_old=balance
mon_interest_rate=annualInterestRate/12
low=balance/12
high=(balance* (1 + mon_interest_rate)**12) / 12.0 
while balance>0:
    ans=(low+high)/2
    for month in range(12):
            rem_bal=balance-ans
            rem_bal=rem_bal+(rem_bal*annualInterestRate/12)
            balance=rem_bal
    balance=round(balance,2)
    if balance>0:
            balance=bal_old
            low=ans
    elif balance<0:
        balance = bal_old
        high=ans
    else:
        break
ans=round(ans,2)       
print 'Lowest Payment: '+str(ans)
stop = timeit.default_timer()
print stop - start 