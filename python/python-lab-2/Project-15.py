import random as r

password=[]

for x in range(10):
    rand=r.randint(33,126)
    rand=chr(rand)
    password.append(rand)
print(f"\nPasword : {''.join(password)}\n")

