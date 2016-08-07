from ps4a import *
import time

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
wordList=loadWords()
def compPlayHand(hand, wordList, n):
    score=0
    print 'Current Hand: ',
    displayHand(hand)
    z=compChooseWord(hand, wordList,n)
    print '"'+str(z)+'"'+' earned '+str(getWordScore(z,n))+' points.',
    print 'Total: '+str(getWordScore(z,n))+' points'
    hand=updateHand(hand, z)
    print hand 
    count=calculateHandlen(hand) 
    print count  
    while count!=0 and hand:
        print 'Current Hand: ',
        displayHand(hand)
        z=compChooseWord(hand, wordList,n)
        if z==None:
            break
        score = getWordScore(z,n)
        print '"'+str(z)+'"'+' earned '+str(getWordScore(z,n))+' points.',
        print 'Total: '+str(score+getWordScore(z,n))+' points'
        hand=updateHand(hand, z)
        count=calculateHandlen(hand)
    print 'Total score: '+str(score+getWordScore(z,n))+' points.'
hand={'a': 2, 'c': 1, 'b': 1, 't': 1}
n=5
compPlayHand(hand, wordList, n)
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function

        
#
# Build data structures used for entire session and play game
#
#if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


