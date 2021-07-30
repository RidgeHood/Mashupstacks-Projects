file=open('test.txt','r')
content=file.readlines()
i=0
result=[]
for x in range(len(content)):
    result.append(content[x].replace("\n",""))
    
print(result)