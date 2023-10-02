#import Special from p2 
from p3_test2 import Special
import sys
def func1():
    a= Special(1,1,1)
    #print(a)
    return(a.__getAttribute__())
#print(sys.path)
print(func1())
print(dir(str))


help(int)