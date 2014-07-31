'''
Created on Jul 18, 2014

@author: bharath
'''
from copy import copy
import os
import sys


class a () :
    def aa (self) :
        print "inside aaa"


class b () :
    def aa (self) :
        print "inside baa "
    
class c (a, b) :
    def pri (self) :
        print "inside pri"


cob = c()

cob.aa()
cob.pri()

print issubclass(c, b)

print isinstance(cob, a)
for i in range(21) :
    print "Leftshift %d times : %d "%(i, 1 << i)

# print 1048576 >> 19


print callable (c)
co = copy(cob)
co.pri()

print cmp(co, cob)



print os.path.basename(sys.argv[0])







