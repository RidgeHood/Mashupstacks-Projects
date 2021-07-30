inp=input("Enter the number:\n")

rfile=open("test.txt",'r')

content=rfile.readlines()
content.reverse()



for line in range(int(inp)):
    print(content[line])