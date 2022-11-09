"""
Programmer: Miguel Gonzalez, Zach Hidalgo
Program: carSales
Program version:3.10.8
Created on 10/31/2022 8:26:00
Last modified: 10/31/2022 8:27:00
"""

"""
Programmers: Zach and Miguel
Program: carSales
Program Version: 3.10.8
Created On: 10/31/2022 8:27:00
Last Modified: 10/31/2022 8:28:00
"""

print("What type of car are you looking for?\n 1 = Truck \n 2 = Sedan \n 3 = Suv \n 4 = Van \n 5 = Hatchback \n 6 = Convertible \n 7 = Coupe")
choice = int(input("Select a type of vehicle by entering a number\t"))
if choice == 1:
    print("What brand of truck?\n1 = Ford \n 2 = Chevy \n 3 = Kia \n 4 = Dodge \n 5 = Toyota \n 6 = Nissan \n 7 = GMC")
    var = int(input("Select a brand by entering a number\t"))
    if var == 1:
        print("What model of Ford truck do you want?\n1 = Maverick\n 2 = Ranger\n 3 = F-150\n 4 = F-250\n 5 = F-350\n 6 = F-450")
        var2 = int(input("Select a model by entering a number\t"))
        if var2 == 1:
            print("The price is $19,995.\n Would you like to pay with cash, card, or take out a loan?")
        if var2 == 2:
            print("The price is $32,525.\n Would you like to pay with cash, card, or take out a loan?")
        if var2 == 3:
            print("The price is $78,874.\n Would you like to pay with cash, card, or take out a loan?")
        if var2 == 4:
            print("The price is $85,535.\n Would you like to pay with cash, card, or take out a loan?")
        if var2 == 5:
            print("The price is $88,974.\n Would you like to pay with cash, card, or take out a loan?")
        if var2 == 6:
            print("The price is $93,768.\n Would you like to pay with cash, card, or take out a loan?")
    if var == 2:
        print("What model of Chevy truck do you want?\n 1 = Colorado\n 2 = S10 Max\n 3 = Silverado\n 4 = 1500\n 5 = 2500\n 6 = 3500")
        var3 = int(input("Select a model by entering a number\t"))
        if var3 == 1:
            print("The price is $28,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var3 == 2:
            print("The price is $19,215.\n Would you like to pay with cash, card, or take out a loan?")
        if var3 == 3:
            print("The price is $35,600.\n Would you like to pay with cash, card, or take out a loan?")
        if var3 == 4:
            print("The price is $49,200.\n Would you like to pay with cash, card, or take out a loan?")
        if var3 == 5:
            print("The price is $69,780.\n Would you like to pay with cash, card, or take out a loan?")
        if var3 == 6:
            print("The price is $93,900.\n Would you like to pay with cash, card, or take out a loan?")
elif choice == 2:
    print("What brand of Sedan?\n1 = Ford \n 2 = Chevy \n 3 = Kia \n 4 = Dodge \n 5 = Toyota \n 6 = Nissan \n 7 = GMC \n 8 = ")
    var8 = int(input("Select a brand by entering a number\t"))
    if var8 == 1:
        print("What model of Ford Sedan do you want?\n 1 = Focus \n 2 = Fusion \n 3 = Taurus \n 4 = Fiesta")
        if var8 == 1:
            print("The price is $19,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $23,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 3:
            print("The price is $29,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 4:
            print("The price is $16,300.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 2:
        print("What model of Ford Sedan do you want?\n 1 = Focus \n 2 = Fusion \n 3 = Taurus \n 4 = Fiesta")
        if var8 == 1:
            print("The price is $19,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $23,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 3:
            print("The price is $29,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 4:
            print("The price is $16,300.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 5:
            print("The price is $29,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 6:
            print("The price is $16,300.\n Would you like to pay with cash, card, or take out a loan?")

