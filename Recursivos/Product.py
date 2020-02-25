def prod(x,y):
	if x == 0 or y == 0:
		return 0
	else:
		return (x + prod(x,y-1))
		
x = int(input("Enter a factor : "))
y = int(input("Enter the other factor : "))

print("The product is " + str(prod(x,y)))
