

sets={1,2,3,4,5,6,7,8,9,10}

print(f"\nThe Set is : {sets}")

userInput=input("Enter the item to be deleted:")
try:
    userInput=int(userInput)

    if userInput in sets:
        sets.remove(userInput)
    else:
        print("Entered item not in set")
except:
    print("Entered item not in set")


print(f"\nThe Set is : {sets}")