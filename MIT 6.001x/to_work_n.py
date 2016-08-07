s='azcbobobegghakl'
def occurrences(string,sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
z=occurrences(s,'bob')
print 'Number of times bob occurs is: '+str(z)
