def fibo(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return (fibo(x-1)+fibo(x-2))

x = int(input("Enter the position of the Fibonacci number : "))

print ("The Fibonacci number is " + str(fibo(x)))
