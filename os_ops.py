#!/usr/bin/python

import os
import urllib as u
import sys

print sys.platform
print os.name # prints posix in unix
os.mkdir("./dfd")
print os.path.exists("./dfd") # check for dir existance
os.rmdir("./dfd")
print os.path.split(os.getcwd())
print os.path.exists(os.getcwd()+"/os_ops.py") # True
print os.path.isdir(os.getcwd()) # true
print os.path.isdir(os.getcwd()+"/os_ops.py") # False
print os.path.isfile(os.getcwd()+"/os_ops.py")# True

print os.path.getmtime("./os_ops.py") # GET THE MODIFICATION DATE/TIME


print os.path.basename(os.path.abspath("./")) # gat the base name 'Python_Project'
print os.getcwd() # prints 'Python_Project'
os.mkdir(os.path.abspath("./newdir")) # create 'newdir' in 'Python_Project'
print os.listdir("./") # print the contents of './' i.e. 'Python_Project'
os.rmdir("./newdir") # remove the directory 'newdir
 
print "after removing"
print os.listdir("./") # print contents after removing


# Two ways of printing the output of 'ls -lh' command

ppe = os.popen("ls -lh")
print ppe.read()


import commands as cmd

print cmd.getoutput("ls -lh")




exit()







