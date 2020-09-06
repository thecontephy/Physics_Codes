import math
import random 

t= 5000
circle= 0
square= 0
for i in range(t): 

	x= random.uniform(-1, 1) 
	y= random.uniform(-1, 1) 

	distance= x**2 + y**2       #unit circle check

	if distance<= 1: 
		circle+= 1

	square+= 1

	pi = 4* circle/ square 
    


print("Final Value of Pi=", pi)	 
