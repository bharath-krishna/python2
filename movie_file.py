'''
Created on Jul 17, 2014

@author: bharath
'''
import os


mvfl = "/media/bharath/NEW/VIDEO_TS/VTS_01_1.VOB"

mv = open(mvfl, "rb")

fl = open("/home/bharath/Desktop/ans/preone.VOB", "w")


mv.seek(973700000)
fl.write(mv.read(100000000))

print os.path.getsize(mvfl)



