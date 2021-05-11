ticket = int(input("Enter ticket cost:"))
if ticket > 500 and ticket < 300:
    print(" Enter correct cost of the ticket")
else:
     if ticket == 500:
        print("seat in A/C block")
     elif ticket >=400 and ticket < 500:
        print("seat in A block")
     elif ticket >= 250 and ticket < 400:
        print("seat in B block")
     else:
          print("give correct value of the ticket ")


bill_amount = int(input("enter bill_amount:"))
if bill_amount >= 10000:
     print("10 % discount or mixer grinder")
elif bill_amount <= 5000:
     print("5 % discount or fry pan")
elif bill_amount < 2000 and bill_amount >= 1000:
     print("milk pan")
elif bill_amount
     print("no discount:generate bill")
