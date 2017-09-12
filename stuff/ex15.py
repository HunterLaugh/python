# coding: utf-8
# open file      read  file 

from sys import argv

# filename 作为参数传递    可以打开任意文件  复用
script,filename=argv

# 打开文件
txt=open(filename)

print("Here's your file %r: " % filename)
# 读取文件
print(txt.read())

print("I'll also ask you to type it again: ")
# 提示符   接受输入文件名
file_again=input("> ")

# 读取文件
txt_again=open(file_again)

# 打印文件
print(txt_again.read())

# 关闭文件
txt.close()
txt_again.close()