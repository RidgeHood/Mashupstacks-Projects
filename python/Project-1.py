from datetime import date as d

name=""
age=""

while name=="":
  name=input("\nEnter name :\t")

while age=="":
  age=input("\nEnter age:\t")
  try:
    age=int(age)
  except:
    print("\nenter valid integer")
    age=""
    continue


def calcAge(uage):
  today=d.today()
  diff=100-uage
  return today.year+diff

print(f"\nHello {name}, you will turn 100yr old in year {calcAge(age)}")