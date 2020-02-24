import math
number = float(input ("Enter a number : "))

aux = 0
i = 2

if (number - int(number)) != 0 or number <= 1:
	print("The number must be natural greater than 1")

else:
	
	while aux == 0 and i < number:
		if (((number/i) - int(number/i)) == 0) :
			aux = aux + 1
		i = i + 1
		
	if aux == 0:
		print("Your number is prime")
	else:
		print("Your number is compose")
