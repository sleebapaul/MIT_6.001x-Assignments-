WORDLIST_FILENAME = "C:\Users\sleeba\Canopy\scripts\Codes\pset4\ProblemSet4\words.txt"
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
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
def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line
def getWordScore(word, n):
    count=0
    for i in word:
        for k in SCRABBLE_LETTER_VALUES:
            if k==i:
                count+=SCRABBLE_LETTER_VALUES[k]
    if len(word)==n:
        score=count*len(word)+50
    else: 
        score=count*len(word)
    return score
def compChooseWord(hand, wordList, n):
    answer=''
    for i in wordList:
        count=0
        handcopy=hand.copy()
        if len(i)<=n:
            for j in i:
                if j in handcopy:
                    handcopy[j]-=1
                    if handcopy[j]<0:
                        break
                    else:
                            count=count+1
                            continue 
                else: 
                    break                       
        if len(answer)<=len(i) and count==len(i):
           answer=i
    if len(answer)==0:
        return 
    else:
        return answer 
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
wordList=loadWords()
n=12
hand=dealHand(n)            
def compPlayHand(hand,wordList,n):
    print 'Current Hand: ',
    displayHand(hand)
    z=compChooseWord(hand, wordList,n)
    score = getWordScore(z,n)
    print '"'+str(z)+'"'+' earned '+str(score)+' points.',
    print 'Total: '+str(score)+' points'
compPlayHand(hand,wordList,n)
    
    