import math

def dist(x1,y1,x2,y2) :
	print (math.sqrt(pow(x2-x1,2)+pow(y2-y1,2)))
	
x1 = float(input ("Enter x1 : "))
y1 = float(input ("Enter y1 : "))
x2 = float(input ("Enter x2 : "))
y2 = float(input ("Enter y2 : "))

dist(x1,y1,x2,y2)
