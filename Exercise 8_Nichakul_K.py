nameInput = input("Username : ")
passInput = input("Password : ")
if  nameInput == "min" and passInput == "789":
        print("Welcome !", nameInput)
        print("----- MShop -----")
        print("1. Water     : 10 bath")
        print("2. Green Tea : 40 bath")

        userSelected = int(input("Select >>"))
        userNumber = int(input("How many >>"))
if userSelected == 1:
        price1 = int(10 * userNumber)
        print("Total price:",price1)
elif userSelected == 2:
        price2 = int(40 * userNumber)
        print("Total price:", price2)