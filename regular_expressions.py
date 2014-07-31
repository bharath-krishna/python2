


import re


m = re.match("a(sd)f", "AsdF", re.I)
print m.group()
print m.group(1)

strr = 'bharath krishna chakravarthi'
n = re.split("\s", strr);

print n


m = re.subn('h', '#', strr)

print m[1]











