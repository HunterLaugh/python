# coding:utf-8
# 复制文件

from sys import argv
from os.path import exists

script,from_file,to_file=argv

print("Copying from %s to %s" %(from_file,to_file))

# we could do these two on one line too, how ?

inputFile=open(from_file)
indata=inputFile.read()

print("The input file is %d bytes long" % len(indata))

# exists(filename)  file 存在返回True   不存在返回False
print("Does the output file exists? %r " % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

output=open(to_file,'w')
output.write(indata)

print("Alright, all done.")

# close file
output.close()
inputFile.close()