print 'Please think of a number between 0 and 100!'
low=0
high=100
x='b'
while (x!='c'):
    ans=(low+high)/2
    print 'Is your secret number ' + str(ans) + '?'
    print 'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.',
    x=raw_input()
    if x=='l':
        low=ans
    elif x=='h':
        high=ans
    elif x=='c':
        break
    else:
        print 'Sorry, I did not understand your input.'
print 'Game over. Your secret number was: '+str(ans)
