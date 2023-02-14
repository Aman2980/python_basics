def Kg():
    if converted > 90:
        print("You fat")
    elif converted < 30:
        print("You got no food")
    else:
        print("You good")
def Lbs():
    if converted > 170:
         print("You fat")
    elif converted < 90:
        print("You got no food")
    else:
        print("You good")

    


weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)s: ")
if unit == "K":
    converted = weight / 2.205
    print(f"You are {converted:.2f} kilos")
    Kg()
elif unit =="L":
    converted = weight * 2.205
    print(f"You are {converted:.2f} pounds")
    Lbs()   
else:
    print("YOU TYPED SOMETHING WRONG")