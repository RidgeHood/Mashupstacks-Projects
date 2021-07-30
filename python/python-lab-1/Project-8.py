import random as r

a=""
while a=="":
    a=input("Enter valid number between 1-9:")
    try:
        a=int(a)
        if a not in range(0,10):
            raise Exception()
    except:
        print("number not in range")
        a=""
        continue


def predict(num):
    
    rnum=r.randint(1,9)

    if num<rnum:
        print("guessed too low")
    elif num>rnum:
        print("guessed too high")
    elif num==rnum:
        print("Right guess")

predict(a)