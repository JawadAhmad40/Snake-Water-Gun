'''
1 is for sake
-1 for water
0 for gun

'''
computer = -1
youstr = input("Enter your choice: ")
youDict = {"s": 1,
           "w" : -1,
           "g" : 0}
reverseDict = {1: "Snake",
           -1 : "Water",
           0 : "Gun"}
you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if (computer==you):
        print("Its Draw!")
else:
    if (computer ==-1 and you ==1):
        print("you win!")
    elif (computer ==-1 and you ==0):
        print("you loose!")
    elif (computer ==1 and you ==-1):
        print("you loose!")
    elif (computer ==1 and you ==0):
        print("you win!")
    elif (computer ==0 and you ==-1):
        print("you win!")
    elif (computer ==0 and you ==1):
        print("you loose!")
    else:
        print("Print something went wrong")


