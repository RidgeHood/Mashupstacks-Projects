a=['cat','dog','goat']

file=open('test.txt','a')

file.write(str(a))
file.close()

rfile=open('test.txt','r')
print(rfile.read())