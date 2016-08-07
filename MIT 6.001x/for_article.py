student=['A','B','C','D','E']
marks=[21,35,13,26,49]
n=len(marks)
count=0
count1=0
for i in range(n):
    if marks[i]>=25:
        print student[i] +' is passed'
        count=count+1
    else:
        print student[i] +' is failed'
        count1=count1+1
print 'No. of students Passed : '+str(count)
print 'No. of students Failed : '+str(count1)