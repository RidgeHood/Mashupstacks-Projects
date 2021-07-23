
class MyNumbers:
  def __init__(self,b):
    self.b=b
  #def fun(self):
   # self.a = 0
   # return self

  def __next__(self):
    if self.a==self.b:
      raise StopIteration

    x = self.a
    self.a += 1
    return x

myclass = MyNumbers(20)
j=myclass.fun()
print(next(j))
print(next(j))
print(next(j))
print(next(j))





