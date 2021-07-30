tup=(1,2,3,4,5,6,7,8,9,10)

enum=list(enumerate(tup))

print(enum)

for x,y in enum:
    print(f"The index of {y} is {x}")