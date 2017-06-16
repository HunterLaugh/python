# coding:utf-8

from sys import argv

script,filename=argv

print("Open  " ,filename)
target=open(filename)

print("Read and Print",filename)
print(target.read())

print("Close file",filename)
target.close()