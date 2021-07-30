myfile=open('test.txt','r')
content=myfile.read()
myfile.close()

newfile=open('test2.txt','w')
newfile.write(content)
newfile.close()

read_newfile=open('test2.txt','r')

print(read_newfile.read())