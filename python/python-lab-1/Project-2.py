a=""

while a=="":
    a=input("Enter valid number:")
    try:
        a=int(a)
    except:
        print("invalid")
        a=""
        continue
    

    
def oddeven(num):
    if num%2==0:
        return "EVEN"
    else:
        return "ODD"

print(f"The number you entered is {oddeven(a)}")