print (333);

a=0;b=7;
C=(a,b,15)
print (isinstance(C,object))

 
class Special():
    def __init__(self,a,b,d):
            self.field1 = a
    def __getAttribute__(self):
         return self.field1+3
    def __getAttribute__(self):
         return self.field1+3
    def __setAttr__(self,a,b,d):
        self.field1=a;
        self.field2=b;
        self.field3=d;
        return self.field1+self.field2+self.field3;

Ob1 = Special(2,2,{})
print(Ob1.field1)
print(Ob1.__getAttribute__())

print(Ob1.__setAttr__(1,2,3))       

print(Ob1.field2)