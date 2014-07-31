
class newclass () :
    
    def set (self, va, ba) :
        self.va = input("please enter value for 'va' = ")
        self.ba = input("please enter value for 'ba' = ")
    
    def add (self) :
        print self.va
        print self.ba
        self.res = self.va+self.ba
    
    def disp (self) :
        print self.res
    


# list handling    

lis = [3,46,7,3]


li = range(1,21)

# print [x for x in li if x%2==1]


import copy
x = [1,2,3,4]

y = copy.copy(x)

y.append("5")

# print x is y
# print y is y


# exit()






# print lis.pop()
# print lis.append("dfd")
# print lis.index("dfd")
# print lis.insert(1,"asdfasf")
# print lis.sort()
# # print lis.extend(lis)
# print lis.reverse()
# print lis[0:4]
# lis[0:2] = lis
# 
# print
# print lis









# string handling

# strr = "    bharath krishna    "
# 
# print strr.title()
# print "a comes", strr.count('a')," times"
# print strr.strip()
# print strr.strip().partition(" ")
# print strr.strip().rpartition(" ")
# print strr.strip().split("h", 2)


# print strr

def args (ga,*tup, **dics) :
    print ga," is a str"
    print tup
    print dics

def unpack (l1,l2,l3,ga,ha,ja) :
    print ga,ha,ja
    pass


dic = {'ga' : 3, 'ha' : 4, 'ja' : 5}
args(12233, 43,545,5,4,fdf = 343, fdfs=322 )
li = ()
# unpack(**dic)
# obj = newclass()
# obj.set(5,5)
# obj.add()
# obj.disp()


exit(0)


# list comprehension

print [x for x in range(2) if(x > 0) for x in range(3) if x > 1]

list = []
for x in range(2) :
    if(x > 0) :
        for x in range(3):
            if x > 1 :
                list.append(x)
        


# print list
# 
# num = 512
# print num << 1
# 
# 
# print 
# s = 'asdf'
# it = iter(s)
# 
# print it.next()
# print it.next()
# print it.next()
# print it.next()


exit()


class reverse () :
    def __init__ (self, data) :
        self.data = data
        self.index = len(data)
    def __iter__ (self) :
        return self
    def next (self) :
        if self.index == 0 :
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]




obj = reverse("bharath")
# print obj
        
iter(obj)

for ch in obj :
    print ch









