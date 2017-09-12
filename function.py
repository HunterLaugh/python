#coding:utf-8

# 绝对值
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

# x的n次方，
# 默认参数
def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s

# 默认参数
def enroll(name,gender,age=6,city='Shenzheng'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

# 可变参数
# sum=参数的平方和
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

# 关键字参数，它可以扩展函数的功能。包含必选项与可选项
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
