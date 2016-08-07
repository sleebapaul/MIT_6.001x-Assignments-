def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    b=string.ascii_lowercase
    for i in lettersGuessed:
        if i in lettersGuessed:
             b= b.replace(i, "")
             print b
    return b
getAvailableLetters()

    
    