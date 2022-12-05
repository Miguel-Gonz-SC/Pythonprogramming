"""
Programmer: Miguel Gonzalez, Zach Hidalgo
Program: carSales
Program version:3.10.8
Created on 10/31/2022 8:26:00
Last modified: 10/31/2022 8:27:00
"""


def carType():
    print("What type of car are you looking for? \n 1 = Truck \n 2. Sedan \n 3. Suv \n 4. Van \n 5. Hatchback "
          "\n 6. Convertible \n 7. Coupe")
    choice = int(input("Select a type of vehicle by entering a number\t"))
    if choice == 1:
        Truck()
    elif choice ==2:
        Sedan()
    elif choice == 3:
        Van()
    elif choice == 4:
        Hatchback()
    elif choice == 5:
        Convertible()
    elif choice == 6:
        Coupe()

# if choice >7, <1
#     carType()    This code is for further Improvement
# return choice

def truckFord():
    print("What model of Ford truck do you want?\n1 = Maverick\n 2 = Ranger\n 3 = F-150\n 4 = F-250\n 5 = F-350\n"
              " 6 = F-450")
    var2 = int(input("Select a model by entering a number\t"))
    if var2 == 1:
        print("The price is $19,995.\n Would you like to pay with cash, card, or take out a loan?")
    elif var2 == 2:
        print("The price is $32,525.\n Would you like to pay with cash, card, or take out a loan?")
    elif var2 == 3:
        print("The price is $78,874.\n Would you like to pay with cash, card, or take out a loan?")
    elif var2 == 4:
        print("The price is $85,535.\n Would you like to pay with cash, card, or take out a loan?")
    elif var2 == 5:
        print("The price is $88,974.\n Would you like to pay with cash, card, or take out a loan?")
    elif var2 == 6:
        print("The price is $93,768.\n Would you like to pay with cash, card, or take out a loan?")
    else:
        print("There is not any vehicles other than the listings sold at our dealership.")
        truckFord()        # use track run var to limit times reruns

def truckChevy():
    print("What model of Chevy truck do you want?\n 1 = Colorado\n 2 = S10 Max\n 3 = Silverado\n 4 = 1500\n 5 = 2500\n 6 = 3500")
    var3 = int(input("Select a model by entering a number\t"))
    if var3 == 1:
        print("The price is $28,000.\n Would you like to pay with cash, card, or take out a loan?")
    elif var3 == 2:
        print("The price is $19,215.\n Would you like to pay with cash, card, or take out a loan?")
    elif var3 == 3:
        print("The price is $35,600.\n Would you like to pay with cash, card, or take out a loan?")
    elif var3 == 4:
        print("The price is $49,200.\n Would you like to pay with cash, card, or take out a loan?")
    elif var3 == 5:
        print("The price is $69,780.\n Would you like to pay with cash, card, or take out a loan?")
    elif var3 == 6:
        print("The price is $93,900.\n Would you like to pay with cash, card, or take out a loan?")
    else:
        print("There is not any vehicles other than the listings sold at our dealership.")

def truckDodge():
    print("What model of Dodge truck do you want?\n 1 = Dakota \n 2 = 1500\n 3 = 2500\n 4 = 3500\n 5 = 4500")
    var4 = int(input("Select a model by entering a number\t"))
    if var4 == 1:
        print("The price is $25,560.\n Would you like to pay with cash, card, or take out a loan?")
    elif var4 == 2:
        print("The price is $42,285.\n Would you like to pay with cash, card, or take out a loan?")
    elif var4 == 3:
        print("The price is $70,955.\n Would you like to pay with cash, card, or take out a loan?")
    elif var4 == 4:
        print("The price is $88,750.\n Would you like to pay with cash, card, or take out a loan?")
    elif var4 == 5:
        print("The price is $97,240.\n Would you like to pay with cash, card, or take out a loan?")
    else:
        print("There is not any vehicles other than the listings sold at our dealership.")

def truckToyota():
    print("What model of Toyota truck do you want?\n 1 = Hilux \n 2 = Tacoma\n 3 = Tundra")
    var5 = int(input("Select a model by entering a number\t"))
    if var5 == 1:
        print("The price is $58,225.\n Would you like to pay with cash, card, or take out a loan?")
    elif var5 == 2:
        print("The price is $49,390.\n Would you like to pay with cash, card, or take out a loan?")
    elif var5 == 3:
        print("The price is $75,245.\n Would you like to pay with cash, card, or take out a loan?")
    else:
        print("There is not any vehicles other than the listings sold at our dealership.")

def truckNissan():
    print("What model of Nissan truck do you want?\n 1 = Frontier\n 2 = Titan")
    var6 = int(input("Select a model by entering a number\t"))
    if var6 == 1:
        print("The price is $39,120.\n Would you like to pay with cash, card, or take out a loan?")
    elif var6 == 2:
        print("The price is $65,070.\n Would you like to pay with cash, card, or take out a loan?")
    else:
        print("There is not any vehicles other than the listings sold at our dealership.")

def truckGMC():
    print("What model of GMC truck do you want?\n 1 = Canyon\n 2 = Sierra\n 3 = 1500\n 4 = 2500\n 5 = 3500")
    var7 = int(input("Select a model by entering a number\t"))
    if var7 == 1:
        print("The price is $45,000.\n Would you like to pay with cash, card, or take out a loan?")
    elif var7 == 2:
        print("The price is $67,000.\n Would you like to pay with cash, card, or take out a loan?")
    elif var7 == 3:
        print("The price is $72,000.\n Would you like to pay with cash, card, or take out a loan?")
    elif var7 == 4:
        print("The price is $79,995.\n Would you like to pay with cash, card, or take out a loan?")
    elif var7 == 5:
        print("The price is $87,985.\n Would you like to pay with cash, card, or take out a loan?")
    else:
        print("There is not any vehicles other than the listings sold at our dealership.")

def suvFord():
    print(
        "What model of Ford SUV do you want?\n1 = Bronco\n2 = EcoSport\n3 = Edge\n4 = Escape\n5 = Expedition\n6 = Explorer" "\n7 = Flex\n8 = Mustang Mach-E")
    _var = int(input("Select a model by entering a number\t"))
    if _var == 1:
        print("The price is $44,495.\n Would you like to pay with cash, card, or take out a loan?")
    elif _var == 2:
        print("The price is $28,545.\n Would you like to pay with cash, card, or take out a loan?")
    elif _var == 3:
        print("The price is $46,675.\n Would you like to pay with cash, card, or take out a loan?")
    elif _var == 4:
        print("The price is $38,515.\n Would you like to pay with cash, card, or take out a loan?")
    elif _var == 5:
        print("The price is $84,670.\n Would you like to pay with cash, card, or take out a loan?")
    elif _var == 6:
        print("The price is $56,275.\n Would you like to pay with cash, card, or take out a loan?")
    elif _var == 7:
        print("The price is $40,740.\n Would you like to pay with cash, card, or take out a loan?")
    elif _var == 8:
        print("The price is $61,690.\n Would you like to pay with cash, card, or take out a loan?")
    else:
        print("There is not any vehicles other than the listings sold at our dealership.")














def Truck():
    print("What brand of truck?\n1 = Ford \n 2 = Chevy \n 3 = Dodge \n 4 = Toyota \n 5 = Nissan \n 6 = GMC")
    var = int(input("Select a brand by entering a number\t"))
    if var == 1:
        truckFord()         #Calling the truckFord function

    elif var == 2:
        truckChevy()


    elif var == 3:
        truckDodge()

    elif var == 4:

        truckToyota()

    elif var == 5:
        truckNissan()

    elif var == 6:
        truckGMC()

def SUV():
    print("What brand of SUV?\n1 = Ford \n 2 = Chevy \n 3 = Dodge \n 4 = Toyota \n 5 = Nissan \n 6 = GMC\n 7 = Kia\n 8 = Infinity")
    var1 = int(input("Select a brand by entering a number\t"))
    if var1 == 1:
        suvFord()

    elif var1 == 2:
        print("What model of Chevy SUV do you want?\n1 = Blazer\n2 = Equinox\n3 = Bolt EUV\n4 = Captiva\n5 = Groove\n6 = Trax" "\n7 = Suburban\n8 = Tahoe")
        _var1 = int(input("Select a model by entering a number\t"))
        if _var1 == 1:
            print("The price is $43,000.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var1 == 2:
            print("The price is $32,600.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var1 == 3:
            print("The price is $29,900.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var1 == 4:
            print("The price is $35,225.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var1 == 5:
            print("The price is $59,700.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var1 == 6:
            print("The price is $21,400.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var1 == 7:
            print("The price is $75,700.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var1 == 8:
            print("The price is $73,000.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif var1 == 3:
        print("What model of Dodge SUV do you want?\n1 = Durango\n2 = Journey")
        _var2 = int(input("Select a model by entering a number\t"))
        if _var2 == 1:
            print("The price is $68,960.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var2 == 2:
            print("The price is $28,959.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif var1 == 4:
        print("What model of Toyota SUV do you want?\n1 = 4Runner\n2 = Aygo\n3 = C-HR\n4 = Corolla Cross\n5 = Front lander" "\n6 = SW4\n7 = Highlander\n8 = Land Cruiser\n9 = Rav 4\n10 = Sequoia")
        _var3 = int(input("Select a model by entering a number\t"))
        if _var3 == 1:
            print("The price is $53,270.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var3 == 2:
            print("The price is $17,800.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var3 == 3:
            print("The price is $23,880.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var3 == 4:
            print("The price is $26,575.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var3 == 5:
            print("The price is $36,420.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var3 == 6:
            print("The price is $62,400.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var3 == 7:
            print("The price is $51,460.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var3 == 8:
            print("The price is $87,995.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var3 == 9:
            print("The price is $41,675.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var3 == 10:
            print("The price is $78,300.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif var1 == 5:
        print("What model of Nissan SUV do you want?\n1 = Ariya\n2 = Juke\n3 = Kicks\n4 = Magnite\n5 = Murano\n6 = Pathfinder" "\n7 = Patrol\n8 = Qashqai\n9 = Rogue\n10 = Terra")
        _var4 = int(input("Select a model by entering a number\t"))
        if _var4 == 1:
            print("The price is $47,125.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var4 == 2:
            print("The price is $30,020.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var4 == 3:
            print("The price is $22,850.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var4 == 4:
            print("The price is $31,420.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var4 == 5:
            print("The price is $46,910.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var4 == 6:
            print("The price is $49,870.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var4 == 7:
            print("The price is $77,760.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var4 == 8:
            print("The price is $47,890.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var4 == 9:
            print("The price is $38,640.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var4 == 10:
            print("The price is $55,000.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif var1 == 6:
        print("What model of GMC SUV do you want?\n1 = Arcadia\n2 = Terrain\n3 = Yukon\n4 = Yukon XL")
        _var5 = int(input("Select a model by entering a number\t"))
        if _var5 == 1:
            print("The price is $47,100.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var5 == 2:
            print("The price is $36,600.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var5 == 3:
            print("The price is $71,400.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var5 == 4:
            print("The price is $84,700.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif var1 == 7:
        print("What model of Kia SUV do you want?\n1 = Soul\n2 = EV6\n3 = K5\n4 = Mohave\n5 = Niro\n6 = KX3\n7 = Sonet" "\n8 = Sorento\n9 = Sportage\n10 = Stonic\n11 = Telluride\n12 = XCEED")
        _var6 = int(input("Select a model by entering a number\t"))
        if _var6 == 1:
            print("The price is $25,390.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 2:
            print("The price is $58,795.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 3:
            print("The price is $31,490.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 4:
            print("The price is $41,100.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 5:
            print("The price is $42,350.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 6:
            print("The price is $29,830.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 7:
            print("The price is $28,700.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 8:
            print("The price is $45,500.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 9:
            print("The price is $42,990.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 10:
            print("The price is $32,490.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 11:
            print("The price is $52,785.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var6 == 12:
            print("The price is $38,420.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif var1 == 8:
        print("What model of Infinity SUV do you want?\n1 = QX50\n2 = QX55\n3 = QX60\n4 = QX80\n5 = ESQ\n6 = QX30\n7 = QX70" "\n8 = EX-Series\n9 = FX")
        _var7 = int(input("Select a model by entering a number\t"))
        if _var7 == 1:
            print("The price is $57,350.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var7 == 2:
            print("The price is $46,500.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var7 == 3:
            print("The price is $65,500.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var7 == 4:
            print("The price is $87,450.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var7 == 5:
            print("The price is $48,200.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var7 == 6:
            print("The price is $41,500.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var7 == 7:
            print("The price is $47,650.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var7 == 8:
            print("The price is $40,650.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var7 == 9:
            print("The price is $61,500.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
def Hatchback():
    print("What brand of Hatchback do you want?\n1 = Ford\n 2 = Chevy\n3 = Toyota\n4 = Nissan\n5 = Kia\n6 = Infinity")
    _var_ = int(input("Select a brand by entering a number\t"))
    if _var_ == 1:
        print("What model of Ford Hatchback do you want?\n1 = C-Max\n2 = Fiesta\n3 = Focus ST\n4 = Focus RS")
        _var_1 = int(input("Select a model by entering a number\t"))
        if _var_1 == 1:
            print("The price is $27,275.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_1 == 2:
            print("The price is $21,230.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_1 == 3:
            print("The price is $41,120.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_1 == 4:
            print("The price is $46,700.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    if _var_ == 2:
        print("What model of Chevy Hatchback do you want?\n1 = Bolt\n2 = Cruze\n3 = Menlo\n4 = Onix\n5 = Spark")
        _var_2 = int(input("Select a model by entering a number\t"))
        if _var_2 == 1:
            print("The price is $31,700.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_2 == 2:
            print("The price is $26,120.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_2 == 3:
            print("The price is $23,500.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_2 == 4:
            print("The price is $34,130.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_2 == 5:
            print("The price is $18,100.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    if _var_ == 3:
        print("What model of Toyota Hatchback do you want?\n1 = Aqua\n2 = Corolla\n3 = Passo\n4 = Yaris")
        _var_3 = int(input("Select a model by entering a number\t"))
        if _var_3 == 1:
            print("The price is $22,250.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_3 == 2:
            print("The price is $26,700.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_3 == 3:
            print("The price is $24,600.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_3 == 4:
            print("The price is $18,750.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    if _var_ == 4:
        print("What model of Nissan Hatchback do you want?\n1 = Leaf\n2 = Micra\n3 = Note\n4 = Tiida")
        _var_4 = int(input("Select a model by entering a number\t"))
        if _var_4 == 1:
            print("The price is $36,040.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_4 == 2:
            print("The price is $24,200.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_4 == 3:
            print("The price is $18,360.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_4 == 4:
            print("The price is $15,700.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    if _var_ == 5:
        print("What model of Kia Hatchback do you want?\n1 = Ceed\n2 = Rio")
        _var_5 = int(input("Select a model by entering a number\t"))
        if _var_5 == 1:
            print("The price is $23,890.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_5 == 2:
            print("The price is $17,190.\n Would you like to pay with cash, card, or take out a loan?")
    if _var_ == 6:
        print("What model of Infinity Hatchback do you want?\n1 = Q30")
        _var_6 = int(input("Select a model by entering a number\t"))
        if _var_6 == 1:
            print("The price is $30,150.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
def Coupe():
    print("What brand of Coupe do you want?\n1 = Ford\n 2 = Chevy\n3 = Toyota\n4 = Nissan\n5 = Dodge\n6 = Infinity")
    _var_7 = int(input("Select a brand by entering a number\t"))
    if _var_7 == 1:
        print(
            "What model of Ford Coupe do you want?\n1 = Mustang\n2 = Mustang Mach-1\n3 = Mustang GT\n4 = Mustang Shelby GT-350"
            "\n5 = Mustang Shelby GT-500\n6 = Mustang Bullitt\n7 = Mustang Boss 302")
        _var_8 = int(input("Select a model by entering a number\t"))
        if _var_8 == 1:
            print("The price is $55,570.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_8 == 2:
            print("The price is $63,790.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_8 == 3:
            print("The price is $60,420.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_8 == 4:
            print("The price is $67,560.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_8 == 5:
            print("The price is $69,420.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_8 == 6:
            print("The price is $74,700.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_8 == 7:
            print("The price is $57,420.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif _var_7 == 2:
        print("What model of Chevy Coupe do you want?\n1 = Camaro\n2 = Corvette")
        _var_9 = int(input("Select a model by entering a number\t"))
        if _var_9 == 1:
            print("The price is $73,300.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_9 == 2:
            print("The price is $126,150.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif _var_7 == 3:
        print("What model of Toyota Coupe do you want?\n1 = GR86\n2 = MK5 Supra")
        _var_10 = int(input("Select a model by entering a number\t"))
        if _var_10 == 1:
            print("The price is $43,240.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_10 == 2:
            print("The price is $110,230.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif _var_7 == 4:
        print("What model of Toyota Coupe do you want?\n1 = GTR\n2 = Z")
        _var_11 = int(input("Select a model by entering a number\t"))
        if _var_11 == 1:
            print("The price is $210,740.\n Would you like to pay with cash, card, or take out a loan?")
        elif _var_11 == 2:
            print("The price is $46,799.\n Would you like to pay with cash, card, or take out a loan?")
        else:
            print("There is not any vehicles other than the listings sold at our dealership.")
    elif _var_7 == 5:
        print("The only model we have is the Dodge Challenger")
        print("The price is $86,645.\n Would you like to pay with cash, card, or take out a loan?")
    elif _var_7 == 6:
        print("The only model we have is the Infinity Q60")
        print("The price is $60,300.\n Would you like to pay with cash, card, or take out a loan?")
def Sedan():
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

def Van():
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
def Convertible():
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
    elif var8 == 2:
        print("What model of Chevy do you want?\n 1 = Camaro \n 2 = Corvette")
        var8 = int(input("Select a model by entering a number\t"))
        if var8 == 1:
            print("The price is $34,905.\n Would you like to pay with cash, card, or take out a loan?")
        if var8 == 2:
            print("The price is $72,000.\n Would you like to pay with cash, card, or take out a loan?")

    # print("There is not any vehicles other than the listings sold at our dealership.")
choiceEntered = carType()

if choiceEntered==1:
    Truck()
elif choiceEntered==2:
    Sedan()
elif choiceEntered==3:
    SUV()
elif choiceEntered==4:
    Van()
elif choiceEntered==5:
    Hatchback()
elif choiceEntered==6:
    Convertible()
elif choiceEntered==7:
    Coupe()