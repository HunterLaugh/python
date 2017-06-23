def persistence(n):
	count=0
	while len(str(n))>1:
		New=1
		L=str(n)
		for x in L:
			n=int(x)*New
		count+=1
	
	return count
	
print("persistence(2)",persistence(2))
print("persistence(29)",persistence(29))		
print("persistence(398)",persistence(398))
print("persistence(7892)",persistence(7892))
print("persistence(98772)",persistence(98772))