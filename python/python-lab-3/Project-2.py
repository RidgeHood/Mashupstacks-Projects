
inp=input("Enter the number:\n")

rfile=open("test.txt",'r')

for line in range(int(inp)):
    print(rfile.readline())