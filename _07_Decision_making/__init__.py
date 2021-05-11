num = int(input("enter number:"))
if num == 0:
    print("Number is neither positive nor negative")
else:
     if num > 0:
         print("number is positive number")
     else:
         print("Number is negative integer")


age = int(input("Age of a person"))
if age >= 60:
    print("old person")
elif age >= 40 and age < 60:
    print("adult person")
elif age >= 25 and age < 40:
    print("elder person")
elif age >=18 and age < 25:
    print("Teenage person")
elif age >=12 and age < 18:
    print("younger person")
else:
    print("they are children")