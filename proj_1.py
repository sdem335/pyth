print (333);

a=0;b=7;
C=(a,b,15)
print (isinstance(C,object))

class AttDict(object):
  def __init__(self, dict=None):
    object.__setattr__(self, '_selfdict', dict or {})


  def __setattr__(self, name, value):
    if name[0] != '_':
      self._selfdict[name] = value
    else: raise AttributeError

def __getattr__(self, name):
    if self._selfdict.has_key(name):
      return self._selfdict[name]
    else:    raise AttributeError

def __delattr__(self, name):
    if name[0] != '_' and self._selfdict.has_key(name):
      del self._selfdict[name]

ferd1=AttDict();
print(ferd1);
ad = AttDict({'a': 1, 'b': 10, 'c': '123'})
#print (ad.a, ad.b, ad.c)
print(ad[0]);
print(ad);
ad.d = 512;
#print (ad.__getattribute__(ad.d))
print(ad.d)