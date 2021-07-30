string=input("Enter string:")

allchars=list(string)
charset=set(allchars)
uniqueChar=list(charset)
uniqueChar.sort()
b={}
print(uniqueChar)

for i in range(0,len(uniqueChar)):

    y=allchars.count(uniqueChar[i])
    print(y)
    b[f"{uniqueChar[i]}"]=f"{y}"

for x,y in b.items():
    print(f"The string has {y} number of '{x}' ")