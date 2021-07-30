import random as r

file=open('file1.txt','r')
content=file.readlines()
file.close()
i=r.randint(0,len(content))

print(content[i])