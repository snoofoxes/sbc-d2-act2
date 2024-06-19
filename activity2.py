from random import randint

#HUMPYANG GAME
P1 = input("Enter 'Hayang' or 'Kulob': ")
C2 = randint(1,2)
C3 = randint(1,2)

if C2 == 1:
    C2 = "Hayang"
else:
    C2 = "Kulob"

if C3 == 1:
    C3 = "Hayang"
else:
    C3 = "Kulob"

if (C2 == "Kulob" and C3 == "Kulob" and P1 == "Kulob"):
    print(f"P1 is {P1} and C2 is {C2} then C3 is {C3}. DRAW!")
elif (C2 == "Hayang" and C3 == "Kulob" and P1 == "Kulob"):
    print(f"P1 is {P1} and C2 is {C2} then C3 is {C3}. C2 Win!")
elif (C2 == "Kulob" and C3 == "Hayang" and P1 == "Hayang"):
    print(f"P1 is {P1} and C2 is {C2} then C3 is {C3}. C2 Win!")
elif (C2 == "Kulob" and C3 == "Kulob" and P1 == "Hayang"):
    print(f"P1 is {P1} and C2 is {C2} then C3 is {C3}. P1 Win!")
elif (C2 == "Hayang" and C3 == "Hayang" and P1 == "Kulob"):
    print(f"P1 is {P1} and C2 is {C2} then C3 is {C3}. P1 Win!")
elif (C2 == "Kulob" and C3 == "Hayang" and P1 == "Kulob"):
    print(f"P1 is {P1} and C2 is {C2} then C3 is {C3}. C3 Win!")
elif (C2 == "Hayang" and C3 == "Kulob" and P1 == "Hayang"):
    print(f"P1 is {P1} and C2 is {C2} then C3 is {C3}. C3 Win!")
elif (C2 == "Hayang" and C3 == "Hayang" and P1 == "Hayang"):
    print(f"P1 is {P1} and C2 is {C2} then C3 is {C3}. DRAW!")
else:
    print("Invalid Input")