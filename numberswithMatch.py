"""
Programmer: Miguel Gonzalez
Program: numbersType
Version : 3.7.9
C reated on: 09/26/2022
Last Modified: 09/30/2022

"""


print("Welcome to Mathmatical operations")
print("1 Odd Numbers \n"
      "2 Even Numbers \n"
      "3 Prime Numbers \n"
      "4 Perfect Numbers \n"
      "5 Palindromes")
choice = int(input("Chose one one of the operations by entering a number 1-5 \t"))
if choice == 1:
    print("Odd numbers from first 100 numbers")
    for i in range(0,101):
        if(i%2 !=0):
            print(i,end=" ")
elif choice == 2:
    print("Even numbers from first 100 numbers")
    for i in range(0,101):
        if(i%2 == 0):
            print(i, end=" ")
elif choice == 3:
    print("Prime numbers from first 100 numbers")
    counter = 0
    n = 100
    for n in range(1, 101):
        for i in range(2,int(n/2+1)):
            if n%i == 0:
                counter=counter+1
        if counter == 0:
            print(n, end=" ")
        counter = 0

elif choice == 4:
    print("Perfect numbers from first 100 numbers")
    sum = 0
    check = 0
    n = 100
    for n in range(1, 101):
        for i in range(1, int(n/2+1)):
            check = n % i
            if (check == 0):
                sum = sum + i
        if sum == n:
            print(n,end=" ")
        sum = 0


elif choice == 5:
    print("Palindrome Numbers")
    number=int(input("Enter your number: "))
    reverse=0
    originalNumber=number
    while number > 0:
        remainder=int(number%10)
        reverse=int(reverse*10+remainder)
        number=int(number/10)
    if originalNumber==reverse:
        print(originalNumber, "is a Palindrome Number")
    else:
        print(originalNumber, "is not a Palindrome Number")