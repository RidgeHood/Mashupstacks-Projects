file=open('test.txt',"r")
rfile=file.read()
words=rfile.split(" ")

for y in words:
    print(f"{y} -{words.count(y)}")