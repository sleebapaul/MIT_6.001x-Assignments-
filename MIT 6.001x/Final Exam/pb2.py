L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
def getSublists(L,n):
    main_list=[]
    for i in range(len(L)):
        mini_list=[]
        num=0
        if i+n<=len(L):
            while num<n:
                mini_list.append(L[i+num])
                num+=1
        else :
            break
        main_list.append(mini_list)
    return main_list
def longestRun(L):
    count=0
    big=0
    for i in range(len(L)-1):
        if L[i+1]>=L[i]:
            count=count+1
        else:
            if count>big:
                big=count
            count=0
        if count>big:
            big=count
    return big+1 
print longestRun([14, 16, 18, 20, 8, 10, 12, 4, 6, 2])