#coding: utf-8
sum=0
for x in range(101):
    sum=sum+x
print('sum=',sum)

sum_odd=0
n=99
while n>0:
    sum_odd=sum_odd+n
    n=n-2
print('sum_odd=',sum_odd)