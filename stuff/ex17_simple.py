# coding:utf-8

from sys import argv
from os.path import exists

script,from_file,to_file=argv

# open from_file->read from_file-->open to_file->write to_file
(open(to_file,'w')).write((open(from_file)).read())
