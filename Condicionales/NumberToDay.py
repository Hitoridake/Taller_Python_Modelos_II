d =  input("Enter number between 1 and 7: ")
d = int(d)

if d == 2:
	d = "Monday"
elif d == 3:
	d = "Tuesday"
elif d == 4:
	d = "Wednesday"
elif d == 5:
	d = "Thursday"
elif d == 6:
	d = "Friday"
elif d == 7:
	d = "Saturday"
elif d == 1:
	d = "Sunday"
else: 
	d = 0
	print ("That number is not between 1 and 7")

if d == 0:
	exit()
else:
	print ("Your day is: " + d)
