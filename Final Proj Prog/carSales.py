"""
Programmer: Miguel Gonzalez, Zach Hidalgo
Program: carSales
Program version:3.10.8
Created on 10/31/2022 8:26:00
Last modified: 10/31/2022 8:27:00
"""

print("What make of car are you looking for")
print("We have Trucks, Sedans, Coupes, Hatchbacks, Convertibles, SUV's, and Vans")

P = int(input("Trucks < 1, Sedans < 2, Coupes < 3, Hatchbacks < 4, Convertibles < 5, SUV's < 6 , Vans < 7 \t"))

if P == 1:
    g = open("inputFile")
    print(g.read())
elif P == 2:
    g = open("inputFile")
    print(g.read())
elif P == 3:
    g = open("inputFile")
    print(g.read())
elif P == 4:
    g = open("inputFile")
    print(g.read())
elif P == 5:
    g = open("inputFile")
    print(g.read())
elif P == 6:
    g = open("inputFile")
    print(g.read())
elif P == 7:
    g = open("inputFile")
    print(g.read())