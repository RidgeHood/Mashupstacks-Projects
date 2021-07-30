dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}


class a():
    def __init__(self,dic):
        self.dic=dic

    def __add__(self,ob2):
        
        self.dic.update(ob2.dic)

        return a(self.dic)
    
    def __str__(self):
        return str(self.dic)
    
obj1=a(dic1)
obj2=a(dic2)
obj3=a(dic3)

print(obj1+obj2+obj3)
