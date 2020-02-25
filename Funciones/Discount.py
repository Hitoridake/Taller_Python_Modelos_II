def perc(number, quant):
	return ((number*quant)/100)
	
def disc(unitys, price):
	if unitys > 6 :
		print (price - perc(price,4))
	elif unitys > 12:
		print (price - perc(price,10))
	else :
		print (price)

disc(float(input("Enter the amount of product to buy :")),float(input("Enter the price of the product ")))
