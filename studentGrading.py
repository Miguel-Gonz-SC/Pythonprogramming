print("Student Grading Program \n")
input("Enter Student Name \t," )
input("Enter SC Student ID # \t",)
P = int(input("Enter percentage on assignment # \t",))

if P>=94:
    print("Letter grade : A")
    print("Grade point 4.00")
    print("Excellent performance")
elif P>=90:
    print("Letter grade : A-")
    print("Grade point 3.667")
    print("Excellent performance")
elif P>=87:
    print("Letter grade : B+")
    print("Gradpoint 3.333")
    print("Denotes good performance")
elif P>=84:
    print("Letter grade : B")
    print("Grade point 3.00")
    print("Denotes good performance")
elif P>=80:
    print("Letter grade : B-")
    print("Grade point 2.667")
    print("Denotes good performance")
elif P>=77:
    print("Letter grade : C+")
    print("Grade point 2.333")
    print("Denotes average performance")
elif P>=74:
    print("Letter grade : C")
    print("Grade point 2.00")
    print("Denotes average performance")
elif P>=70:
    print("Letter grade : C-")
    print("Grade point 1.667")
    print("Denotes average performance")
elif P>=65:
    print("Letter grade : D+")
    print("Grade point 1.333")
    print("Denotes unsatisfactory performance")
elif P>=60:
    print("Letter grade : D")
    print("Grade point 1.00")
    print("Denotes unsatisfactory performance")
elif P>=55:
    print("Letter grade : D-")
    print("Grade point 0.667")
    print("Denotes unsatisfactory performance")
elif P<=54.99:
    print("Letter grade : F")
    print("Grade point 0.00")
    print("Denotes failing performance")