def f(x):
	import math
	return 200*math.e**(math.log(0.5)/14.1 * x)
def radiationExposure(start, stop, step):
    y=0
    while start<=stop:
        y=y+f(start)
        start=start+step  
    return y
z=radiationExposure(14, 20, 0.1)
print z      
        