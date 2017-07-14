"""
WeIrD StRiNg CaSe
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

for example:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
"""

# coding:utf-8
# 解题思路
# 字符串分拆为单个字符串 s.plit()-->字符串转换为 list-->判断list 字符大小写情况 if i%2==0 and L[i].islower() : L[i].upper()-->list合成string

# s.islower() 所有字符都是小写
# s.isupper() 所有字符都是大写
# s.upper()  把所有字符大写
# s.lower()  把所有字符小写

def to_weird_case(string):
	# your code
#	st=string.split()
#	for x in  st:
		Li=list(string)
		i=0
		for y in Li:
			if i%2==0:
				Li[i]=y.upper()
			else:
				Li[i]=y.lower()
			i+=1
			
		Li=str(Li)
		
		x=Li

		
	return st

# test
print(to_weird_case("This"))