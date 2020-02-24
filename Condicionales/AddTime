aux = 0
l = None 
ll = None
seconds = 0

while aux == 0:
	t =  input("Enter time in format (hours / minutes / seconds) : ")
	t = t.strip()
	print(t)
	
	seconds = float(input("Enter the amount of time to add in seconds : "))
	
	
	if t[0] != '(' :
		print ("This is not the right format .")
		aux == 1
		
	elif t[len(t)-1] != ')':
		print ("This is not the right format .")
		aux == 2
	else:
	
		
		if ("/" in t) :
			l = t.find("/")
		if ("/" in t[l+1:]) :
			ll = t[l+1:].find("/") + l + 1
		if ("/" in t[ll+1:]) :
			aux == 3
			print ("This is not the right format .")
			
		
		
		
		if aux == 0:
			hour = float(int(t[1:l]))
			min = float(int(t[l+1:ll]))
			sec = float(int(t[ll+1:len(t)-1]))
			
			if hour >=24 or min >= 60 or min >= 60:
				print ("This is not the right format .")
				break
			
			seconds = seconds + (hour*3600) + (min*60) + sec
			
			hour = float (int (seconds/3600))
			min = float (int ((seconds-(hour*3600))/60))
			sec = seconds - (hour*3600) - (min*60)
			
			if hour >= 24 :
				hour = hour - 24 
			
			print("(" + str(int(hour)) + "/" + str(int(min)) + "/" + str(int(sec)) + ")")
			
			aux = 4
			
