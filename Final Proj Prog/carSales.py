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

print("What type of car are you looking for?\n 1 = Truck \n 2 = Sedan \n 3 = Suv \n 4 = Van \n 5 = Hatchback \n 6 ="
      " Convertible \n 7 = Coupe")
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
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $19,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $23,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 3:
            print("The price is $29,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 4:
            print("The price is $16,300.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 2:
        print("What model of Chevy Sedan do you want?\n 1 = Cruze \n 2 = Malibu \n 3 = Monza \n 4 = Onix Plus \n 5 = Optra \n 6 = Aveo")
        var8 = int(input("Select a model by entering a number\t"))
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
    elif var8 == 3:
        print("What model of Kia Sedan do you want?\n 1 = Forte \n 2 = Rio \n 3 = Rio 5-Door \n 4 = Stinger \n 5 = K5")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $19,490.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $16,550.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 3:
            print("The price is $17,490.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 4:
            print("The price is $36,590.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 5:
            print("The price is $25,090.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 4:
        print("What model of Dodge Sedan do you want?\n 1 = Charger \n 2 = Challenger")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $32,645.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $30,940.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 5:
        print("What model of Toyota Sedan do you want?\n 1 = Avalon \n 2 = Camry \n 3 = Supra \n 4 = Corolla \n 5 = GR86 \n 6 = Mirai \n 7 Prius")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $36,825.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $25,845.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 3:
            print("The price is $43,540.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 4:
            print("The price is $20,425.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 5:
            print("The price is $27,700.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 6:
            print("The price is $49,500.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 7:
            print("The price is $25,075.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 6:
        print("What model of Nissan Sedan do you want?\n 1 = Sentra \n 2 = Maxima \n 3 = Altima")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $23,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $29,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 3:
            print("The price is $16,300.\n Would you like to pay with cash, card, or take out a loan?")

if choice == 4:
    print("What brand of Van?\n1 = Ford \n 2 = Chevy \n 3 = Kia \n 4 = Dodge \n 5 = Toyota \n 6 = Nissan \n 7 = GMC")
    var8 = int(input("Select a brand by entering a number\t"))
    if var8 == 1:
        print("What model of Ford Van do you want?\n 1 = E-Transit \n 2 = Transit")
        var2 = int(input("Select a model by entering a number\t"))
        if var2 == 1:
            print("The price is $49,575.\n Would you like to pay with cash, card, or take out a loan?")
        if var2 == 2:
            print("The price is $50,130.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 2:
        print("What model of Chevy Van do you want?\n 1 = Orlando \n 2 = Spin\n 3 = Exspress\n 4 = N300\n 5 = N400")
        var3 = int(input("Select a model by entering a number\t"))
        if var3 == 1:
            print("The price is $51,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var3 == 2:
            print("The price is $43,215.\n Would you like to pay with cash, card, or take out a loan?")
        if var3 == 3:
            print("The price is $45,600.\n Would you like to pay with cash, card, or take out a loan?")
        if var3 == 4:
            print("The price is $49,200.\n Would you like to pay with cash, card, or take out a loan?")
        if var3 == 5:
            print("The price is $69,780.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 3:
        print("What model of Kia Van do you want?\n 1 = Rando \n 2 = Carens \n 3 = Carnival")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $42,490.\n Would you like to pay with cash, card, or take out a loan?")
        elif var8 == 2:
            print("The price is $40,550.\n Would you like to pay with cash, card, or take out a loan?")
        elif var8 == 3:
            print("The price is $47,490.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 4:
        print("What model of Dodge Van do you want?\n 1 = Caravan \n 2 = Cargo")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $52,045.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $42,940.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 5:
        print("What model of Toyota Van do you want?\n 1 = H100 \n 2 = Calya \n 3 = Avanza \n 4 = Sienna \n 5 = Roomy \n 6 = Alphrard \n 7 Proace")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $36,825.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $34,845.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 3:
            print("The price is $43,540.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 4:
            print("The price is $50,425.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 5:
            print("The price is $45,700.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 6:
            print("The price is $49,500.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 7:
            print("The price is $40,075.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 6:
        print("What model of Nissan Van do you want?\n 1 = Caravan \n 2 = Elgrand \n 3 = Livina")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $42,935.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is 50,000.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 3:
            print("The price is $38,300.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 == 7:
        print("What model of GMC Van do you want?\n 1 = Savanna")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $46,000.\n Would you like to pay with cash, card, or take out a loan?")
if choice == 6:
    print("What brand of Convertible?\n 1 = Ford \n 2 = Chevy")
    var8 = int(input("Select a brand by entering a number\t"))
    if var8 == 1:
        print("What model of Ford do you want?\n 1 = Mustang \n 2 = Mustang GT \n 3 = Mustang GT500")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $34,865.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $37,990.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 3:
            print("The price is $47,450.\n Would you like to pay with cash, card, or take out a loan?")
    elif var8 ==2:
        print("What model of Chevy do you want?\n 1 = Camaro \n 2 = Corvette")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $34,905.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $72,000.\n Would you like to pay with cash, card, or take out a loan?")