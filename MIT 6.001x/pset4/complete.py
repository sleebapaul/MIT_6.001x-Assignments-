import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
WORDLIST_FILENAME = "C:\Users\sleeba\Canopy\scripts\Codes\pset4\ProblemSet4\words.txt"
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq	
def isValidWord(word, hand, wordList):
    handcopy=hand.copy()
    if word in wordList:
        for i in word:
            if handcopy.has_key(i):
                handcopy[i]-=1
                if handcopy[i]<0:
                    return False
                else: continue
            else:
                return False
        return True
    else:
        return False
def isValidWord2(word, hand, wordList):
    handcopy=hand.copy()
    for i in word:
        if handcopy.has_key(i):
            handcopy[i]-=1
            if handcopy[i]<0:
                    return False
            else: continue
        else:
                return False
    return True
def dealHand(n):
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1   
    return hand
def getWordScore(word, n):
    count=0
    for i in word:
        for k in SCRABBLE_LETTER_VALUES:
            if k==i:
                count+=SCRABBLE_LETTER_VALUES[k]
    if len(word)==n:
        return count*len(word)+50
    else: 
        return count*len(word)
def updateHand(hand, word):
    handcopy=hand.copy()
    for i in word:
        for k in handcopy:
            if k==i:
                handcopy[k]-=1
    return handcopy
def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter, 
    print
def calculateHandlen(hand):
    count=0  
    for i in hand.keys():
        count=count+hand[i]
    return count

def compChooseWord(hand, wordList, n):
    score=0
    answer=''
    for i in wordList:
        if len(i)<=n:
            z=isValidWord2(i, hand, wordList)
            if z==True:
                newscore=getWordScore(i, n)
                if score<newscore:
                    answer=i
                    score=newscore
                    continue
                else: continue
            else:continue
    if answer!='':
        return answer
    else:
        return                               
def playHand(hand, wordList, n):
    score=0
    print 'Current Hand: ',
    displayHand(hand)
    count=calculateHandlen(hand)
    word=raw_input('Enter word, or a "." to indicate that you are finished: ',)
    while word!='.' and count!=0:
        z=isValidWord(word, hand, wordList)
        if z==False:
            print 'Invalid word, please try again.'
            print 'Current Hand: ',
            displayHand(hand)
            word=raw_input('Enter word, or a "." to indicate that you are finished: ',)
            continue
        else:
            print str(word)+' earned '+str(getWordScore(word, n))+' points. ',
            score=score+getWordScore(word,n)
            print 'Total: '+str(score)+' points'
            hand=updateHand(hand, word)
            count=calculateHandlen(hand)
            if count==0:
                break
            print 'Current Hand: ',
            displayHand(hand)
            word=raw_input('Enter word, or a "." to indicate that you are finished: ',)
    if word=='.':
        print 'Goodbye! Total score: '+str(score)+' points.'
    elif count==0:
        print 'Run out of letters. Total score: '+str(score)+' points.'
wordList=loadWords()

def compPlayHand(hand, wordList, n):
    print 'Current Hand: ',
    displayHand(hand)
    score=0
    count=0
    z=compChooseWord(hand, wordList,n)
    if z!=None:    
        score=getWordScore(z,n)
        print '"'+str(z)+'"'+' earned '+str(score)+' points.',
        print 'Total: '+str(score)+' points'
        hand=updateHand(hand, z)
        count=calculateHandlen(hand)  
    while count!=0:
        print 'Current Hand: ',
        displayHand(hand)
        z=compChooseWord(hand, wordList,n)
        if z==None:
            break
        print '"'+str(z)+'"'+' earned '+str(getWordScore(z,n))+' points.',
        print 'Total: '+str(score+getWordScore(z,n))+' points'
        score = score+getWordScore(z,n)
        hand=updateHand(hand, z)
        count=calculateHandlen(hand)
    print 'Total score: '+str(score)+' points.'
def playGame(wordList):
    k=str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '),)
    while k!='n':
        if k=='r':
            print 'You have not played a hand yet. Please play a new hand first!'
            k=str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '),) 
        elif k=='e':
            break
        else:
            print 'Invalid command.'
            k=str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '),) 
    while k!='e':
        if k=='n':
            warn=str(raw_input('Enter u to have yourself play, c to have the computer play: '),)
            while True:
                if warn=='u':
                    hand=dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif warn=='c':
                    hand=dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
                    warn=str(raw_input('Enter u to have yourself play, c to have the computer play: '),)
            k=str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '),)
        elif k=='r':
            warn=str(raw_input('Enter u to have yourself play, c to have the computer play: '),)
            while True:
                if warn=='u':
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif warn=='c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
                    warn=str(raw_input('Enter u to have yourself play, c to have the computer play: '),)
            k=str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '),)
        else:
            print 'Invalid command.'
            k=str(raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '),)
wordList=loadWords()
playGame(wordList)

