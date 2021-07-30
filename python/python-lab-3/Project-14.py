file1=open("file1.txt",'r')
file1_content=file1.readlines()
file1.close()

file2=open('file2.txt','r')
file2_content=file2.readlines()
file2.close()

result_file=open('file3.txt','w')

class Fileloop :
    def __init__(self,file1,file2):
        self.file1=file1
        self.file2=file2

    def __iter__(self):
        self.i=0
        self.a=""
        self.b=""
        self.res=""
        return self
    
    def __next__(self):
        if len(self.file1)>self.i or len(self.file2)>self.i:
            self.a=str(self.file1[self.i])
            self.b=str(self.file2[self.i])
            self.res=self.a+self.b
            self.i=self.i+1
            return self.res
        else:
            raise StopIteration

myfile=Fileloop(list(file1_content),list(file2_content))
file_iter=iter(myfile)

while True:
    try:
        print(next(file_iter))
    except:
        break
    