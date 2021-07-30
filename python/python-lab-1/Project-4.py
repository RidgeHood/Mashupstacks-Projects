a=""
while a=="":
    a=input("Enter valid number:")
    try:
        a=int(a)
    except:
        print("invalid")
        a=""
        continue

sum=0
for x in range(1,a+1):
    if a%x==0:
        sum=sum+1

print(f"\n The number {a} have {sum} divisor(s)")