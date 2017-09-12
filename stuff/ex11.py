# coding:utf-8
# stand input()  return string
# stand output print()
# int() float()

print("How old are you?",end=' ')
age=int(input())
print("How tall are you?",end=' '),
height=int(input())
print("Howe much do you weight?",end=' '),
weight=float(input())

print("So you're %r old, %r tall and %r heavy." %(age,height,weight))