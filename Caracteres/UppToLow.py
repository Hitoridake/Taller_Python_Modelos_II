t = input("Enter a string : ")
s = t
for i in t:
	if i.islower():
		s = s[0:s.find(i)] + s[s.find(i)].upper() + s[s.find(i) + 1:]

print (s)

for i in t:
	if i.isupper():
		t = t[0:t.find(i)] + t[t.find(i)].lower() + t[t.find(i) + 1:]
		
print(t)
