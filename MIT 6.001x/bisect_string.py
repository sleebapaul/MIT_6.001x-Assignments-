def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    low = 0
    high = len(aStr)
    ans=(low +high)/2
    if char == aStr(ans-1):
        return True 
    elif char > aStr(ans-1):
        low=ans
        return isIn(aStr[low:high])
     else:
         high=ans
         return isIn(aStr[low:high])
        
