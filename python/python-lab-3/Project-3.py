text=input('Enter the text: ')
file=open('test.txt','a')

file.write(text)
file.close()

rfile=open("test.txt",'r')

print(rfile.read())
