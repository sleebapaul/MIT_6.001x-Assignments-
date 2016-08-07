def getGuessedWord(secretWord, lettersGuessed):
    strng=''
    for i in secretWord:
        if i not in lettersGuessed:
            strng+=' _ '
        else: 
            strng+=i      
    return strng
def getAvailableLetters(lettersGuessed):
    import string
    b=string.ascii_lowercase
    for i in lettersGuessed:
        if i in lettersGuessed:
             b= b.replace(i, "")
    return b
def isWordinside(secretWord, lettersGuessed):
 
    if lettersGuessed[-1] not in secretWord:
            return False
    else: 
            return True  
def hangman(secretWord):
    print 'Welcome to the game, Hangman!'
    secretWord=secretWord.lower()
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '------------'
    print 'You have 8 guesses left.'
    print 'Available letters: abcdefghijklmnopqrstuvwxyz'
    lettersGuessed=[]
    n=8
    lettersGuessed.append(raw_input('Please guess a letter: '),)
    lettersGuessed=[x.lower() for x in lettersGuessed]
    z=isWordinside(secretWord, lettersGuessed)
    if z==True:
        strng=getGuessedWord(secretWord, lettersGuessed)
        print 'Good guess: ' + str(strng)
    elif z==False:
        strng=getGuessedWord(secretWord, lettersGuessed)
        print 'Oops! That letter is not in my word: '+str(strng)
        n=n-1
    print '------------'
    if secretWord==strng:
            print 'Congratulations, you won!'
    while n>0:
        print 'You have '+str(n)+' guesses left.'
        b=getAvailableLetters(lettersGuessed)
        print 'Available letters: '+str(b)
        lettersGuessed.append(raw_input('Please guess a letter: '),)
        lettersGuessed=[x.lower() for x in lettersGuessed]
        g=lettersGuessed[-1]
        z=isWordinside(secretWord, lettersGuessed)
        if lettersGuessed.count(g)>1:
                strng=getGuessedWord(secretWord, lettersGuessed)
                print 'Oops! You\'ve already guessed that letter: '+ str(strng)
        elif z==True:
                strng=getGuessedWord(secretWord, lettersGuessed)
                print 'Good guess: ' + str(strng)
        elif z==False:
                strng=getGuessedWord(secretWord, lettersGuessed)
                print 'Oops! That letter is not in my word: '+str(strng)
                n=n-1
        print '------------'
        if secretWord==strng:
            print 'Congratulations, you won!'
            break 
    if secretWord!=strng:
        print 'Sorry, you ran out of guesses. The word was '+str(secretWord)+'.'        
hangman('family')      