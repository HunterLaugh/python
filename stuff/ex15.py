# coding: utf-8
# open file      read  file 

from sys import argv

# filename ��Ϊ��������    ���Դ������ļ�  ����
script,filename=argv

# ���ļ�
txt=open(filename)

print("Here's your file %r: " % filename)
# ��ȡ�ļ�
print(txt.read())

print("I'll also ask you to type it again: ")
# ��ʾ��   ���������ļ���
file_again=input("> ")

# ��ȡ�ļ�
txt_again=open(file_again)

# ��ӡ�ļ�
print(txt_again.read())

# �ر��ļ�
txt.close()
txt_again.close()