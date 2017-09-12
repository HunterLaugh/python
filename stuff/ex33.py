#  use  loop   function  and  range  for  0-->n

i=0
numbers=[]

while i<6:
	print("At the top i is %d" % i)
	numbers.append(i)
	
	i=i+1
	print("Numbers now: ", numbers)
	print("At the bottom i is %d" % i)
	
print("The numbers: ")

for num in numbers:
	print(num)
	

# test more
def  func(n):
	li=[]
	i=0
	while i<n:
		li.append(i)
		i=i+1
	
	return li
	
print("func(10)",func(10))

# test more
f_r=[]
for x in range(10):
	f_r.append(x)
	
print("f_r ",f_r)