d = {1:10, 2:20, 3:30,3:40}
def dict_invert(d):
    v = {}
    for key, value in sorted(d.iteritems()):
        v.setdefault(value, [])
    return v
print dict_invert(d)

d= {"George":'G.MacDonald', "Luke":'G.MacDonald', "Larry":'G.MacDonald'} 
#d = {1:100, 2:20, 3:30, 4:30}
d={4:True, 2:True, 0:True,4:False}
v = {}
for key, value in sorted(d.iteritems()):
    print [key,value]
    v.setdefault(value, []).append(key)
print v


new = {}
d={4:True, 2:True, 0:True,5:False}
for (key, value) in d.iteritems():
    if key in new:
        new[value].append(key)
    else:
        new[value] = [key]
print new