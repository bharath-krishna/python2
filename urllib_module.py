'''
Created on Jul 15, 2014

@author: bharath
'''

import os
import socket
import urllib as url


res = url.urlopen("http://www.gmail.com") # open the url
x = res.read() #read the url (HTML content) and write into a file.html
if os.path.exists(os.getcwd()+"/gmail.html") : # check for file existance
    pass
else :
    # create output file by system's touch command
    os.system("touch "+os.getcwd()+"/gmail.html")


# open the gmail.html file in read and write mode
fh = open(os.getcwd()+"/gmail.html", "w")

fh.write(x)

os.system("firefox gmail.html")



# print url.localhost() # print IP address of localhost as below

# print socket.gethostbyname('localhost')










