def sum(n):
    res=0
    for x in range(0,n,2):
        res=res+(n-x)
    print(res)

inp=int(input("Enter the value for n:"))
sum(inp)    